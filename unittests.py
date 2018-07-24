import unittest
import copy
import random
import time
import os
import sys
from assignment4 import konane as kb
from assignment4 import student_code as student

def runGame(board, max_moves, depth, algoG, algoS, student_xo):
  start = time.clock()
  moves_x = []
  moves_o = []

  b = kb.KonaneBoard(board)

  if student_xo == "x":
    player_x = student.player(b, 'x', depth, algoS)
    player_o = student.player(b, 'o', depth, algoG)
  else:
    player_o = student.player(b, 'o', depth, algoS)
    player_x = student.player(b, 'x', depth, algoG)

  done = False
  while not done and len(moves_o) < max_moves:
    [done, move] = player_x.takeTurn()
    moves_x.append(move)
    if not done:
      [done, move] = player_o.takeTurn()
      moves_o.append(move)

  timing = time.clock()-start

  if student_xo == 'x':
    return(moves_x, timing)
  else:
    return(moves_o, timing)


class UnitTests(unittest.TestCase):
  def test_1(self):
    boardA = [[' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' '],
              [' ', 'x', ' ', ' '],
              ['o', 'o', 'o', ' ']]
    ans1 = [None]

    game = [copy.deepcopy(boardA), ans1, 100, 5, 'First Move', 'MiniMax', 'x']
    board = game[0][:]
    gold = game[1]
    max_moves = game[2]
    depth = game[3]
    algoS = game[4]
    algoG = game[5]
    xo = game[6]

    ans = runGame(board,max_moves,depth,algoS,algoG,xo)
    self.assertEqual(ans[0], gold)
    self.assertTrue(ans[1] <= 30)

  def test_2(self):
    boardB = [['x','o','x','o'],
              ['o',' ',' ','x'],
              ['x','o','x','o'],
              ['o','x','o','x']]

    ans2 = [((3, 1), (1, 1)), ((3, 3), (3, 1)),
            ((1, 3), (3, 3)), ((0, 0), (0, 2)),
            ((2, 0), (0, 0))]
    
    game = [copy.deepcopy(boardB),ans2,100,5,'First Move','MiniMax','x']
    board = game[0][:]
    gold = game[1]
    max_moves = game[2]
    depth = game[3]
    algoS = game[4]
    algoG = game[5]
    xo = game[6]

    ans = runGame(board,max_moves,depth,algoS,algoG,xo)
    self.assertEqual(ans[0], gold)
    self.assertTrue(ans[1] <= 30)

  def test_3(self):
    boardB = [['x','o','x','o'],
              ['o',' ',' ','x'],
              ['x','o','x','o'],
              ['o','x','o','x']]

    ans3 = [((0, 1), (2, 1)), ((3, 0), (3, 2)),
            ((2, 1), (2, 3)), ((1, 0), (3, 0))]
    
    game = [copy.deepcopy(boardB),ans3,100,7,'First Move','AlphaBeta','o']
    board = game[0][:]
    gold = game[1]
    max_moves = game[2]
    depth = game[3]
    algoS = game[4]
    algoG = game[5]
    xo = game[6]

    ans = runGame(board,max_moves,depth,algoS,algoG,xo)
    self.assertEqual(ans[0], gold)
    self.assertTrue(ans[1] <= 30)

