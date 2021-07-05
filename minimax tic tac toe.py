import sys
import math


def findTotalSum(player):
    arr_size = len(player)
    for i in range(0, arr_size-2):
        for j in range(i + 1, arr_size-1):
            for k in range(j + 1, arr_size):
                if player[i] + player[j] + player[k] == 14:
                    return True

    # If we reach here, then no
    # triplet was found
    return False


def evaluation(board, player, opponent):
    if findTotalSum(player) == True:
        return "Player"
    if findTotalSum(opponent) == True:
        return "Opponent"
    return None


def minimax(board, player, opponent, depth, isMax):
    allSteps = 0
    steps = 0

    tmpBoard = board[:]
    result = evaluation(board, player, opponent)
    if result == "Player":
        return 10-depth, 1
    if result == "Opponent":
        return -10+depth, 1
    if (len(board) == 0 and result == None):
        return 0, 1

    if(isMax):
        bestScore = -math.inf
        for x in board:
            player.append(x)
            tmpBoard.remove(x)

            scores, steps = minimax(
                tmpBoard, player, opponent, depth+1, False)
            bestScore = max(bestScore, scores)

            allSteps = allSteps + steps

            player.remove(x)
            tmpBoard.append(x)

        return bestScore, allSteps
    else:
        bestScore = +math.inf
        for x in board:
            opponent.append(x)
            tmpBoard.remove(x)
            scores, steps = minimax(
                tmpBoard, player, opponent, depth+1, True)
            bestScore = min(bestScore, scores)
            allSteps = allSteps + steps
            opponent.remove(x)
            tmpBoard.append(x)

        return bestScore, allSteps


def findBestMove(board, player, opponent):
    allSteps = 0
    tmpBoard = board[:]
    bestVal = -math.inf
    bestNum = -math.inf

    for x in board:
        player.append(x)
        tmpBoard.remove(x)

        score, steps = minimax(tmpBoard, player, opponent, 0, False)
        allSteps = allSteps + steps

        player.remove(x)
        tmpBoard.append(x)

        if(score > bestVal):
            bestNum = x
            bestVal = score

    return bestNum


totalMoves = int(sys.argv[1])

pile = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# who are u
p = []
o = []
# cards in hand
playerA = []
playerB = []


# save all the cards into hand
for i in range(totalMoves):

    # save card into playerB
    if i % 2 != 0:
        playerB.append(int(sys.argv[i+2]))

    # save card into playerA
    if i % 2 == 0:
        playerA.append(int(sys.argv[i+2]))

    # remove sent card in list
    pile.remove(int(sys.argv[i+2]))


# identify which player you are
if totalMoves % 2 == 0:
    p = playerA
    o = playerB
else:
    p = playerB
    o = playerA

# check who will win in current move
playerWin = findTotalSum(p)
oppoWin = findTotalSum(o)


# print whole str
lastNum = 0
if playerWin == False and oppoWin == False:
    lastNum = findBestMove(pile, p, o)

    print(totalMoves+1, end=" ")

    for i in range(totalMoves):
        print(sys.argv[i+2], end=" ")

    print(lastNum, end="")
