import random
import string


class queen8:      # stores the 8puzzle problem data

    def __init__(self):
        """
        sets an inital table with 8 queens inside it...which in every col & row there is one queen
        we store the table with the array of queens number of rows
        """
        self.queens = [ None for j in range(8) ]

        for i in range(8):
            self.queens[i]=i

        """ START   <randomally change cols with each other to create a random board which has a queen in every row & col>    START   """
        for i in range(8):
            newcol=random.randint(0,7)
                 # print newplace
            temp=self.queens[i]
            self.queens[i]=self.queens[newcol]
            self.queens[newcol]=temp
        """  END    <randomally change cols with each other to create a random board which has a queen in every row & col>     END    """

        print ("class initiated")



    def setQueen(self,queen_number,new_row_number):     # set the position of the queen_number to new_row_number ( by switching the queen col with the other queen's col that have the same row number as new_row_number)
        other_queen_number=-1;
        for i in range(8):  # find the other queen number
            if(self.queens[i]==new_row_number):
                other_queen_number=i;
        if other_queen_number==-1:
            return 0        # invalid row number!
        self.queens[other_queen_number]=self.queens[queen_number]
        self.queens[queen_number]=new_row_number
        return 1            # successful operation


    def show(self):         # show the current state of the problem
        print(self.queens)
    def showG(self):        # show the current state of the problem (graphical)
        for i in range(8):
            s="";
            spaces=["[ ]","{ }"]        # stands for black & white tiles
            for j in range(self.queens[i]):
                s= s + spaces[(j+i)%2]
            if ((self.queens[i]+i)%2):
                s=s+"{#}"
            else:
                s=s+"[#]"
            for j in range(8-self.queens[i]):
                s= s + spaces[(self.queens[i]-1+j+i)%2]
            print s

    def is_gurding(self,queen_pose,tile_pose):      # returns true if the queen in queen_pose gurds the tile_pose in board
        (qx,qy)=queen_pose
        (tx,ty)=tile_pose
        if (qx==tx)or(qy==ty):  # straight check
            return 1
        if  ((qx-tx)==(qy-ty))or((qx+qy)==(tx+ty)): # diagonal check
            return 1


    def number_of_invalid_queens(self):     # return the number of queens which gurd at least one queen
        result=0
        for i in range(8):
           for i in range(8):
               if not(i==j):
                   if self.is_gurding( (i,self.queens[i]) , (j,self.queens[j]) ):
                       result = result+1
        return result
    def isSolved(self):
        for i in range(8):
            if not self.nums[int(i/3)][i%3]==i+1:
                return 0
        return 1

# just to test class methods
"""
m=puzzle8()
m.show()
print m.isSolved()
m.scramble(30)
m.show()
"""
m=queen8()
m.showG()
# print m.isSolved()

