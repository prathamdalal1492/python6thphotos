from __future__ import print_function
import random  
secret = "hello"
tracker = True 
letters_guessed=[]
Times_wrong=[]
Times_wrong_count = 0 

def taking_inputs(): 
    input_taker = raw_input("Guess one letter: ")
    letters_guessed.append(input_taker)
    if input_taker not in secret: 
        Times_wrong.append('Wrong')
        Times_wrong_count = 10 - len(Times_wrong) 
        print("You have ",Times_wrong_count,"guesses left") 
    return   

def hangman_display(secret) : 
    taking_inputs()
    dis_word = ''  
    for char in secret:  
        if char in letters_guessed:  
            dis_word += char 
        elif char == ' ': 
            dis_word += char
        else:
            dis_word += '-'  
    answer=dis_word 
    return answer
    
def many_tries(): 
    global tracker
    while len(Times_wrong) < 10 and tracker == True : 
        dis_word=''
        answer = hangman_display(secret)
        print(answer)
        if secret == answer:
            print("Congratulations you win")
            tracker = False
            break 
        if len(Times_wrong) >= 10: 
            print("You ran out of guesses")
            user_choice = raw_input("Would you like to play again. Type Y or N ")
            if user_choice == "Y":
                Times_wrong_count=0 
                for count in range(len(Times_wrong)):
                    del Times_wrong[0]
                for counting in range (len(letters_guessed)):
                    del letters_guessed[0]
                else:
                    print(len(letters_guessed))
                    print(len(Times_wrong))
                    many_tries()
            else: 
                print("See you next time")
        
many_tries() 