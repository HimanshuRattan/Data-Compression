#512x512 means 512 rows and colums
#we are going to map the values from 0-255 to 0-8
#8 bits to represent value from 0-255
#we will use 3 bit image which means 0-8
import numpy
from PIL import Image

im=Image.open('lena.jpg')
pixelMap=im.load()

#to see it as a matrix
#I=numpy.asanyarray(Image.open('lena.jpg'))

#create a new image of same size
#new image object of same mode and size
#but we havent assigned pixels yet.. so it will be blank
img=Image.new(im.mode,im.size)
#first arguement os type second is size

pixelNew=img.load()

'''
8 bit means it can contain values upto 2^8

we will do 2^8 -> 2^3
we will map elemnts in a range
0-31=0
32-63=1
64-95=2
96-127=3
128-159=4
160-191=5
192-223=6
224-255=7
'''
#we will loop through the old image, see where the number is lying and change value

for i in range(img.size[0]):
    for j in range(img.size[1]):
        #zero is row
        #1 os columnn
        if(pixelMap[i,j]>=0 and pixelMap[i,j]<=31):
            pixelNew[i,j]=0
        elif(pixelMap[i,j]>=32 and pixelMap[i,j]<=63):
            pixelNew[i,j]=1
        elif(pixelMap[i,j]>=64 and pixelMap[i,j]<=95):
            pixelNew[i,j]=2
        elif(pixelMap[i,j]>=96 and pixelMap[i,j]<=127):
            pixelNew[i,j]=3
        elif(pixelMap[i,j]>=128 and pixelMap[i,j]<=159):
            pixelNew[i,j]=4
        elif(pixelMap[i,j]>=160 and pixelMap[i,j]<=191):
            pixelNew[i,j]=5
        elif(pixelMap[i,j]>=192 and pixelMap[i,j]<=223):
            pixelNew[i,j]=6
        elif(pixelMap[i,j]>=224 and pixelMap[i,j]<=255):
            pixelNew[i,j]=7
            
img.save('lena_2.jpg')

#to see the matrix
J=numpy.array(Image.open('lena_2.jpg'))
