import random
player = int(input("What you choose ? Type 0 for Rock , 1 for Paper or 2 for Scissors"))
bot = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lis =[rock,paper,scissors] 
if player == bot :
    print(lis[player])
    print(lis[bot])
    print("ta3adol")
elif player == 0 or (player == 1 and bot == 0) :
    print(lis[player])
    print(lis[bot])
    print("rbahti")
else :
    print(lis[player])
    print(lis[bot])
    print("khsati")