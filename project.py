from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_config import Base, Century, Entrepreneur, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

# Connect to Database and create database session

engine = create_engine('sqlite:///entrepreneurslistwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    print "done!"
    return output


@app.route("/gdisconnect")
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# JSON APIs to view Century Information
@app.route('/century/<int:century_id>/list/JSON')
def CenturiessJSON(century_id):
    century = session.query(Century).filter_by(id=century_id).one()
    entrepreneurs = session.query(Entrepreneur).filter_by(century_id=century_id).all()
    return jsonify(Entrepreneurs=[e.serialize for e in entrepreneurs])


@app.route('/century/<int:century_id>/list/<int:list_id>/JSON')
def entrepreneursJSON(century_id, list_id):
    entrepreneur = session.query(Entrepreneur).filter_by(id=list_id).one()
    return jsonify(Entrepreneur=entrepreneur.serialize)


@app.route('/century/JSON')
@app.route('/JSON')
def CenturiesJSON():
    centuries = session.query(Century).all()
    return jsonify(centuries=[c.serialize for c in centuries])


# Show all centuries
@app.route('/')
@app.route('/century/')
def showCenturies():
    centuries = session.query(Century).order_by(asc(Century.name))
    return render_template('centuries.html', centuries=centuries)


# Show a century list
@app.route('/century/<int:century_id>/')
@app.route('/century/<int:century_id>/list/')
def showList(century_id):
    century = session.query(Century).filter_by(id=century_id).one()
    entrepreneurs = session.query(Entrepreneur).filter_by(century_id=century_id).all()
    return render_template('entrepreneurs.html', entrepreneurs=entrepreneurs, century=century)


# Create a new entrepreneur
@app.route('/century/<int:century_id>/list/new/', methods=['GET', 'POST'])
def newEntrepreneur(century_id):
    if 'username' not in login_session:
        return redirect('/login')

    century = session.query(Century).filter_by(id=century_id).one()
    if request.method == 'POST':
        newEntrepreneur = Entrepreneur(name=request.form['name'], information=request.form['information'], century_id=century_id, user_id=century.user_id)
        session.add(newEntrepreneur)
        session.commit()
        return redirect(url_for('showList', century_id=century_id))
    else:
        return render_template('newentrepreneur.html', century_id=century_id)

# show information
@app.route('/century/<int:century_id>/list/<int:list_id>/information')
def showInformation(century_id, list_id):
    entrepreneur = session.query(Entrepreneur).filter_by(id=list_id).one()
    century = session.query(Century).filter_by(id=century_id).one()
    entrepreneurs = session.query(Entrepreneur).filter_by(century_id=century_id).all()
    return render_template('information.html', century_id=century_id, list_id=list_id, entrepreneur=entrepreneur)


# Edit an entrepreneur
@app.route('/century/<int:century_id>/list/<int:list_id>/edit', methods=['GET', 'POST'])
def editEntrepreneur(century_id, list_id):

    if 'username' not in login_session:
        return redirect('/login')

    editedEntrepreneur = session.query(Entrepreneur).filter_by(id=list_id).one()
    century = session.query(Century).filter_by(id=century_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedEntrepreneur.name = request.form['name']
        if request.form['information']:
            editedEntrepreneur.information = request.form['information']
        session.add(editedEntrepreneur)
        session.commit()
        return redirect(url_for('showList', century_id=century_id))
    else:
        return render_template('editentrepreneur.html', century_id=century_id, list_id=list_id, entrepreneur=editedEntrepreneur)


# Delete a menu item
@app.route('/century/<int:century_id>/list/<int:list_id>/delete', methods=['GET', 'POST'])
def deleteEntrepreneur(century_id, list_id):

    if 'username' not in login_session:
        return redirect('/login')

    century = session.query(Century).filter_by(id=century_id).one()
    entrepreneurToDelete = session.query(Entrepreneur).filter_by(id=list_id).one()
    if request.method == 'POST':
        session.delete(entrepreneurToDelete)
        session.commit()
        return redirect(url_for('showList', century_id=century_id))
    else:
        return render_template('deleteentrepreneur.html', entrepreneur=entrepreneurToDelete)


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception:
        return None


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
