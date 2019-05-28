
from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
## 1 -3 N/A 
#4 
''' this counts the days in september ''' 
def days():
    ''' It probably adds the days 
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')   
#5 a setup for a histrogram 
def picks():  
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('picks')
#picks() 
##6 a 
def roll_hundred_pair():
    dicerolls = []   # created an empty list 
    for roll in range(0,101):   # executing 100 times 
        dice=random.randint(2,12)  # choosing the random number 
        dicerolls.append(dice)  # number added to list 
    plt.hist(dicerolls)   # plotting the dice 
    plt.savefig('diceroll')  # saving the histrogram 
## 6B         
def dice_L(n):
    diceroll1= random.randint(0,n)
    diceroll2 = random.randint(0,n)
    print (diceroll1 + diceroll2)
    
    
roll_hundred_pair()

''' While Loops ''' 
# 7 
def validate():
    guess = '1' # initialization with a bad guess   
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
    
# Line 2 is needed because the variable needs to be defined, it would also start
# the while loop

#8 
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''the winner is a random player selected from he list, .

    '''
    winner = random.choice(players) 

    ####
    # Summarize the following section of code here
    ####   This is asking for a guess of players 
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # this is a random guess 
        print(p+', ', end='')  # this prints all the players 
    print(players[len(players)-1]) # this line is here to check the guess against the master list 

    ####
    # Summarize the following section of code here
    # Counts the times you are wrong and times you are right 
    ## If the guess is wrong the program will say guess again
    ## If you are right it will give the amount of guesses you guessed in.
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    
# guess_winner()
# 9 
def goguess(): 
    guess = 0 
    number_creation=random.randint(1,20) # creation of the number 
    for x in range(20):
        number_input=raw_input("I have a number between 1 and 20 guess ")
        # makes sure the number does not work 
        if int(number_input) > number_creation: # too high 
            print("The number is too high, guess again")
            guess +=1 
        elif int(number_input) < number_creation: # too low  
            print("The number is too low")
            guess +=1 
        elif int(number_input) == number_creation:
            guess += 1
            print("You guessed correctly in",guess,"guesses")  
            break
# goguess()
# 10 if the person is not stupid they will require 6000 gusses, if they are stupid, 
#    they would have guessed duplicates 
def matches(tickets,winners):
    matchnumber=0 
    for x in range(0,len(tickets)):
        if tickets[x] in winners: # if the number is in any part of tickets 
            matchnumber +=1 
    else:
        print("You got 2 matches",matchnumber,) 
# matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17])   

# 12 
secret = ['red','red','yellow','yellow','black']
guess = ['red','red','red','green','yellow'] 
def report(guess, secret): 
    inplace=0
    outplace=0 
    for y in range(0,len(guess)):
        if guess[y] in secret: # if the number is in the list 
            if guess[y] == secret[y]: # if the color is in the correct spot 
                inplace = inplace + 1 
                print("Correct Place")
            else:
                outplace = outplace +1 
                print("Out of Place ")
    print("The amount in the correct spot is ",inplace,)
    print("The amount in the wrong spot is ",outplace,)
        
            
            
#report(guess,secret)
''' Conclusion ''' 
#1 if you are iterating through a dictonary named x, and you print out each key 
#  x[1] , x[2],x[3] it is hard to change the name of the dictonary. If you want to 
#  change the name to something like counter you will have to indivdually change 
#  each thing, it also just takes up more room 
#2 Iternating goes through a large set of data quickly, this usally involved using 
#  a for loop 
#3 a while loop constantly runs while a condition is true, a for loop runs when 
#  interating through data 
#4 Sometimes we work together, othertimes we dont. It's hard to work with parters 
#  in general on problems, I like to try many solutions to see what is wrong with 
#  the code but sometimes I have trouble explaining my self especially when 
#  I am in "Problem solving mode". It's hard for me to explain my thoughts 
# 1.3 . 7 function test 
days() # this is the days functions 
#picks() # this is the pick function  
roll_hundred_pair() # this is the rolling  function 
dice_L(302) # choose the sides of the dice  
validate() # validate function 
guess_winner() # guessing function 
goguess() ## the function you have to guess between one and 20
list1 = ['red','red','yellow','yellow','green']
list2 = ['red','green','red','green','yellow'] 
report(list1,list2) # this is where I call the MATCH game function 
matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17])   # This is the gambling/lottery function          
