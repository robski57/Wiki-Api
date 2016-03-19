import wikipedia
import sqlite3
user = input("Please enter a selection: ")



mn = wikipedia.search
print (wikipedia.search(user))

mn = (wikipedia.page(user))
print (wikipedia.page(user))

conn = sqlite3.connect("wiki_database.db")
curs = conn.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS wikiTable (Title TEXT PRIMARY KEY, Url TEXT, Link TEXT )');
curs.execute("INSERT INTO wikiTable (Title) VALUES('Title')");

mn.title
print ("Title: " + mn.title)

mn.url
print("URL: " + mn.url)

mn.content
print(mn.content)

mn.images
print(mn.images)

mn.links[3]
print ("Link: " + mn.links[3])

wikipedia.set_lang("fr")
wikipedia.summary("Facebook", sentences=1)
