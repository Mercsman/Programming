from hilo import Hilo

class Director:
    '''Creating a Director to control the game.'''

    def __init__(self):
        '''Creating game director'''
        self.is_playing = "y"
        self.total_score = 300
        self.hilo = Hilo()

    def start_game(self):
        '''Setting up the start of the game.'''

        while self.is_playing == "y":
            self.get_inputs()
            self.get_updates()
            self.get_outputs()

    def get_inputs(self):
        '''Gets guess from user if the next card will be higher or lower.'''
        self.hilo.draw()
        print(f'Your card is: {self.hilo.card_number1}')
        self.high_low = input('Higher or lower? [h/l] ')

    def get_updates(self):
        '''Update Score if right or wrong and draw next card. '''
        if self.high_low == "h":
            self.points = self.hilo.high()
        elif self.high_low == "l":
            self.points = self.hilo.low()
        self.total_score = self.total_score + self.points
        print(f"Next card was {self.hilo.card_number2}")

    def get_outputs(self):
        '''Update total score and ask if user wants to play another round.'''
        print(f"Your score is: {self.total_score}")
        if self.total_score <= 0:
            quit()
        self.is_playing = input(f"Play again? [y/n] ")
