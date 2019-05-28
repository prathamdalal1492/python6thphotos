from __future__ import print_function # must be first in file 
import random
''' Part 1 Nester if structures and testing ''' 
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
# 1 a) The answer resulted from line 17 
#   b 1) if the food we are looking for is in the citrus list and fruit list  
#   b 2) if there the food is in the fruits list but not the citrus list
#   b 3) if the food we are looking for is not in fruits but is in the starchy list 
#   b 4) if the food we are looking for is not a fruit in any list 
#   c) the banana is in the fruits list, therefore it will not go the else part 

def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    if food_id('apple') != 'NOT Citrus, Fruit':
        works= 'apple bug in food_id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works='potato bug in food_id()'
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
# 2 N/A 
# 3 
def f(n): 
    ''' this checks for the input type ''' 
    if int(n) == n: 
        if int(n) % 2 ==0: 
            if int(n) % 3 ==0: 
               return "The number is a multiple of 6"
            else:
                return "The number is even" 
        else: 
            return "N is odd"
    else: 
        return "N is not a number"
# 4 you could maybe put a list of numbers 1 -5 and check each one of them making 
#  sure they go in the function. You could check with the number they are suppose
#  to go into 
# 5 
def f_test(): 
    ''' this is to make sure that there is no problem in the code ''' 
    check_it= True 
    if f(1) != "N is odd":
        check_it="problem with 1"
    if f(2) != "The number is even" :
        check_it="problem with 2"
    if f(3) != "N is odd":
        check_it="problem with 3"
    if f(4) != "The number is even" :
        check_it="problem with 4"  
    if f(5) != "N is odd":
        check_it="problem with 5"
    if f(6) != "The number is a multiple of 6":
        check_it="problem with 6"
        
    if check_it == True:
        print("All good!")
        return True
    else:
        print(check_it)
        return False
        
# 6 is your mistake 
# 7 when used for a concatentaion the "+ adds strings together"
#   numeric addition basically adds integers numbers 
# 8 Line 11 tells the user the number they guessed is correct, the number they 
#   the end='!\n' explains how python should end it's print 

#8b
def guess_once():
    ''' this is a predefined function from the code, a guessing number game ''' 
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:    # This goes into the loop for the wrong answer 
        if guess > secret:
            print('Too high my number is ', secret, '.', sep='')
        if guess < secret:
            print('Too low my number is ', secret, '.', sep='')
    else: # Anything else 
        print('Right on , my number is', guess, end='!\n')
#9 create a function 
def quiz_decimal(low,high):
    ''' this is where you are given 2 numbers, and you are suppose to place 
    a number in between''' 
    print("Guess a number between",low,"and",high,"?")
    quiz=float(raw_input("My guess is "))
    if float(low) <= quiz <= float(high): 
        print("Good",low,"<",quiz,"<",high)
    if low>=quiz: 
        print("No",quiz,"is lower than",low)
    if quiz>=high: 
        print("No",quiz,"is bigger than",high)
''' Conclusion Questions ''' 
#1 if statements are statements that check for certain conditions, glass box 
#  testing is a process checking for problems in the if statement 
#2 Since the statements are if or else potentially only 1 block will be completely 
#  exectuted 
#3 A test suite checks if , if and else statements , are correct by using the 
#  the expected output. Programmers might write this first so they can use the 
#  expected output to write the function 
#4 yes you but not for all the functions you will also have to use and for some 
def divisible_by_2(n): 
    ''' this is meant to check if the number is divisible_by_2 ''' 
    if int(n) % 2 == 0: 
        print("The number is divisible by 2")
    else: 
        print("The number is not")
def divisible_by_6(n): 
    ''' this is meant to check if the number is divisible by 6''' 
    if int(n) % 3 == 0 and int(n) % 2 ==0: 
        print("The number is divisible by 6")
    else: 
        print("The number is not")
        
def f_challenge(n):
    ''' this is a nested version of checking certain numbers and what they are 
    divisible by ''' 
    if int(n) == n:
        if int(n) % 2 == 0: 
            print("The number",int(n), "is even and divisible by 2") ## EVEN declaration 
            if int(n) % 3 ==0: 
                print("The number",int(n)," is divisible by 2 and 3") # DIVISIBLE BY 2 and 3 
                print("This means the number",int(n),"can be divided by 6")
            else: 
                print("The number",int(n),"is divisible by 2 but not 3")  # Not completely divisible 
        else: 
            print("The number",int(n),"is odd") # ODD declaration 
 # This was diffucult, when you use a string, the function does not work 
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)
# I think so 3                 
        
        
    