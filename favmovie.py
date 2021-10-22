import sqlite3

# Create a Database instance using connection and cursor
#Connecting the database

connection = sqlite3.connect('favmovie_sqlite.db')

cursor = connection.cursor()

# Create a TABLE movies that stores values

command="""CREATE TABLE IF NOT EXISTS movies(m_id INTEGER PRIMARY KEY, name TEXT, director TEXT, actor TEXT, actress TEXT, year of release INTEGER)"""

cursor.execute(command)

# Insert the data to the TABLE

cursor.execute("INSERT or IGNORE INTO movies VALUES(1, 'E.T. The Extra-Terrestrial' , 'Steven Spielberg' , ' Henry Thomas' , 'Drew Barrymore' , '1982' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(2, 'Star Wars' , 'George Lucas' , 'Mark Hamill' , 'Carrie Fisher' , '1977' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(3, 'Bach to Future' , 'Robert Zemeckis' , 'Michael J. Fox' , ' Lea Thompson' , '1985' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(4, 'Gone With the Wind' , 'Victor Fleming' , 'Clark Gable' , 'Vivien Leigh' , '1939' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(5, 'The Sound of Music' , 'Robert Wise' , 'Christopher Plummer' , 'Julie Andrews' , '1965' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(6, 'Singin in the Rain' , 'Stanley Donen' , 'Gene Kelly' , 'Debbie Reynolds' , '1952' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(7, 'When Harry Met Sally' , 'Rob Reiner' , 'Billy Crystal' , 'Meg Ryan' , '1989' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(8, 'Toy Story' , 'John Lasseter' , 'Tom Hanks' , 'Annie Potts' , '1995' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(9, 'Kung Fu Panda' , 'Mark Osborne' , 'Jack Black' , 'Angelina Jolie' , '2008' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(10, 'The Matrix' , 'Lana Wachowski' , 'Keanu Reeves' , 'Carrie-Anne Moss' , '1999' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(11, 'Titanic' , 'James Cameron' , 'Leonardo DiCaprio' , 'Kate Winslet' , '1997' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(12, 'Finding Nemo' , 'Andrew Stanton' , 'Albert Brooks' , 'Ellen DeGeneres' , '2003' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(13, 'Mary Poppins' , 'Robert Stevenson' , 'Dick Van Dyke' , 'Julie Andrews' , '1964' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(14, 'Avatar' , 'James Cameron' , 'Sam Worthington' , 'Zoe Saldana' , '2009' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(15, 'Gladiator' , 'Ridley Scott' , 'Russell Crowe' , 'JConnie Nielsen' , '2000' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(16, 'Rocky' , 'John G. Avildsen' , 'Sylvester Stallone' , 'Talia Shire' , '1976' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(17, 'Interstellar' , ' Christopher Nolan' , 'Matthew McConaughey' , 'Anne Hathaway' , '2014' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(18, 'Jurassic Park' , 'Steven Spielberg' , 'Sam Neill' , 'Laura Dern' , '1993' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(19, 'Sherlock Holmes' , 'Guy Ritchie' , 'Robert Downey Jr.' , 'Rachel McAdams ' , '2010' )")
cursor.execute("INSERT or IGNORE INTO movies VALUES(20, 'Home Alone' , 'Chris Columbus' , 'Macaulay Culkin' , 'Catherine O Hara ' , '2001' )")


# Retrieve the results

cursor.execute("SELECT * FROM movies")

results1 = cursor.fetchall()

print(results1)

cursor.execute("SELECT name FROM movies WHERE director ='Brad Bird'")

results2 = cursor.fetchall()

print(results2)

# Commit changes
connection.commit()

# Close database connection
connection.close()
