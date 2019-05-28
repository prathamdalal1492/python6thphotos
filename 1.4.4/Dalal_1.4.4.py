from __future__ import print_function 
# MATPLOTLIB - it is required for setting the axis as well as plotting all the 
# images, displays the image as a plot 
# np - keeps track of the array postion, rows, columns 
# PIL uses commands to change the format of image ALL THE PIXELS OF AN IMAGE 

# 14 

'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_eye')

#15 
'''Practice using this vocabulary by describing line 19: Line 19 calls the 
function subplots from the plt library. The function is being called with
2 argument(s): 1,2. The function returns 2 object(s), which is/are 
being assigned to fig and ax . ''' 
#15 b 
''' 
Line 20 calls __imshow()_ on ___ax[0]____
Line 23 calls __imshow() on ax[1]
Line 24 calls _set_xticks() on ax[1]
Line 25 calls _set_xlim() on ax[1]
Line 26 calls _set_ylim() on _ax[1]
Line 27 calls _save_fig on fig_
''' 

#15 c 
# (1162, 966) 

# 16 

# TOP LEFT CORNER 710 940 
# TOP RIGHT CORNER 800 , 940 
# BOTTOM RIGHT CORNER 800, 1016 
# BOTTOM LEFT CORNER 710, 1016 
# Width 90 
# Height: 76 

# 17
#a Line 30 uses the join() method from the os.path module. It is 
#being passed 2 arguments. The value it returns is being assigned to 
#the variable earth_file.
#b In line 31 the open() function of the PIL.Image module returns a new PIL.
#Image object, which is being assigned to the variable earth_img.
#c The first () represents the calling of the function. the () inside the first 
# represents the tuple input 
#d 89 represents how long the width of the box is, 87 represents the height of 
#  the box 
#e '''Delete After Sharing''' 
'''Line __ calls the function _________ from the _______ library with __ 
argument(s): ____________. 
The function returns ____ object(s), which is/are being assigned to _____________.

Line __ calls the method _________ on the object _______ with __ argument(s): ____________. '''

# Line 33 calls the method subplots on the plt object with 2 arguments 
# Line 34 calls the im method on the plt object with 1 argument 
# Line 35 calls the imshow method on the plt object with 1 argument 
# Line 36 calls the savefig method on the plt object with 1 argument 
#f The resize argument has an option to use a filter. The defualt value is nearest 
#  the filter argument helps in downsampling, it changes the interpolation 
#g The size attribute in PIL represents the coordinates of how zoomed in the picture 
#  is 
#  If you look on the left and bottom you can see the pixel count. The picture on 
#  the right has a fewer amount of pixels 

#18 
'''axes3[1].imshow(student_img, interpolation='none') # sets the image as a object
axes3[1].set_xlim(500, 1500) # zooms in between these coordinates on the x axis 
axes3[1].set_ylim(1130, 850) # zooms on these coordinates on the y axis 
'''
#19 

student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3. savefig('earth_eye')

# student_img = 16,500,000 
# earth_small = 7,200 
#b) 
earth_small.save('smallEarth.png')
#c 
# student_img = 206,000 
# small_earth = 18,300 

#d step a I got 16500 kb which is bery different from 206 KB 
#  however the second image has a bigger download than the first with 18.3 kb vs 7kb 
# e if color is used as the first part of the argument the next argument you need 
#   is a box, this sets the area of where colors should be changed, if there is none 
#   the program changes every pixel 
#f according to the documentation the second pictures mode changes to the the first 
#  pictures mode 
#g the first argument is the new image you are pasting, the second argument is the 
#  the top corner of the box, and the third argument is the mask 
#20 
student_img.paste(earth_small, (700, 900), mask=earth_small) 
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3. savefig('earth_as_eye')
