'''
Created on 23 Sep 2019

@author: user
'''

class Player1:
    '''
    classdocs
    '''
    def __init__(self):
        pass;
    
    def shipPlacement (self):
        coordinates = list();
        print('Please enter the row your ship is in:');
        x = int(input());
        print('Please enter  the column your ship is in:');
        y = int(input());
        coordinates.append(x);
        coordinates.append(y);
        return coordinates;
            
        