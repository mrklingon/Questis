# Python program to print all Primes Smaller
# than or equal to N using Sieve of Eratosthenes
#https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
from adafruit_circuitplayground import cp
import time
import random
import math

blank = (0,0,0)
red = (20,0,0)
orange = (25, 10, 0)
yellow = (24,24,2)
green  = (0,20,0)
blue = (0,0,8)

def showbin(num):
    cp.pixels.fill(blue)

    if num < 0:
        c = red
        num = num * -1
    else:
        c = green
        
    if num == 0:
        return
    bits = 1 + int(math.log(num)/math.log(2))
    if num == 8:
        cp.pixels[3] = c
        return

    if num != 0:
        for i in range(bits):
            if i>9 and num >2**10:
                for m in range(9):
                        cp.pixels[m]=cp.pixels[m+1]
                cp.pixels[9] = blue
            if ((2**i)&num)>0:
                if i>9:
                    cp.pixels[9] = c
                else:
                    cp.pixels[i]= c
            if (i > 9): time.sleep(.1)
    if bits>9:
        time.sleep(.5)
    else:
        time.sleep(.25)


def showbinx(num):
    cp.pixels.fill(blank)
    for x in range(3):
        cp.pixels[x+5] = blue
        
    if num < 0:
        c = red
        num = num * -1
    else:
        c = green
        
    if num == 0:
        return
    bits = 1 + int(math.log(num)/math.log(2))

    if num != 0:
        for i in range(bits):
            if ((2**i)&num)>0:
                    cp.pixels[5+i]= c
    time.sleep(.5)
    

def showdigit(num):
    cp.pixels.fill(blue)
    for i in range(num):
        cp.pixels[i] = yellow
    time.sleep(1)

def shownum(num):
    snum = str(num)
    for i in range(len(snum)):
            showdigit(eval(snum[i]))


def pick():  # create a random color
    return (random.randrange(200), random.randrange(200), random.randrange(200))

def rndcolor():
    cp.pixels[random.randrange(10)] = pick()

enter = 1 #enter numbers
calc  = 2 #act on numbers
stack = []

if cp.switch:
    state = enter
    z = 0
else:
    state = calc
    action = 0
    cp.pixels.fill(blank)
    
while True:
    #switch between enter/calc states
    
    if state == calc and cp.switch:
        state = enter
        z = 0
    if state == enter and not cp.switch:
        state = calc
        action = 0
    val = 0
    if cp.button_a and not cp.button_b:
        val = val + 1
        time.sleep(.1)
    if cp.button_b  and not cp.button_a:
        val = val + 2
        time.sleep(.1)
    if cp.button_a and cp.button_b:
        val = 3
        
    if val == 3 and state == enter:
        print("push "+str(z)+" on stack")
        stack.insert(0,z)
        z = 0
        showbin(z)
        time.sleep(1)
        
    if cp.touch_A1 and state == calc:
        print ("stack is "+str(len(stack))+" elements")
        showbin(len(stack))
        time.sleep(1)
        showbin(0)
    if val==3 and state == calc:
        print ("stack:") 
        for x in (stack):
            print(str(x))
            showbin(x)
            time.sleep(.25)
        
        showbin(len(stack))
        time.sleep(1)
        showbin(0)
    if val > 0:
        if state == enter:
            if val == 1:
                z = z+1
            if val == 2:
                z = z-1
 
            showbin(z)
            if z == 0:
                time.sleep(.25)
        if state == calc:
            if val == 1:
                action = (action + 1)%5
                showbinx(action)
                
            if val == 2 and len(stack)>1 and action == 3:#ADD
                v1 = stack.pop(0)
                v2 = stack.pop(0)
                z = v1 + v2
                print (str(v1)+"+"+str(v2)+"="+str(z))

                stack.insert(0,z)
                showbin(z) 
                
            if val == 2 and len(stack)>1 and action == 4:#Subtract
                v1 = stack.pop(0)
                v2 = stack.pop(0)
                z = v1 - v2
                print (str(v1)+"-"+str(v2)+"="+str(z))

                stack.insert(0,z)
                showbin(z)              
                
            if val == 2 and len(stack)>1 and action == 1:#Multiply
                v1 = stack.pop(0)
                v2 = stack.pop(0)
                z = v1 * v2
                print (str(v1)+"*"+str(v2)+"="+str(z))

                stack.insert(0,z)
                showbin(z)              
            if val == 2 and len(stack)>1 and action == 2:#Divide
                v1 = stack.pop(0)
                v2 = stack.pop(0)
                z = int((v1 / v2))
                print (str(v1)+"/"+str(v2)+"="+str(z))

                stack.insert(0,z)
                showbin(z)              
