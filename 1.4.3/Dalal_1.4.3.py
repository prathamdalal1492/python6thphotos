from __future__ import print_function
'''--- 1.4.2 --- ''' 
''' Part 1 Using Array of pixels ''' 
#4) A array is quicker and can only work with numbers, A list can work with strings 
#   and floats also. These things are similar because when you use a index you 
#   still have to use the -1 rule. 
#5)
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
#6) 
'''# Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
height = len(img)   # line 15 
width = len(img[0])     
for row in range(420, 470):
    for column in range(120,160):
        img[row][column] = [0, 255, 0] # red + green = yellow
#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.minorticks_on() 
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('green_earings.png')
print(len(img))
print(len(img[0])) 
print(img[24,49])'''
#  the image height = the number of rows of pixels = 960
#	the image width = the number of columns = 584 
#	the green intensity at (5,9) = img[5][9][1]
#the red intensity at (4,10) = 62
#	the red intensity of the 25th pixel in the 50th row = 75 

#7) 
#a - the for r in range checks the amount of columns, then line 29 checks each pixel 
#    in each row, line 30 checks if the position of the pixel, r and c are letters 
#    in the n array which is a position, has all of it's rgb values is greater than 
#    500, this means it is the sky, we then convert that pixel to the color magenta 
# Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'Nagasaki_bomb.png')
# Read the image data into an array
img = plt.imread(filename)
height = len(img)   # line 15 
width = len(img[0])     
for row in range(0, 470):
    for column in range(0,300):
        img[row][column] = [0, 0, 255,0] # red + green = yellow
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.minorticks_on() 
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('thebomb.png')
print(len(img))
print(len(img[0])) 
print(img[24,49])

'''
#8) 
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import PIL
import os.path

def make_mask(rows, columns, stripe_width):
    An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (columns + row * 3 ) / stripe_width % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [255,0, 0, 255] # pale red, alpha=0
            
            else:
                # Odd stripe
                image[row][column] = [0, 0, 255, 255] # magenta, alpha=255
    for row in range(0,30):
        for column in range(0,40):
            image[row][column] = [255,255,255,0] # red + green = yellow
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask_hello')  

# Read the image data 
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'women_sky_earing.png')
# Read the image data into an array
img = plt.imread(filename)
fig, ax = plt.subplots(1, 2)
ax[1].axis('off')
ax[0].axis('off')
ax[0].imshow(img, interpolation='none') # Override the default
# Create figure with 2 subplots
# Show the image data in the first subplot
filename = os.path.join(directory, 'mask.png')
# Read the image data into an array
img_2 = plt.imread(filename)
ax[1].imshow(img_2, interpolation='none') # shows the new image 
# Show the figure on the screen
# fig.show()
fig.savefig('women_and_mask.png')  
'''