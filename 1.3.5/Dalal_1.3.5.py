from __future__ import print_function
# 1 - 4 N/A 
# The answer is going to be int meaning integer or float meaning float 
#6 N/A 
slogan = 'My school is the best'   
#7 the slogan[-7] just starts counting from the back 
#8 The answer is slogan[17:21]
#9 
print("Our "+ slogan[3:]+" because people are nice and diverse")
#10 we just counted the charecters and found the number is 7 
#10b It is just printing certain parts of activity. It's going to print the first 
#    portion and continue printing until the index of the length - 1. All this 
#    means is every letter except the last one 
# 11 if the exact string test goo is somewhere in the string you are comparing it too 
#    then your output will result as true which in this case it does. 

#12 

def how_eligible(essay):
    ''' the purpose of this is to check if the participant has everything they need ''' 
    number=0
    if "?" in essay: 
        number=number + 1 
    if "\"" in essay:
        number=number + 1
    if "." in essay:
        number=number + 1
    if "!" in essay:
        number=number + 1
    print("The number of requirements you have are ",number,".")
    
    
        
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

## I think I finished the assignment. However in Python 2 when you do a function
## if you dont return anything, then as an output you get none. I dont think 
## there is anything you can do to fix it 


