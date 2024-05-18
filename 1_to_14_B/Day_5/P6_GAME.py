print('''                         /
                              /\  //\\
                       /\    //\\///\\\        /
                      //\\  ///\////\\\\  /\  //\\
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ 
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo ''')

start = input(" hello and welcome in my Game FIND KING \n just say Y or N").lower()
if start == "y" :
    q1 = int(input("let start the game |\n You have in front of you to doors witch one you will choise  ? 1 or 2 ? "))
    if q1 == 1 :
        q2 = int(input("Good you are in the way keep going to find the king |\n You have in front of you to doors witch one you will choise  ? 1 or 2 ? "))
        if q2 == 2 : 
            q3 = int(input("Good you are in the way keep going to find the king |\n You have in front of you to doors witch one you will choise  ? 1 or 2 ? "))
            if q3 == 2 : 
                print (" YOU WIN , YOU FIND THE KING")
            else :
                print("GAME OVER ? YOU FIND DINASOR")
        else : 
         print("GAME OVER ! MAFIA FIND YOU ")
    else : 
        print("GAME OVER ! YOU FILL IN HOL ")
else :
    print("OK BYE hhh you can Start the game later ")     
       
    


