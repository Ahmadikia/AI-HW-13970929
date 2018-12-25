import random
import string


class queen8:      # stores the 8queen problem data

    def __init__(self):
        """
        sets an inital table with 8 queens inside it...which in every col & row there is one queen
        we store the table with the array of queens number of rows
        """
        self.queens = [ None for j in range(8) ]

        for i in range(8):
            self.queens[i]=i

        """ START   <randomally change cols with each other to create a random board which has a queen in every row & col>    START   """
        for j in range(10):
            for i in range(8):
                newcol=random.randint(0,7)
                     # print newplace
                temp=self.queens[i]
                self.queens[i]=self.queens[newcol]
                self.queens[newcol]=temp
        """  END    <randomally change cols with each other to create a random board which has a queen in every row & col>     END    """

        #print ("class initiated")



    def setQueen(self,queen_number,new_row_number):     # set the position of the queen_number to new_row_number ( by switching the queen col with the other queen's col that have the same row number as new_row_number)
        if self.queens[queen_number]==new_row_number:
            return 1        # no action needed
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
            for j in range(8-self.queens[i]-1):
                s= s + spaces[(self.queens[i]-1+j+i)%2]
            print s

    def is_gurding(self,queen_pose,tile_pose):      # returns true if the queen in queen_pose gurds the tile_pose in board
        (qx,qy)=queen_pose
        (tx,ty)=tile_pose
        if (qx==tx)or(qy==ty):  # straight check
            return 1
        if  ((qx-tx)==(qy-ty))or((qx+qy)==(tx+ty)): # diagonal check
            return 1


    def number_of_invalid_queens(self):     # return the number of queens which gurd at least one queen  ---  can be used to set heurisitc function return value
        result=0
        for i in range(8):
           for j in range(8):
               if not(i==j):
                   if self.is_gurding( (i,self.queens[i]) , (j,self.queens[j]) ):
                        result = result+1
                        break

        return result
    def isSolved(self):
        if self.number_of_invalid_queens()==0:
            return 1
        return 0
    def heuristic(self):
        return self.number_of_invalid_queens()


class agent:        # an agent which travers the problem tree
    def __init__(self,problem):
        self.problem = problem
        self.isDone = 0

    def goToNext(self):     # agent goes to the next best state
        if self.isDone:
            return  0       # agent is finished
        besti=-1    # next queen to move
        nestj=-1    # new place for the queen
        bestH=8   # 8 is the worst heuristic that the problem can have
        for i in range(8):
            p=self.problem      # p is an alias for self.problem...this statement wont back up self.problem in p
                            #(since there is no any copy constructor in queen8 class...we can't back it up easily...so we have to roll back changes)
            for j in range(8):
                oldrow=p.queens[i]      # saves data to roll back the sate later
                p.setQueen(i,j)
                temp=p.heuristic()
                if bestH > p.heuristic():
                    besti=i
                    bestj=j
                    bestH=temp
                p.setQueen(i,oldrow)    # roll back changes in the problem stored in this agent (since there is no any copy constructor in queen8 class...so we can't back it up easily...we have to roll back changes)
        if besti == -1:  # there is no any better state(node) in the problem tree (near the current state)
            self.isDone = 1
            return 0        # agent is finished
        if bestH < self.problem.heuristic():
            self.problem.setQueen(besti,bestj)      # move to the next best state
#            print self.problem.heuristic()
#            self.problem.showG()

            return 1            # agent has changed
        return 0    # there is no any better state(node) in the problem tree (near the current state) ... agent is finished

class solver:
    def __init__(self,agentsCount):
        self.agentCount = agentsCount
        self.agents = [ None for j in range(agentsCount) ]
        self.isDone=0
        for i in range(agentsCount):
            p=queen8()  # a random 8 queen puzzle with a wrong preset of queens is stored in p
            self.agents[i] = agent(p)     # the agent will later use hillclimbing algorithm to fix the wrong preset of queens stored in p (its exclusive problem)
    def allAgentsGoToNext(self):
        if self.isDone:
            return 0    # all agents are done....
        doneCount=0
        for a in self.agents:
            doneCount = doneCount + (a.goToNext() == 0)
        s="stoped agents: " + str(doneCount)
        print s
        self.isDone = ( doneCount == self.agentCount)
        if self.isDone:
            return 0    # all agents are done....
        return 1    # at least one agent is moving....
    def solve(self):
        while not self.isDone:
            self.allAgentsGoToNext()
        count=0
        i=-1
        for a in self.agents:
            i=i+1
            if (a.problem.isSolved()):
                count = count + 1
                s= "answer number " + str(count) + " from agent number " + str(i)
                print s
                a.problem.showG()
                print " "
        s="total agents: "+ str(self.agentCount)
        print s
        s="successful agents: "+ str(count)
        print s
        s="success rate: "+ str((count+0.0)*100/self.agentCount) +"%"
        print s


# just to test class methods

AI = solver(1000)       # creates a hillclimb based solver with 1000 agents for 8 queen problem

AI.solve()      # solves the 8 queen problem and show the successful agents result (may contain duplicated answers)
