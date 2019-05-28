from __future__ import print_function
import random

## 1) Collections, they can be things like card collections, collections can also 
## be things like trashcans 
## 2 - 3 
''' Tuples ''' 
#4 ) A tuple is (3,7,556)
#5 ) Some of my teachers like MLA format while others like APA format,
#  b) he is not here right now using cammel case and the underscore rule 
#6 ) The answer you get is the letter b, it is at position 2 in the tuple 
#  b) I predict everything will be printed because 0 : 2 is everything in the tuple
## Correction it only prints a and b, It's probably because position 2 does not get printed 
#7 I think answer is going to be true because a is subbed into the tuple and a 
#  is defined as 10. The problem is checking if that value = 10 which it does 
#  ( I also ran it)
#7 b) the answer will output 10, since b[1] is 10 in the tuple 
''' Lists ''' 
# 8) I think every thing except the first element will be printed from the list 
# 9) I guess the result will be false, when you save values[2] as a string you can't
# use a comparator because when you are comparing you are comparing in the form of 
# an integer not a string 
# 10) I think the output will be the original values list is printed plus the 
# additions of 4,5 
# b) I think the result of 10 b will be the samething only instead of using a plus 
#  sign we used a method 
# 11) It does not work because the computer does not know what to add the five to do
# 12) The output will be 18, it only looks different because not having an equal sign 
''' Lists and random module ''' 
# 13) N/A 
#14) 
def roll_two_dice():
    first_dice = random.randint(1,6)
    second_dice= random.randint(1,6)   
    print(first_dice + second_dice)       
roll_two_dice()
''' Conclusion Questions ''' 
# 1) a is a string and there are no spaces, b is a tuple and it's values can't 
# be changed after it's definition. c is a list where it's values can be altered 
# at any time 
# 2)There are variety of variable types for the different circumstances that 
# require them, everything can't be represented in numbers because the world is 
# not all math, english exists in the world so it all has to exist in the code 
# 3)
# 1.3.2 = we learned how to define functions, use parameters and arguments 
# 1.3.3 = we learned how if and else statements work inside functions 
# 1.3.4 = we learned about how nested loops work (if inside a if)
# 1.3.5 = we learned how to slice strings, and add strings together 
# 1.3.6 = how the random operator/function works and how to import it 