import random
import string


class puzzle8:      # stores the 8puzzle problem data

    def __init__(self):
        """
        set the initial state to be the goal state
            1 2 3
            4 5 6
            7 8 #

        later you can use 'scramble()' function to change it in a random GOOD way!-(which is solvable)
        """
        self.nums = [ [ None for j in range(3) ] for i in range(3) ]
        for i in range(8):
            self.nums[int(i/3)][i%3]=i+1
        self.nums[2][2]=0    # there is no number
        self.cur=(2,2)      # cur points to the empty slot in the 8puzzle
        print ("class initiated")

    def moveUp(self):   # move empty slot up
        (x,y)=self.cur
        if y==0:
            return 0    # move failed
        self.nums[x][y]=self.nums[x][y-1]
        self.nums[x][y-1]=0
        self.cur=(x,y-1)
        return 1    # move succeed

    def moveDown(self):   # move empty slot down
        (x,y)=self.cur
        if y==2:
            return 0    # move failed
        self.nums[x][y]=self.nums[x][y+1]
        self.nums[x][y+1]=0
        self.cur=(x,y+1)
        return 1    # move succeed

    def moveLeft(self):   # move empty slot left
        (x,y)=self.cur
        if x==0:
            return 0    # move failed
        self.nums[x][y]=self.nums[x-1][y]
        self.nums[x-1][y]=0
        self.cur=(x-1,y)
        return 1    # move succeed

    def moveRight(self):   # move empty slot Right
        (x,y)=self.cur
        if x==2:
            return 0    # move failed
        self.nums[x][y]=self.nums[x+1][y]
        self.nums[x+1][y]=0
        self.cur=(x+1,y)
        return 1    # move succeed

    def move (self,dir):        # we are moving the empty slot...
        if dir == 'u':
            return self.moveUp()
        if dir == 'd':
            return self.moveDown()
        if dir == 'l':
            return self.moveLeft()
        if dir == 'r':
            return self.moveRight()

    def scramble(self,level):
        for i in range(level):
            randomDir=random.choice('udlr')
            while not self.move(randomDir):    # to avoid invalid move orders we use a while loop
                randomDir=random.choice('udlr')     # if the last move was invalid....make another move

    def show(self):         # show the current state of the problem
        print(self.nums[0])
        print(self.nums[1])
        print(self.nums[2])

    def isSolved(self):
        for i in range(8):
            if not self.nums[int(i/3)][i%3]==i+1:
                return 0
        return 1

# just to test class methods
m=puzzle8()
m.show()
print m.isSolved()
m.scramble(30)
m.show()
print m.isSolved()

