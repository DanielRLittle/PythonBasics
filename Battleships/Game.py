'''
Created on 23 Sep 2019

@author: user
'''

from Battleships.Board import BattleShipBoard;
from Battleships.Player1 import Player1

board = BattleShipBoard(3);

danny = Player1();

board.printLayout();

listy = danny.shipPlacement();

print(listy);