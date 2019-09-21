'''
Created on 21 Sep 2019

@author: user
'''

class BattleShipBoard:

    def __init__(self, size):
        self.size = size;
    
    def perpareLayout(self):
#         x = 0;
        self.layout = [['O', 'O', 'O'],
                       ['O', 'O', 'O'],
                       ['O', 'O', 'O']];
#         while x < self.size:
#             self.layout.append()
            
        
    def printLayout(self):
        for i in self.layout:
            print('{}'.format(i));

board = BattleShipBoard(3);
board.perpareLayout();
board.printLayout();

print();

board.layout[0].pop();

board.printLayout();

print();

board.layout[1][0] = 'X';

board.printLayout();
