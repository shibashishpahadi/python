#generate random number like OTP
from random import*
for i in range(10): #if 10 random no required
 print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='') 

#sep='' means no space in between no and if randon 6 digit no required within (0,9) range this randint(0,9) 6 times need to be written
