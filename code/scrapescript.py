'''
This file will run through a script and
convert it into an intermediate csv format
from which it will be converted into a
character interaction table.
'''

#Import required modules
from bs4 import BeautifulSoup
import csv

with open('./data/deadpool.html') as file:
    soup = BeautifulSoup(file,'html.parser')

#Dictionary of movie characters
#Key: Name of a character
#Value: Set of aliases of a character
movie_alias = dict()

#temp
characters = []
scenes = []

#Read the csv alias file and store it in movie_alias
with open('./data/deadpool_alias.csv', 'rb') as aliases:
    reader = csv.reader(aliases)
    for row in reader:
        movie_alias[row[0]] = set()

i = 0
for b in soup.select('b'):
    element = b.text.strip()
    if "INT." in element or "EXT." in element:
        scenes.append(element)
    elif element in movie_alias:
        characters.append(element)
        print(b.next_sibling)
        print("*****")
    if i > 50:
        break
    i+=1
