import random
import konane
import copy

#COMMENT

# class for individual player.  student and grader players should be identical except for:
#     - implementation of getMinimaxMove() and getAlphabetaMove(), and
#     - any helper functions and/or members implemented by student
class player:
    def __init__(self, b,s,depth,algo):
        self.b = b                  # board to be played for test
        self.s = s                  # save 'x' or 'o' designation
        self.depth = depth          # maximum depth for search (in number fo plies)
        self.algo = algo            # name of algorithm for player
        self.prior_move = 'L'       # helper variable for first/last deterministic player algo

    # should not be needed for autograder, but include to help development
    def makeFirstMove(self,r,c):
        self.b.firstMove(self.s,r,c)

    # returns list of available moves for player as list of [[x_from][y_from],[x_to][y_to]] items
    def getNextMoves(self):
        return(self.b.possibleNextMoves(self.s))

    # makes move specified by move expressed as [[x_from][y_from],[x_to][y_to]]
    def makeNextMove(self,move):
        self.b.nextMove(self.s,move)

    ######
    # next few methods get the next move for each of the available algorithms

    # get the first move of the list of available moves
    def getFirstMove(self):
        moves = self.b.possibleNextMoves(self.s)
        return moves[0]

    # alternative between taking the first and last available move
    def getFirstLastMove(self):
        moves = self.b.possibleNextMoves(self.s)
        if self.prior_move == 'L':
            move = moves[0]
            self.prior_move = 'F'
        else:
            move = moves[len(moves)-1]
            self.prior_move = 'L'
        return move

    # randomly choose one of the available moves
    def getRandomMove(self):
        moves = self.b.possibleNextMoves(self.s)
        selected = random.randint(0,len(moves)-1)
        return moves[selected]

    # ask a human player for a move
    def getHumanMove(self):
        print("Possible moves:" , self.b.possibleNextMoves(self.s))
        origin = self._promptForPoint("Choose a piece to move (in the format 'row column'): ")
        destination = self._promptForPoint("Choose a destination for (%s, %s) -> " % (origin[0], origin[1]))
        if (origin, destination) in self.b.possibleNextMoves(self.s):
            return (origin, destination)
        else:
            print("Invalid move.", (origin, destination))
            return self.getHumanMove()

    # help for prompting human player
    def _promptForPoint(self, prompt):
        raw = raw_input(prompt)
        (r, c) = raw.split()
        return (int(r), int(c))

    # minimax algorithm to be completed by students
    # note: you may add parameters to this function call
    def getMinimaxMove(self):
        # to be completed by students
        return []
        
    # alphabeta algorithm to be completed by students
    # note: you may add parameters to this function call
    def getAlphaBetaMove(self):
        # to be completed by students
        return []
        
    def opposite(self,s):
        if s == 'x':
            return 'o'
        else:
            return 'x'

    def heuristic(self, board, player):
        score = len(board.possibleNextMoves(self.s)) - len(board.possibleNextMoves(self.opposite(self.s))) + \
            int(board.state[0][0]==self.s) + \
            int(board.state[0][board.size-1]==self.s) + \
            int(board.state[board.size-1][0]==self.s) + \
            int(board.state[board.size-1][board.size-1]==self.s)
        return score

    # member function called by test() which specifies move to be made for player's turn, with move
    # expressed as [[x_from][y_from],[x_to][y_to]]
    # if no moves available, return Python 'None' value
    def takeTurn(self):
        moves = self.b.possibleNextMoves(self.s)

        # return Python 'None' if no moves available
        if len(moves) == 0:
            return [True,None]

        if self.algo == 'First Move':  # select first avaliable move
            move = self.getFirstMove()

        if self.algo == 'First/Last Move':  # alternate first and last moves
            move = self.getFirstLastMove()

        if self.algo == 'Random':  # select random move Note: not determinisic, just used to exercise code
            move = self.getRandomMove()

        if self.algo == 'MiniMax':  # player must select best move based upon MiniMax algorithm
            move = self.getMinimaxMove()

        if self.algo == 'AlphaBeta':  # player must select best move based upon AlphaBeta algorithm
            move = self.getAlphaBetaMove()

        if self.algo == 'Human':
            move = self.getHumanMove()

        # makes move on board being used for evaluation
        self.makeNextMove(move)
        return [False,move]
