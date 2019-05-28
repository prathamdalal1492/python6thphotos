def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip# Doc
# 17a 
def hyp(leg1,leg2):
    ''' this is the function that calculates hypotonuse''' 
    answer_2 = leg1**2 + leg2**2 
    answer= answer_2** 0.5 
    return answer       
# 17b 
def meanie(a,b,c): 
    ''' this is meant to find the mean of 3 numbers  ''' 
    answer_3= a + b + c 
    answer_4= answer_3/3.0 
    return answer_4 
    # 17c 
def perimeter(base,height): 
    ''' this function is meant to take geometry teacher's jobs ''' 
    answer_7=base + base +  height + height 
    return answer_7
# 1)I would love to have making food completely automated. I could ask to make 
#something and the food would be made for me quickly
# 2) We learned about ints and floats. We did not learn as much 
# 3) In the command line after you type the command line it, the code is hard 
#to edit. In the code editor you can copy and paste elements multiple lines 
# 4) The benefit of a function is that you can reuse code with differing 
# variables. You can also reuse code without copying and pasting and not 
# clogging up the code editor. 
#5) We probably did this because Mr. Brown wants to make sure the code works quicly. 

#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print meanie(3,4,7)
print perimeter(3,4)
    