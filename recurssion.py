import random
import string
import re



#print("You have ", Guesses, "left")
   # print("you have ", Available_Letters(""), "left")
    
    #check_letter(Guess_letter)
    
   
       

# 
def Available_Letters(Guess_letter, available_letters):
    #available_letters = 'abcdefghijklmnopqrstuvwxyz'
    print("Available letter funct start: ", Guess_letter)
    available_letters = available_letters.replace(Guess_letter,"")
    print("Available letters: ",available_letters)
        
                
def check_letter(Guess_letter, secrete_word, guesses):
    if (Guess_letter not in secret_word):
        
    #(guesses != 0):
        #if (Guess_letter not in secret_word):
        print("Wrong Guess")
        guesses = guesses - 1
        print("You have: ", Guesses(guesses), "left")
    Available_Letters(Guess_letter, available_letters)
    print("The word is: ", Display_word(secrete_word,Guess_letter,display_word))
   # print("DISPLAY WORD", display_word)
    Guess_letter=Take_input()
    print("TAKE input G_L", Guess_letter)
    Available_Letters(Guess_letter, available_letters)
    check_letter(Guess_letter, secret_word, guesses)
    
    
    # if (guesses != 0):
     #   if (Guess_letter in secrete_word):
      #      print("Correct Guess!")
       #     print(Display_word(secrete_word,Guess_letter))
        
        
        
        #    print("You have: ", Guesses(), "left")
            
         #   Available_Letters(Guess_letter) 
          #  Take_input()
           # print(Display_word(secrete_word,Guess_letter))
#            check_letter(Guess_letter,secrete_word)
        
        
        #while (guesses != 0):
         #   recursive_call(guesses)
            
            
    
          
        
        
        
         
        #while (guesses != 0):
            #recursive_call(guesses)
   # else:
    #    print("Oops!You lost all the guesses! End of game")
        
    
def Display_word(secret_word,Guess_letter,display_word):
    #print("start Display func: ", display_word)
    ##N = len(secret_word) 
    #global display_word
    ##display_word = ''.join(random.choice('*') for _ in range(N))
    #display_word = display_word.replace(*,Guess_letter)
    #Finding index of G_L in S_w
    res = None
    for i in range (0, len(secret_word)):
        if secret_word[i] == Guess_letter:
            res = i + 1
            break
    if res == None:
        pass
    else:
        display_word = display_word[:i] + Guess_letter + display_word[i+1:]
        display_word = display_word[:i] + Guess_letter + display_word[i+1:]
        print("IN DISPLAY FUNCTION:", display_word)
        return (display_word)
      
def Guesses(guesses):
    
    #guesses -= 1
    return guesses

def Take_input():
    global Guess_letter
    Guess_letter = input("Guess your letter: ")
    
    print(Guess_letter)
    return Guess_letter
    

"""
def recursive_call(guesses):
    print(Take_input())
    Available_Letters(Guess_letter)
    check_letter(Guess_letter, secret_word)
    
    print(Display_word(secret_word,Guess_letter))
    
"""    
#MAIN
if __name__ == "__main__":
    
    print("Welcome to Hangman")
    WORDLIST_FILENAME = "words.txt"
    global guesses
    guesses = 6
    global available_letters
    available_letters = 'abcdefghijklmnopqrstuvwxyz'
  
    print("Loading word list from file...")
  # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    secret_word = random.choice(wordlist)
    print("secret word is",secret_word)
    N = len(secret_word) 
    
    
    
    display_word = ''.join(random.choice('*') for _ in range(N))
    print("The secret word is: ", display_word)
    
    
    
    
    
    Take_input()
    #Available_Letters(Guess_letter)
    
    check_letter(Guess_letter, secret_word, guesses)
    
    #print(Display_word(secret_word,Guess_letter))