**Item Catalogue Project**

This project is part of Udacity's Full Stack Web Developer Nanodegree program. It creates a list of centuries and a list of famous entrepreneurs and information about each entrepreneur in each century where uers can add, edit/update and delete entrepreneurs' information. 

**Setup and run the project**

**Requirements**

Python - The code uses Python ver Python 3

Vagrant - A virtual environment builder and manager

VirtualBox - An open source virtualiztion product.

Git - An open source version control system

**How to Run**

1.Install VirtualBox and Vagrant
2.Clone this repository
3.Unzip and place the Item Catalogue Project folder in your vagrant directory
4.Launch Vagrant
```sql
$ Vagrant up
```
5.Login to Vagrant
```sql
$ Vagrant ssh
```
6.Change directory to /vagrant
```sql
$ Cd /vagrant
```
7.Initialize the database
```sql
$ Python database_config.py
```
8.Populate the database with some initial data
```sql
$ Python listofentrepreneurs.py
```
9. Launch application
```sql
$ Python project.py
```
10.Open the browser and go to http://localhost:5000
 
**JSON endpoints**

**Returns JSON of all centuries**
```sql
/century/JSON
```
```sql
/JSON
```

**Returns JSON of a specefic entrepreneur**
```sql
/century/<int:century_id>/list/<int:list_id>/JSON
```
**Returns JSON of a specefic century's entrepreneurs**
```sql
/century/<int:century_id>/list/JSON
```

