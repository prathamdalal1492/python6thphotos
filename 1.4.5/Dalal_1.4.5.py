''' 1 - 4 N/A ''' 
# 5a round_corner_one_image, round_corners_of_all_images and get_images, it 
# appears the code does not have a big output. You execute the code by running the file
# and calling each function with their arguments

#6 
# a new folder is created under 1.4.5 images with all the same images only they have 
# rounded edges 

#7 
# The function was defined to take 2 arguments, 
# Argument 1: PIl.Image.Object because that's where the folder leads too  --> Image 
# Argument 2: float because youre applying a float to that argument which returns 
# it as a float 
# Return Value: Returns a list, probably all the colors of all the pixels 
#7b 
# The color it makes is Magenta #7c 
# Object created in line 26: rounded_mask a mask used later to paste 
# Object created in line 27: drawing_layer and it's a combo of new image and 
#7d 
# I think the alpha value should be 0,
#7e 
# The circles are creates because of lines 32,36, 41, 43, 45, 47 
# Line 33: It draws the vertical rectangle 
# Line 36: It draws the horizontal rectangle 
# Line 41:Draws the top left circle 
# Line 43:Draws the top right circle 
# Line 45:Draws the bottom left circle 
# Line 47: Draws the bottom right circle 
# 7f 
# the coordinates of 0,0,0 is black 
# 7g 
# The color is black again 
''' DO THIS AGAIN ''' 
#8 
#a) It can have 0 or 1 arguments 
#b) the function will return a list of images in the folder, and a list of 
#   Pil.Image objects. The object returns 2 lists  
#8
#c) directory = os.getcwd()  -- 

# directory_list = os.listdir(directory) 
# absolute_filename = os.path.join(directory, entry)
#8d 
# Return a list containing the names of the entries in the directory given by path.
#8e 
# To make sure there is no error with the photo type, for example the difference 
# between numpy and pil. Pro's: Every image is examined througly and we know what 
# caused the error to triger, Con: It may take a while to run the code if there 
# is an excess amount of things being checked by the try and except loop 
 
#8f 
# Line 80 checks to see if the code gets an IOE error, Line 80 is executed when 
# an IOE error happens in the code. Line 81 just lets the code keep on running 
# by using the keyword pass. # These 2 lines almost ignore the error by letting 
# the error not halt the code. 

#9a 
# After every photo that is manipulated we need to save it under a new filename 
# this is what the Os does. We need the try and except feature to see if there is 
# any problem naming the file 
#9b 
# This would determine the number of images in the folder. This would help the user 
# see how many photos have been modified and are in the new list 
#9c 
#106: helps in iteration, goes up 1 for every photo in image list 
#108: Prints the number people are on (Mainly for the user)
#109: saves the new image in the nth position, which is increasing per photo 
#112: saves the image in a new list in a sepeeration 


