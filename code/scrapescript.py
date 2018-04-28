'''
This file will run through a script and
convert it into an intermediate text format
from which it will be converted into a
character interaction table.
'''

#Import required modules
from bs4 import BeautifulSoup
from bs4 import Tag
import os
import re
import csv

screenplay = "toystory"

with open('./data/'+ screenplay + '.html') as file:
    soup = BeautifulSoup(file,'html.parser')

#Dictionary of movie characters
#Key: Name of a character
#Value: Set of aliases of a character
movie_alias = dict()


#Read the csv alias file and store it in movie_alias
with open('./data/' + screenplay + '_alias.csv', 'rb') as aliases:
    reader = csv.reader(aliases)
    for row in reader:
        movie_alias[row[0]] = set()

file_path = os.path.abspath('./out/' + screenplay + '_updated.txt')
with open(file_path,'w+') as updated_file:
    for b in soup.select('b'):
        #remove extra whitespace
        element = b.text.strip()
        #remove words in parentheses to get rid of (CONTD.)
        element = re.sub(r'\([^)]*\)', '', element)
        element = element.strip()

        character = ""
        if "INT." in element or "EXT." in element:
            updated_file.write('----------------------------------------\n')
            updated_file.write('# ' + element + '\n')
        elif element in movie_alias and element != '':
            updated_file.write(element+': ')
            character = element
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
                if line != "" and character != "":
                    dialogue = dialogue + " " + line
            else:
                line = line.strip()
                if line != "":
                    action = action + " " + line

        dialogue = re.sub(r'[:]','',dialogue)
        dialogue = re.sub(r'\.{3}',' ', dialogue)
        dialogue = re.sub(r'\s+',' ', dialogue)
        dialogue = re.sub(r'[\'\"]',' ', dialogue)
        dialogue = dialogue.strip()
        action = re.sub(r'[:]','',action)
        action = re.sub(r'\.{3}', ' ', action)
        action = re.sub(r'\s+', ' ', action)
        action = re.sub(r'[\'\"]',' ', action)
        action = action.strip()

        if dialogue != "":
            updated_file.write(dialogue + '\n')
        if action != "":
            updated_file.write('###  [' + action + '] \n')
