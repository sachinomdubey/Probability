#Code by GVV Sharma
#November 19, 2019
#released under GNU GPL
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

import math
vector_1 = [3,2,6] #Direction vector of first line in problem 1
vector_2 = [1,2,2] #Direction vector of second line in problem 1
vector_3 = [1,-1,-2] #Direction vector of first line in problem 2
vector_4 = [3,-5,-4] #Direction vector of second line in problem 2

unit_vector_1 = vector_1 / np.linalg.norm(vector_1) #Calculating unit vector of vector1
unit_vector_2 = vector_2 / np.linalg.norm(vector_2) #Calculating unit vector of vector2
unit_vector_3 = vector_3 / np.linalg.norm(vector_3) #Calculating unit vector of vector3
unit_vector_4 = vector_4 / np.linalg.norm(vector_4) #Calculating unit vector of vector4
dot_product1 = np.dot(unit_vector_1, unit_vector_2) #calculating dot product of unit vector 1 and 2
dot_product2 = np.dot(unit_vector_3, unit_vector_4) #calculating dot product of unit vector 3 and 4
angle1 = np.arccos(dot_product1) * 180 / math.pi #calculating angle between of unit vector 1 and 2
angle2 = np.arccos(dot_product2) * 180 / math.pi #calculating angle between of unit vector 3 and 4
print("Problem (1) - Angle between L1 and L2 is : ", angle1)
print("Problem (2) - Angle between L1 and L2 is : ", angle2)

#creating x,y for 3D plotting for problem 1
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax = fig.add_subplot(111,projection='3d',aspect='equal')

#Points on the plane
A = np.array([5,-3,7]).reshape((3,1))
B = np.array([2,-5,1]).reshape((3,1))
C = np.array([9,-2,4]).reshape((3,1))
D = np.array([7,-6,0]).reshape((3,1))


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(C,D)


#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="Line1")
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],label="Line2")

#plotting point
ax.scatter(3.65,-3.9,4.3,'o')
ax.scatter(8.05,-3.9,2.1,'o')

ax.text(3.65,-3.9,4.3, "c1(3.65,-3.9,4.3)", color='red')
ax.text(8.05,-3.9,2.1, "c2(8.05,-3.9,2.1)", color='red')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()

	#creating x,y for 3D plotting for problem 2
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig1 = plt.figure()
ax = fig1.add_subplot(111,projection='3d')
#ax = fig1.add_subplot(111,projection='3d',aspect='equal')

#Points on the plane
A1 = np.array([43,-39,-82]).reshape((3,1))
B1 = np.array([48,-44,-92]).reshape((3,1))
C1 = np.array([26,-41,-88]).reshape((3,1))
D1 = np.array([35,-56,-100]).reshape((3,1))


#Generating all lines
x_AB1 = line_gen(A1,B1)
x_BC1 = line_gen(C1,D1)


#plotting line
plt.plot(x_AB1[0,:],x_AB1[1,:],x_AB1[2,:],label="Line1")
plt.plot(x_BC1[0,:],x_BC1[1,:],x_BC1[2,:],label="Line2")

#plotting point
ax.scatter(45.77,-41.77,-87.54,'o')
ax.scatter(29.69,-47.15,-92.92,'o')

ax.text(45.77,-41.77,-87.54, "c1(45.77,-41.77,-87.54)", color='red')
ax.text(29.69,-47.15,-92.92, "c2(29.69,-47.15,-92.92)", color='red')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()

	





