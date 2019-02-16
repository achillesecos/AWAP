"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
mdunaevs
gkasha
aecos
"""
from awap2019 import Tile, Direction, State

class Team(object):
    def __init__(self, initial_board, team_size, company_info):
        """
        The initializer is for you to precompute anything from the
        initial board and the company information! Feel free to create any
        new instance variables to help you out.

        Specific information about initial_board and company_info are
        on the wiki. team_size, although passed to you as a parameter, will
        always be 4.
        """
        self.board = initial_board
        self.team_size = team_size
        self.company_info = company_info


        self.team_name = "We Don't Deserve a Name"

    def getScope(self):
        with open(self.board) as f:
            first_line = f.readline()
        first_line = text.split(' ')
        scope = first_line[len(first_line)-1]
        return scope

    def findMinBooth(self, visible_board, mainBotPos, scopeRange):
        playerRow = mainBotPos[0]
        playerCol = mainBotPos[1]
        minBooth = 100000
        pos = (-1, -1)
        for drow in range(-scopeRange, scopeRange + 1):
            for dcol in range(-scopeRange, scopeRange + 1):
                if(self.isInBounds(drow + playerRow, dcol + playerCol, visible_board)):
                    posName = visible_board[drow + playerRow][dcol + playerCol].get_booth()
                    if(posName != None):
                        currMin = self.company_info[posName]
                        if(currMin < minBooth):
                            minBooth = currMin
                            pos = (drow + playerRow, dcol + playerCol)
        return pos


    def findSmallestTile(self, visible_board, playerPos):
        values = []
        minVal = 10000000
        playerRow = playerPos[0]
        playerCol = playerCol[1]
        maxPos = (-1, -1)
        for dirr in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            drow = dirr[0]
            dcol = dirr[1]
            amtPeople = visible_board[playerRow + drow][playerCol + dcol].num_bots
            if(amtPeople < minVal):
                minPos = (playerRow + drow, playerCol + dcol)
                minVal = amtPeople
        if(minPos == (-1, -1)):
            return (playerRow + 0, playerCol + 1)
        return minPos

    def isInBounds(self, row, col, visible_board):
        return (0 <= row < len(visible_board) and 0 <= len(visible_board[0]))

    def mainPlayerMove(self, visible_board, states)
        minBoothPos = self.findMinBooth(visible_board, states[0], self.getScope)
        if(minBoothPos == (-1, -1)):
            reuturn self.findSmallestTile(visible_board, states[0])
        return minBoothPos

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """

        mainPlayerNewPos = self.mainPlayerMove(visible_board, states[0])

        
        # Access each individuals teams player positions
        # Check 5x5 grid around
        # Use this to find best direction



class Graph:

	def __init__(self):
		#dictionary of nodes to its neighboring nodes where key is node and
		#value is array of neighboring nodes
		self.graph = {}
		self.weight = {}

	#add the "line" from a node to another node
	def addEdge(self, start, end, distance):
		#normal order
		if start not in self.graph:
			self.graph[start] = [end]
		else:
			self.graph[start].append(end)
		#Reverse order
		if end not in self.graph:
			self.graph[end] = [start]
		else:
			self.graph[end].append(start)

		self.weight[(start,end)] = distance
		self.weight[(end,start)] = distance

	#returns an array of nodes that neighbor a node
	def getNeighbors(self, node):
		return self.graph[node]


	#returns the distasnce between two nodes
	def getWeight(self, node1, node2):
		return self.weight[(node1, node2)]


def dijkstra(graph, initial, target):
	#array of different nodes to check
	que = []
	#distance from initial start to node
	distance = {}
	#the previous nodes checked
	previous = {}
	distance[initial] = 0
	#inital has no previous node
	previous[initial] = None
	que.append(initial)
	#check through all the nodes
	while len(que) != 0:
		#access first node from que
		node = que.pop(0)
		#more efficient
		if node == target:
			break
		#check neighbor nodes
		for neighbor in graph.getNeighbors(node):
			tmpDist = distance[node] + graph.getWeight(neighbor, node)
			#if tempDistance is less than previous distance, update distance
			#when checking distance of new node, also update distance
			if neighbor not in distance or tmpDist < distance[neighbor]:
				que.append(neighbor)
				distance[neighbor] = tmpDist
				previous[neighbor] = node
	return distance, previous


graph = Graph()
