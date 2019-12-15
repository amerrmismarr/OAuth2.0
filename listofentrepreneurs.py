from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_config import Century, Base, Entrepreneur, User

engine = create_engine('sqlite:///entrepreneurslistwithusers.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


User1 = User(name="Amer", email="amerrmismarr@gmail.com")
session.add(User1)
session.commit()

# 17th Century entrepreneurs
century17 = Century(user_id=1, name="17th century entrepreneurs")
session.add(century17)
session.commit()

entrepreneur1 = Entrepreneur(user_id=1, name="Regina Basilier (1572-1631)", century=century17, information="She was born in Danzig and married to the Hamburg merchant Adam Basilier, who was a significant creditor of the Swedish prince John, Duke of Ostergotland. Upon the death of Prince John in 1618, she emigrated to Sweden to protect her interests. She acquired the estates Kungs Norrby in Ostergotland as well as Gripsholm, Vibyholm, and Akers in Sodermanland, from the crown as leasehold estates. Regina Basilier was one of the greatest creditors of the Swedish royal house and often provided the crown with financial loans as well as supplies from her Swedish leasehold estates. She also continued a lucrative trading import business of textiles and jewelry and was a provider of such luxury items to the Swedish royal family. She is, for example, recorded to have sold bed draperies to Christina of Holstein-Gottorp, wallpaper to Gustavus Adolphus of Sweden, and jewelry for Maria Eleonora of Brandenburg.")
session.add(entrepreneur1)
session.commit()

entrepreneur2 = Entrepreneur(user_id=1, name="Birgitta Durell (1619-1683)", century=century17, information="Brechtgien Durell, nee von Crakow or von Cracauw (1619 in Hoorn, the Netherlands - 1683 in Sweden) was a Swedish (originally Dutch) industrialist. She was the daughter of Carel van Cracauw, the Dutch envoy to Copenhagen, a rich heiress and related to rich bankers. In 1647, she married the rich Swedish merchant Magnus Durell, who had been ennobled not long before their wedding. She followed her spouse to Sweden and settled on his recently acquired country estate, Vallen Castle near Laholm.")
session.add(entrepreneur2)
session.commit()

entrepreneur3 = Entrepreneur(user_id=1, name="Louis De Geer (1587-1652)", century=century17, information="Louis De Geer (17 November 1587 - 19 June 1652) was a Netherlandish entrepreneur and industrialist of Walloon origin. An early pioneer of outward foreign direct investment in the early modern period, he is considered by many as the father of Swedish industry for introducing Walloon blast furnaces in Sweden. He produced cannons for the German Protestant movement, the Dutch navy and the Dutch East India Company and the Dutch West India Company.")
session.add(entrepreneur3)
session.commit()

entrepreneur4 = Entrepreneur(user_id=1, name="Isaac Le Maire (ca.1558-1624)", century=century17, information="Isaac Le Maire (c. 1558 in Tournai - September 20, 1624 in Egmond aan den Hoef) was a Walloon-born Dutch entrepreneur, investor, and a sizeable shareholder of the Dutch East India Company (VOC). He is best known for his constant strife with the VOC, which ultimately led to the discovery of Cape Horn.")
session.add(entrepreneur4)
session.commit()

entrepreneur5 = Entrepreneur(user_id=1, name="Johan Palmstruch (1611-1671)", century=century17, information="Johan (Hans) Wittmacher was born in Riga where his father was a merchant. Sometime in the 1630s, he moved to Amsterdam where he married Margrieta van der Bosch (1617-1677) in February 1644. He became a commissioner in the National Board of Trade after his arrival in Sweden in 1647 and began submitting proposals for banking institutions to King Charles X Gustav in the 1650s. The first two such proposals were rejected but the third, which promised half the bank's profits to the crown, was accepted. He was made a Swedish nobleman under the surname Palmstruch and become a commissioner at the National College of Commerce.")
session.add(entrepreneur5)
session.commit()

entrepreneur6 = Entrepreneur(user_id=1, name="Pierre-Paul Riquet (1609-1680)", century=century17, information="Pierre-Paul Riquet, Baron de Bonrepos (29 June 1609 (some sources say 1604) - 4 October 1680) was the engineer and canal-builder responsible for the construction of the Canal du Midi.")
session.add(entrepreneur6)
session.commit()

# 18th Century entrepreneurs
century18 = Century(user_id=1, name="18th century entrepreneurs")
session.add(century18)
session.commit()

entrepreneur1 = Entrepreneur(user_id=1, name="Anna Elisabeth Baer", century=century18, information="Anna Elisabeth Baer nee Carlbohm (1722-1799) was a Finnish merchant and shipowner. She was one of the richest merchants in the latter half of the 18th century in Turku, Finland.")
session.add(entrepreneur1)
session.commit()

entrepreneur2 = Entrepreneur(user_id=1, name="Samuel Crompton", century=century18, information="Samuel Crompton (3 December 1753 - 26 June 1827) was an English inventor and pioneer of the spinning industry. Building on the work of James Hargreaves and Richard Arkwright he invented the spinning mule, a machine that revolutionized the industry worldwide.")
session.add(entrepreneur2)
session.commit()

entrepreneur3 = Entrepreneur(user_id=1, name="Caroline Gother", century=century18, information="Caroline Gother (1761-1836) was a Swedish banker. She was born to Maria Elisabeth Bedoir (1726-1783) and the rich merchant and city official Engelbert Gother (1708-1775). Her father died bankrupted and her sisters swiftly married in order to support themselves: she, however, chose to become a governess. She corresponded with the poet Johan Elers.")
session.add(entrepreneur3)
session.commit()

entrepreneur4 = Entrepreneur(user_id=1, name="Johns Hopkins", century=century18, information="Johns Hopkins (May 19, 1795 - December 24, 1873) was an American entrepreneur, abolitionist and philanthropist of 19th-century Baltimore, Maryland. His bequests founded numerous institutions bearing his name, most notably Johns Hopkins Hospital, and Johns Hopkins University (including its academic divisions such as Johns Hopkins School of Nursing, Johns Hopkins School of Medicine, Johns Hopkins Carey Business School, Johns Hopkins Bloomberg School of Public Health, and Johns Hopkins School of Advanced International Studies).")
session.add(entrepreneur4)
session.commit()

entrepreneur5 = Entrepreneur(user_id=1, name="Anna Lisa Jermen", century=century18, information="Anna Lisa Jermen or Jarmen (27 March 1770 - 11 March 1799) was a Finnish entrepreneur. She was born to Johan Jermen and Stina Matsintytar in Turku. She married the sailor Henrik Ambolin (1752-1796) in 1791, and the sailor Wilhelm Sparfven in 1797. Being married to sailors (who by profession were absent most of the time), suffering from consumption and with two small daughters, Anna Lisa Jermen knitted socks to sell. She was successful, which is evident as she was able to buy her home and left jewelry and expensive clothes and textiles after her death, and managed to support both herself, her daughters and spouses.")
session.add(entrepreneur5)
session.commit()

entrepreneur6 = Entrepreneur(user_id=1, name="Anna Lohe", century=century18, information="Anna Lohe nee Blume (1654 - 23 January 1731), was a Swedish banker. She was the daughter of Tobias Blume, a pastry maker of the royal Swedish court, and Anna Techlin. She married Johan Lohe (1643-1704) in 1673, with whom she had eighteen children. Her husband was one of the richest people in Sweden and managed a trading company, a shipping business, a sugar refinery and ironworks. However, he became most known for his banking business as a moneylender, by which he acquired an enormous fortune and counted the king of Sweden among his clients; he was ennobled in 1703.")
session.add(entrepreneur6)
session.commit()


# 19th Century entrepreneurs
century19 = Century(user_id=1, name="19th century entrepreneurs")
session.add(century19)
session.commit()


entrepreneur1 = Entrepreneur(user_id=1, name="John Jacob Astor", century=century19, information="John Jacob Astor (born Johann Jakob Astor; July 17, 1763 - March 29, 1848) was a German-American businessman, merchant, real estate mogul and investor who mainly made his fortune in fur trade and by investing in real estate in or around New York City.")
session.add(entrepreneur1)
session.commit()

entrepreneur2 = Entrepreneur(user_id=1, name="Augusta Bjorkenstam", century=century19, information="Augusta Bjorkenstam (3 December 1829 - 10 July 1892) was a Swedish countess and businessperson. She founded the transport company Stockholms Expressbyra (1877), which managed the transport of luggage from the Stockholm Central Train Station to its recipients. Her company was eventually also engaged by the authorities, the customs, railway stations, boat traffic and shops as well as the postal offices.")
session.add(entrepreneur2)
session.commit()

entrepreneur3 = Entrepreneur(user_id=1, name="Andrew Carnegie", century=century19, information="Andrew Carnegie (November 25, 1835 - August 11, 1919) was a Scottish-American industrialist, business magnate, and philanthropist. Carnegie led the expansion of the American steel industry in the late 19th century and became one of the richest Americans in history. He became a leading philanthropist in the United States and in the British Empire. During the last 18 years of his life, he gave away $350 million (conservatively $65 billion in 2019 dollars, based on percentage of GDP) to charities, foundations, and universities - almost 90 percent of his fortune.")
session.add(entrepreneur3)
session.commit()

entrepreneur4 = Entrepreneur(user_id=1, name="James Buchanan Duke", century=century19, information="James Buchanan Duke (December 23, 1856 - October 10, 1925) was an American tobacco and electric power industrialist best known for the introduction of modern cigarette manufacture and marketing, and his involvement with Duke University.")
session.add(entrepreneur4)
session.commit()

entrepreneur5 = Entrepreneur(user_id=1, name="Thomas Alva Edison", century=century19, information="Thomas Alva Edison (February 11, 1847 - October 18, 1931) was an American inventor and businessman who has been described as America's greatest inventor. He developed many devices in fields such as electric power generation, mass communication, sound recording, and motion pictures. These inventions, which include the phonograph, the motion picture camera, and the long-lasting, practical electric light bulb, have had a widespread impact on the modern industrialized world. He was one of the first inventors to apply the principles of organized science and teamwork to the process of invention, working with many researchers and employees.")
session.add(entrepreneur5)
session.commit()


# 20th Century entrepreneurs
century20 = Century(user_id=1, name="20th century entrepreneurs")
session.add(century20)
session.commit()


entrepreneur1 = Entrepreneur(user_id=1, name="Agha Hasan Abedi", century=century20, information="Agha Hasan Abedi (14 May 1922 - 5 August 1995) was a Pakistani banker and philanthropist. Abedi founded Bank of Credit and Commerce International (BCCI) in 1972. Abedi underwent a heart transplant operation in 1988, and died of a heart attack on 5 August 1995 in Karachi.")
session.add(entrepreneur1)
session.commit()

entrepreneur2 = Entrepreneur(user_id=1, name="Paul Allen", century=century20, information="Paul Gardner Allen (January 21, 1953 - October 15, 2018) was an American business magnate, researcher, investor, and philanthropist. He is best known for co-founding Microsoft Corporation alongside Bill Gates in 1975, which helped spark the microcomputer revolution of the 1970s and 1980s and later became the world's largest personal computer software company. Allen was ranked as the 44th-wealthiest person in the world by Forbes in 2018, and had an estimated net worth of $20.3 billion at the time of his death.")
session.add(entrepreneur2)
session.commit()

entrepreneur3 = Entrepreneur(user_id=1, name="Dhirubhai Ambani", century=century20, information="Dhirajlal Hirachand Ambani, popularly known as Dhirubhai Ambani (28 December 1932 - 6 July 2002) was an Indian business tycoon who founded Reliance Industries in Bombay and appeared in The Sunday Times top 50 businessmen in Asia. Ambani took Reliance public in 1977 and was worth $25.6 billion upon his death on 6 July 2002. In 2016, he was honored posthumously with the Padma Vibhushan, India's second highest civilian honour for his contributions to trade and industry.")
session.add(entrepreneur3)
session.commit()

entrepreneur4 = Entrepreneur(user_id=1, name="Mary Kay Ash", century=century20, information="Mary Kay Ash (May 12, 1918 - November 22, 2001) was an American businesswoman and founder of Mary Kay Cosmetics, Inc.")
session.add(entrepreneur4)
session.commit()

entrepreneur5 = Entrepreneur(user_id=1, name="Bang Si-hyuk", century=century20, information="Bang Si-hyuk (born August 9, 1972), known professionally as Hitman Bang (stylized as hitman bang), is a South Korean lyricist, composer, producer, and record executive. He is the founder and co-CEO of Big Hit Entertainment.")
session.add(entrepreneur5)
session.commit()

entrepreneur6 = Entrepreneur(user_id=1, name="Otto Beisheim", century=century20, information="Otto Beisheim (3 January 1924 - 18 February 2013[1]) was a German businessman and founder of Metro AG. In 2010, his net worth was estimated at US $3.6 billion.")
session.add(entrepreneur6)
session.commit()


# 21st Cenutury entrepreneurs
century21 = Century(user_id=1, name="21st century entrepreneurs")
session.add(century21)
session.commit()

entrepreneur1 = Entrepreneur(user_id=1, name="Brian Acton", century=century21, information="Brian Acton (born February 17, 1972) is an American computer programmer and Internet entrepreneur. Acton is the Executive Chairman of the Signal Foundation, which he co-founded with Moxie Marlinspike in 2018.")
session.add(entrepreneur1)
session.commit()

entrepreneur2 = Entrepreneur(user_id=1, name="Charles T. Akre", century=century21, information="Charles T. Akre is an American investor, financier and businessman. He is on the board of directors of Enstar Group, Ltd., a Bermuda run-off reinsurance company, he is also the founder, chairman and chief investment officer of Akre Capital Management, FBR Focus, and other funds. Akre Capital Management is based in Middleburg, Virginia.")
session.add(entrepreneur2)
session.commit()

entrepreneur3 = Entrepreneur(user_id=1, name="Folorunso Alakija", century=century21, information="Folorunso Alakija (born 15 July 1951) is a Nigerian billionaire businesswoman. She is involved in the fashion, oil, real estate and printing industries. She is the group managing director of The Rose of Sharon Group which consists of The Rose of Sharon Prints & Promotions Limited, Digital Reality Prints Limited and the executive vice-chairman of Famfa Oil Limited. She also has a majority stake in DaySpring Property Development company. Alakija is ranked by Forbes as the richest woman in Nigeria with an estimated net worth of $1 billion.")
session.add(entrepreneur3)
session.commit()

entrepreneur4 = Entrepreneur(user_id=1, name="Rod Aldridge", century=century21, information="Sir Rodney Malcolm Aldridge OBE FRSA (born 7 November 1947) is the founder and former executive chairman of Capita, a British company specialising in business process outsourcing.")
session.add(entrepreneur4)
session.commit()

entrepreneur5 = Entrepreneur(user_id=1, name="Qais Al Khonji", century=century21, information="Qais Al Khonji is an Omani businessman and entrepreneur. He is the founder of Qais United Enterprises Trading and Genesis International. He serves as a board member for many Omani companies and is known for assisting Omani citizens with overcoming the hurdles of starting small businesses in the country.")
session.add(entrepreneur5)
session.commit()

print "added menu items!"
