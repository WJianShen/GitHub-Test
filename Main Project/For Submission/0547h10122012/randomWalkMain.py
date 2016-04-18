#PHYS2641 Laboratory Skills and Electronics: Introduction to Programming Main Project
'''Module for producing random walks with periodic boundary conditions and kinesis. Calculating diffusion constant for a basic random walk.'''
import numpy
import random
import matplotlib.pyplot as pyplot

STUDENT_NAME = 'Woo Jian Shen'
STUDENT_ID = 'lnbw38'

def makeRandomWalk(nSteps):
    '''Generates an array of positions of a random walker.
The random walk starts at position 0 and may take steps of 1 or -1 with equal probability.
The i-th entry of the array is the position of the walker after the i-th step.'''
    pos=numpy.zeros((nSteps+1),dtype='float')
    pos[0]=0 #initial position of 0
    for step in range(nSteps):
        pos[step+1]=pos[step]+random.choice([-1,1])
    return pos

def measureMSD(nSteps,nWalkers):
    '''Returns a calculated Diffussion Coefficient from simulation of random walkers from randomWalk() function.
Number of walkers and the number of steps these walkers take must be given as integers.
Also plots a graph of Mean-Squared-Dsiplacement(MSD) against Time. '''
    SDlist = numpy.zeros((nWalkers,nSteps+1),dtype='float')#should I try stacking method instead of filling in?
    MSD = numpy.zeros((nSteps+1),dtype='float')
    for walker in range(nWalkers):
        SD=makeRandomWalk(nSteps)
        SD=(SD-SD[0])**2#Square of Displacement
        SDlist[walker,:] = SD[:]
    MSD=numpy.mean(SDlist,axis=0)
    D=numpy.mean(MSD[1:]/numpy.arange(1,nSteps+1))/4#Gradient calculated from y/x of each point
    pyplot.figure()#Create figure
    pyplot.plot(numpy.arange(1,nSteps+1),MSD[1:],'.')#Actual data
    pyplot.plot(numpy.arange(1,nSteps+1),numpy.arange(1,nSteps+1)*4*D)#Ideal line based on calculated D                    
    pyplot.xlabel('Time')
    pyplot.ylabel('MSD')
    pyplot.show()
    return D

def randomWalkPBC(nSteps):
    '''Generates an array of positions of a random walker.
The random walk starts at position 0 and may take steps of 1 or -1 with equal probability.
However there are periodic boundary conditions such as the coordinates wrap from ...,58,59,-59,-58,..
The i-th entry of the array is the position of the walker after the i-th step'''
    pos=numpy.zeros((nSteps+1),dtype='float')
    pos[0]=0 #initial position of 0
    for step in range(nSteps):
        pos[step+1]=pos[step]+random.choice([1,-1])
        if abs(pos[step+1]) == 60:#periodic boundary conditions
              pos[step+1] = pos[step+1]/abs(pos[step+1]) - pos[step+1]
    return pos

def plotRandomWalkPBC(nSteps,nWalkers):
    '''Plots multiple random walks from the randomWalkPBC() function.'''
    pyplot.figure()#Create figure
            
    for i in range(nWalkers):#Add a plot for each walker
        pyplot.plot(numpy.arange(nSteps+1),randomWalkPBC(nSteps),alpha=0.5)#numpy.arange is just representing the time variable
                        
    pyplot.xlabel('Time')
    pyplot.ylabel('Walker position')#Position after x units of time
    pyplot.title('Position of Random Walker with Periodic Boundary Conditions')
    pyplot.show()
    
def randomWalkPBCWoodlouse(nSteps):
    '''Generates an array of positions of a Woodlice random walker. Similar to randomWalkPBC()
If t>100 and -10<=x<=10, the Woodlice takes steps of 5 or -5 with equal probability.
Otherwise, the Woodlice takes steps of 1 or -1 with equal probability.
Periodic boundary conditions are such that position wraps from ...,58,59,-59,-58,..'''
    pos=numpy.zeros((nSteps+1),dtype='float')
    pos[0]=0 #initial position of 0
    for step in range(nSteps):
        if step<=100:#Normal for t<=100
            pos[step+1]=pos[step]+random.choice([1,-1])
        else: #For t>=100 kinesis is possible('the sun rises')
            if -10<=pos[step]<=10:#('in direct sunlight')
                pos[step+1]=pos[step]+random.choice([5,-5])
            else:
                pos[step+1]=pos[step]+random.choice([1,-1])
        if abs(pos[step+1]) >= 60:#periodic boundary conditions
              pos[step+1] = (abs(pos[step+1])-59)*pos[step+1]/abs(pos[step+1]) - pos[step+1]
    return pos

def plotRandomWalkPBCWoodlice(nSteps,nWalkers):
    '''Plots multiple random walks from the randomWalkPBCWoodlouse() function.'''
    pyplot.figure()#Create figure
           
    for i in range(nWalkers):#Add a plot for each walker
        pyplot.plot(numpy.arange(nSteps+1),randomWalkPBCWoodlouse(nSteps),alpha=0.5)#Each plot is a different random walk
                        
    pyplot.xlabel('Time')
    pyplot.ylabel('Walker position')#Position after x units of time
    pyplot.title('Position of Woodlice')
    pyplot.show()
    
if __name__ == '__main__':
    s = int(raw_input('Number of steps: '))
    p = int(raw_input('Number of plots: '))
    plotRandomWalkPBCWoodlice(s,p)
