''' Introduction ''' 
# 1 - 3 N/A 
#4 C:// Users/Student login/Desktop / nice.jpg
#5 ../Studentlogin/Desktop/nice.jpg 
#6 This would be an Absolute Filename, because it starts at C. No it 
#  does not matter since it is absolute 
#7 
'''
JDoe_JSmith_1_4_2: Read and show an image.

import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('cat_plot') 
''' 
# 7 
# The new code works, the only diffrence is we are saving the new picture 
  # because it is non GUI The coordinates are 402,277, Corrdinates for the CAT are 
  # 463, 233 

#8 
#  fig is an instance of the class of Figure 
#  ax is an instance of the class axis subplot  
#  Similarly, in line 25, the method savefig is being called on the object fig. 
#  That method is being given Women plot arguments. That method is a method of 
#  the class savefig.
#9 5 cats 
'''import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 2 subplots
fig, ax = plt.subplots(1,5) # controls how many subplots make 
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('five_cats.png') '''

# 23: the method imshow()is being called on the object ax.
# 10 
# interpolation will help predict objects that are not explicitly stated, it's almost 
# like the computer guessing the pattern and filling in the blanks 
# when interpolation = "none" then the computer is not allowed to guess anything 

 #11 Zooming In and a couple other methods 
'''import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np   
# Read the image data 
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[0].minorticks_on()
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
ax[1].minorticks_on()
ax[1].set_title("Woman")
# Show the figure on the screen
# fig.show()
fig.savefig('expirement.png')'''
# 11 b 
'''
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np   
# Read the image data 
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[0].minorticks_on() 
ax[0].set_xlim(50, 65)
ax[0].set_ylim(20, 30) 
ax[1].imshow(img, interpolation='none')
ax[1].minorticks_on() 
ax[1].set_xlim(20, 10)
ax[1].set_ylim(90, 100)
ax[2].imshow(img,interpolation = 'none')
ax[2].minorticks_on() 
ax[2].set_xlim(0, 10)
ax[2].set_ylim(65, 75)
ax[1].set_title("The  Close up")

# Show the figure on the screen
# fig.show()
fig.savefig('three_closeup.png')           
# 12 
# a intresting method I discovered is called Axes.set_autoscale_on, this automatically 
# scales the axis by 2, since it is an auto you dont need to put in the scale, 
# you dont need an argument so the default value will be 0 

#13 
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[0].minorticks_on()
ax[1].set_xlim(135, 165)
ax[1].set_ylim(420,470)
ax[1].minorticks_on()
ax[1].set_title("Woman")
# Show the figure on the screen
# fig.show()
fig.savefig('expirement.png')'''
# 11 b 

import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np   
# Read the image data 
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].minorticks_on() 
ax[1].plot(120, 40, 'ro')
ax[1].plot(140,40,'ro')
ax[1].plot(40,45,'ro')
ax[1].imshow(img, interpolation='none') # shows the new image 
 
# Show the figure on the screen
# fig.show()
fig.savefig('crazy_mice.png')  


''' 
--- NOTES --- 
variable holds information 
len(listname) - 1 gets you the highest index 
Multi dimesnional, rows by columns  ax [row][column] 
Depends on how you define your AX 
Remember everything still starts at 0 
you can have 3 dimensions rows, columns, and what's inside 
what's inside has 3 things in it, the red, green and blue 
this is how you manipulate colors ? 
len column and len row explain the height and width of picture 
Every class starts with a Capital 
Images are flipped because the corrdinates are wrong 

'''