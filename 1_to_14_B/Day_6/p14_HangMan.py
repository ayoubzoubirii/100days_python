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
words = ["cat","dog","god","car","good","bus","game","man","women","king","price","week","day","same","hello","kids","bad","table","phone","laptop","cafe","water","pen","big","led","floor"]
# words = ["good","week","hello","laptop","floor"]

word = random.choice(words).lower()
# print(word)
blink = []

new_blink = ""
for w in word :
    blink.append("_")

# print(blink)

numL = []
harf_kayn = []
# for b in blink :
#     # blink = ""
#     new_blink += b
# print(new_blink)

gs_letter = input("gess letter : ").lower()
score = 7
while  len(numL)  != len(word) and score != 0 :

    # if  score == 1 :
    #     print(" GAME OVER ")


    if  ( gs_letter not in word  and score != 0 ) or gs_letter == '' :
        if score == 1:
            print(" GAME OVER ")
            score -= 1
            print(HANGMANPICS[0])
        else :

            score -= 1
            print(HANGMANPICS[0])
            del HANGMANPICS[0]
            gs_letter = input("next one gess letter : ").lower()
        
    

    elif gs_letter in word  :
        if gs_letter in harf_kayn :
                print("kayn")


        for  n in range(0,len(word))  :

            if gs_letter == word[n] and n  not in numL   :
                numL.append(n)
                harf_kayn.append(word[n])
                print(harf_kayn) 
                numL.sort()
                # l_inde = word.index(word[n]) 
                # print(numL)
                blink[n] = gs_letter
                print(blink)
                blink_plus= ''.join(blink)
                print(blink_plus)
            
        if blink_plus == word :
            print(" YOU WIN ")
        elif score != 1 and blink_plus != word :    
            gs_letter = input("next one gess letter : ").lower() 
            
import subprocess

def lazygit(commit_message):
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)
        # Commit with the provided message
        subprocess.run(["git", "commit", "-a", "-m", commit_message], check=True)
        # Push the changes
        subprocess.run(["git", "push"], check=True)
        print("Changes have been successfully pushed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running git command: {e}")

# Example usage:
# lazygit("Your commit message here")


            # listblink= list(new_blink)
            # listblink[int(len(listblink) / n)] = gs_letter
    # print(listblink)
                # blink = " "
        
        


        # l_index = int(l_inde)
        # blink[l_inde] = gs_letter
        # print(blink[l_index])
    # for b in blink :
    #     blink = ""
    #     new_blink += b
        # print(new_blink)
    # print(new_blink)    
    # print(blink)
    # print(l_index)
    # if len(numL)  != len(word) :
    #     gs_letter = input("next one gess letter : ")
# print(listblink)
