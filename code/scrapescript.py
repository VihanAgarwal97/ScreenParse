'''
This file will run through a script and
convert it into an intermediate text format
from which it will be converted into a
character interaction table.
'''

#Import required modules
from bs4 import BeautifulSoup
from bs4 import Tag
import csv
import re

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


for b in soup.select('b'):
    #remove extra whitespace
    element = b.text.strip()
    #print(element)
    #remove words in parentheses to get rid of (CONTD.)
    element = re.sub(r'\([^)]*\)', '', element)
    element = element.strip()
    #print(element)


    if "INT." in element or "EXT." in element:
        print("Scene: " + element)
    elif element in movie_alias and element != "":
        print("Character: " + element)
    if isinstance(b.next_sibling, Tag):
        continue

    block = b.next_sibling.encode(encoding="UTF-8")
    block = re.sub(r'\([^)]*\)', '', block, re.M)
    lines = []
    lines = block.split('\n')
    dialogue = ""
    action = ""
    for line in lines:
        if line.startswith("           "):
            line = line.strip()
            if line != "":
                dialogue = dialogue + " " + line
        else:
            line = line.strip()
            if line != "":
                action = action + " " + line

    dialogue = re.sub(r'[:]','',dialogue)
    dialogue = re.sub(r'\s+',' ', dialogue)
    dialogue = re.sub(r'\.+','.', dialogue)
    dialogue = dialogue.strip()
    action = re.sub(r'[:]','',action)
    action = re.sub(r'\s+', ' ', action)
    action = re.sub(r'\.+', '.', action)
    action = action.strip()

    if dialogue != "":
        print("Dialogue: " + dialogue)
    if action != "":
        print("Action: " + action)
    print("*****")

# cow = "DEADPOOL (CONT'D)"
# cow = re.sub(r'\([^)]*\)', '', cow)
# print(cow)
