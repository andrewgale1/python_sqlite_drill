
#task: create dB table in RAM named Roster, include name,species,iq fields.
#populate table with given values, update the species of K.D. to human.
#display names and iq of humans in dB.


import sqlite3

connection = sqlite3.connect(':memory:')
c = connection.cursor()

c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

rosterValue1 = ('Jean-Baptiste Zorg','Human',122)
rosterValue2 = ('Korben Dallas','Meat Popsicle',100)
rosterValue3 = ("Ak'not",'Mangalore',-5)

c.execute("INSERT INTO Roster VALUES (?,?,?)",rosterValue1)
c.execute("INSERT INTO Roster VALUES (?,?,?)",rosterValue2)
c.execute("INSERT INTO Roster VALUES (?,?,?)",rosterValue3)

c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?", ('Human','Korben Dallas',100))

c.execute("SELECT Name,IQ FROM Roster WHERE Species='Human'")
for row in c.fetchall():
    print row
