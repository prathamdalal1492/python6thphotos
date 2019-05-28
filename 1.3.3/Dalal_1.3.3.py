from __future__ import print_function # use Python 3.0 printing  IGNORE THIS 
''' Procedure '''
# 1 - 5 N/A 
''' Part 1 Conditionals ''' 
#6a: I think the result will be false because of the second command 
    # I guess the answer is actually true. I think its because a is 3 and 3>3 
    #is not true. However right before it the command says not. not false is true 
#6b I think both conditions are true so the whole condition will be true     

# 7 the code is below  70 <= x and y >= 40  

# 8 N/A 
''' part 2 if and else ''' 
# 9 
def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
# 9a. Predictions: I think the 10 year old will get a too young output and the 
    #16 year old will get a good enough output 
    # I was correct, 10 < 13 is true and 16 <13 is false so the code goes to the 
    #else and 16 > 13 is true 
# 9b. 
def report_grade(percent):
    ''' checks if your grade is good or not, the parameter is the percentage point, it 
    should return a string with your number ''' 
    if percent >= 80: 
        print ('A grade of',percent,'indicates mastery. Keep up the good work ')
    else: 
        print ('A grade of',percent,'does not indicate mastery. Seek extra practice or help')
''' Part 3 The in operator ''' 
# Question 10 N/A
# Question 11 
def letter_in_word(guess,word): 
    if guess in word: 
        return True 
    else: 
        return False 
# question 12  
def hint(color, secret ): 
    if color in secret: 
        print("The color",color,"IS in secret sequence of colors.")
    else: 
        print("The color",color, "is NOT in the secret sequence of colors.")
        
''' Conclusion Questions ''' 
# QUESTION 1 
# The if statement is usually placed first, it its like the first condition 
# The elif statement is like a else, but also takes an argument. It is in the 
#middle between a if and else, That's why it's placed in the middle. 
# Else blocks are the last, they take no argument, you can still give it code 
#for what to do if other conditions are rejected. else is a reject pile for code

## QUESTION 2 
# >= Greater than or equal to, <= Less than or equal to, == checks if it is equal 
# to, There is also and, not, "and" or 
# I re - remembered how to combine boolean operators together. For example 1 + 2 == not 2 
# The result would be false 

# QUESTION 3 
# Ira: I some what agree with this person. While it is best to have 1 print 
#statement, the code will not run slower. For example if there is a print in the 
#else and code does not go in the else, the computer will not use it's memory 
#there
#Jayla: She is right. You will need to change the code in 2 places. However 
# it will not make a big difference 
#Kendra: I agree with her the most. The program will not run slower with 2 print
# statements. but it will take up some memory 


# IGNORE THIS PART 
 #1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)      
        
        
        