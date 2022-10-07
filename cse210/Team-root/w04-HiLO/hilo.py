import random
class Hilo:
    ''' Setting up the Hilo Game'''

    def __init__(self):
        '''New constuction of hilo game'''
        self.card_number1 = 0
        self.card_number2 = 0

    def draw(self):
        '''Drawing random cards with nubmers between 1-13'''
        self.card_number1 = random.randint(1, 13)
        self.card_number2 = random.randint(1, 13)

    def high(self):
        '''This is for if the player choosed high, if they are right
        they will get 100 points and -75 if they are wrong'''
        if self.card_number2 > self.card_number1:
            return 100
        elif self.card_number2 < self.card_number1:
            return -75

    def low(self):
        '''This is if signer chooses low, if they are right
        they will get 100 points and -75 if they are wrong'''
        if self.card_number2 < self.card_number1:
            return 100
        elif self.card_number2 > self.card_number1:
            return -75

        
    

    


