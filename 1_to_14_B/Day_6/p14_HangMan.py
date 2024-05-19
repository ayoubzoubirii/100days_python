import random 

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ["cat","dog","god","car","bus","game","man","women","king","price","week","day","same","hello","kids","bad","table","phone","laptop","cafe","water","pen","big","led","floor"]
word = random.choice(words)
print(word)
blink = ""

for w in word :
    blink += "_"

print(blink)   
# print("Hello and welcome in game Hang man")
