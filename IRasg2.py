#IR-Assignment-2
#2019-BCS-19

import numpy as np
import math as m
  
def Rx(ang):              #for rotation along x axis 
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, m.cos(ang),-m.sin(ang)],
                   [ 0, m.sin(ang), m.cos(ang)]])
  
def Ry(ang):              #for rotation along y axis
  return np.matrix([[ m.cos(ang), 0, m.sin(ang)],
                   [ 0           , 1, 0           ],
                   [-m.sin(ang), 0, m.cos(ang)]])
def Rz(ang):            #for rotation along Z axis
  return np.matrix([[ m.cos(ang), -m.sin(ang), 0 ],
                   [ m.sin(ang), m.cos(ang) , 0 ],
                   [ 0           , 0            , 1 ]])

Bp = np.matrix([2,3,0])
Ap = Rx(30) * Ry(30) * Ry(30) * np.transpose(Bp)
print(np.round(Ap, 3))
