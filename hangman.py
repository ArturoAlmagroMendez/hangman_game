import random
import os
from images import *

foopath = "Files/data.txt"
foopath2 = "C:/Users/Arturo/Desktop/Workspace/hangman_game/Files/data.txt"
fails = 0



def obtain_random_word():
    list_of_words = []
    with open(foopath, "r" , encoding="utf-8") as f:
        for line in f:
            list_of_words.append(line.strip())
    random_word = random.choice(list_of_words).lower()
    return random_word


def print_menu(images_hangman,random_word,fails,secret_list):
    print(random_word)
    print(f"{images_hangman[fails]}")
    print_secret_word(secret_list)


def print_secret_word(secret_list): 
    for i in secret_list:
        print(i , end=" ")
   

def obtain_secret_word_and_list(random_word):
    secret_word = "_" * len(random_word)
    secret_list = list(secret_word)
    return secret_list

    
def is_contained(random_word,user_input,secret_list):
    global fails
    if user_input in random_word:
        for i in range(len(list(random_word))):
            indexes = [i for i ,c in enumerate(list(random_word)) if c == user_input]
        for i in indexes:
            if user_input in list(random_word):
                secret_list[i] = user_input
    
    
        #os.system("clear")      
        

    else:
        fails += 1

    return fails
        
    
def run():
    
    print("Welcome to the developer Hangman Game,all the words are programming languages =)")
    random_word = obtain_random_word()
    secret_list = obtain_secret_word_and_list(random_word)
    print_menu(images_hangman,random_word,fails,secret_list)
    user_input = input("\n \n Choose a character :")
    is_contained(random_word,user_input,secret_list)
    #random_word_list = list(random_word)
    while fails < 6:
        print_menu(images_hangman,random_word,fails,secret_list)
        if secret_list == list(random_word):
            print(f"{game_win[0]}")
            exit()
        user_input = input("\n \n Choose a character :")
        is_contained(random_word,user_input,secret_list)

    print(f"{images_hangman[fails]}{game_over[0]}")
    


if __name__ == '__main__':
    run()
