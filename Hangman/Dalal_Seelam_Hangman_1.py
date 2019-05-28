# Features, option to choose random words, make sure there are no duplicates, restart 
# can have up to 10 guesses 
from __future__ import print_function
import random 
List_name = ["The Office","Friends","Game of Thrones","Breaking Bad","The Big Bang Theory",
            "South Park","Rick and Morty","Flash", "Supergirl", "Legends of Tommorrow",
            "Arrow", "Greys Anatomy", "Riverdale", "13 Reasons Why","Teen Wolf"] 
secret_1= random.choice(List_name)
secret= secret_1.upper()
tracker = True 
letters_guessed=[]
Times_wrong=[]
Times_wrong_count = 0 
print("This is the secret word: ",secret)
print("The theme is TV Shows")
def taking_inputs(): 
    '''variables: input_taker_1 is the variable that saves the input, input taker 
    saves the input of input_taker_1 in all caps, loops: our first loop checks 
    to see if the letter we guessed has already been guessed the guesser is silly 
    and loses a guess, the elif is activated when the user's guess is not in the 
    secret word and has not been guessed before, we append the times this has 
    been activated into a list and we use the len of this length to see how many 
    wrong guesses the user has done, if the guess is correct the letters are inputed 
    into a list, Expected output, This function is being called in the function 
    Hangman Display ''' 
    input_taker_1= raw_input("Guess one letter: ")
    input_taker=input_taker_1.upper()
    if input_taker in letters_guessed: 
        print("You already guessed that letter silly")
        Times_wrong.append('Wrong')
        Times_wrong_count = 10 - len(Times_wrong) 
        print("You have ",Times_wrong_count,"guesses left") 
    elif input_taker not in secret : 
        Times_wrong.append('Wrong')
        Times_wrong_count = 10 - len(Times_wrong) 
        print("You have ",Times_wrong_count,"guesses left")
        letters_guessed.append(input_taker)
    else:
        letters_guessed.append(input_taker)
    return   

def hangman_display(secret) :
    ''' variables: disword, it's a blank string and every letter that is guessed 
    correctly is inserted into the string, the string is then printed, char it's 
    not an official variable but it's used in the for loop, secret is the variable 
    that has the secret word, answer is the exact same variable as dis_word, we 
    just change the name of the variable so we can use it in later functions, loops: 
    we run a for loop on the list secret and we compare if a letter we guessed 
    is in the letter of secret we are currently on, if it is we add it to disword, 
    if the guess is a space we add the space, and finally if the letter is not in 
    secret we make a little -, This function also calls the previous function 
    taking_inputs ''' 
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
    
def hangman(): 
    ''' variables: Times_wrong and the Times_wrong_count both keep track of the 
    number of wrong guesses the user has made, secret is the word the computer 
    has generated for the user to guess, answer is the same as dis_word which are 
    the current words the user has guessed, tracker is a variable that turns on and 
    off at certain points in the code the variable is always on and only turns off 
    when the user wins the game, this would indicate the while loop to stop and tell 
    the user to win the game, loops: the first while loops checks to see if the user 
    has had less than 10 wrong guesses and the tracker is still true (which means 
    the user has not won the game yet), the next loop activates tracker when the 
    secret word is the same as the guessing word. The final loop checks to see if 
    the user still has enough guesses left, if the user loses he gets an option to 
    reset, at this point all the variables and lists are reset, this functions 
    calls the previous function Hangman display wich calls taking inputs. All 
    functions are called here ''' 
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
                    hangman()
            else: 
                print("See you next time")
        
hangman()
