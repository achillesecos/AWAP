"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
gkasha
mdunaevs
aecos
"""
import random

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

        self.team_name = "We don't deserve a team name"

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """

        pass

    def testCase1():
        threshHoldArr = [[5,1,6,10,124,20,18,4],
                         [13,21,12,12,124,24,11,1],
                         [12,10,4,10,14,20,11,4],
                         [11,15,14,10,12,20,12,4],
                         [10,12,56,7,124,20,13,4],
                         [9,9,6,11,124,23,4,4],
                         [8,6,6,3,122,2,14,4],
                         [7,3,6,11,1,21,13,7]]

        boothArr = [[0,0,0,0,0,0,0,0],
                    [0,0,0,12,0,0,0,1],
                    [0,10,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,7,0,0,0,0],
                    [0,0,0,0,0,0,4,0],
                    [0,0,0,3,0,0,0,0],
                    [0,0,0,0,0,0,0,0]]

        #really big number
        minBooth = 1000
        x = 0
        y = 0

        for i in range(len(boothArr)):
            for j in range(len(boothArr[0])):
                if(boothArr[i][j] != 0 and boothArr[i][j] < minBooth):
                    minBooth = boothArr[i][j]
                    x = i
                    y = j

        assert(minBooth == threshHoldArr[x][y])
        return (minBooth,x,y)

    print(testCase1())






