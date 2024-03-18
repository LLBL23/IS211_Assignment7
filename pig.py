import random

class Player:
    def __init__(self, name):

        self.name = name
        self.turn = True
        self.roll_score = 0

    def player_rolled(self):
        die = Die()
        rolled = die.roll()
        if rolled == 1:
            self.roll_score = 0
            self.turn = False
        else:
            self.roll_score += rolled
            return rolled




class Die:
    def __init__(self):
        self.roll = 0
    def random_roll(self):
        """
        Generate a random number 1-6.
        :return: Generated random number
        """
        self.roll = random.randint(1,6)
        return self.roll

class Game:
    """
    Tracks the players, their scores and the die.
    """

    def __init__(self, players):
        self.players = players
        self.players_scores = [0 for _ in range(players)]
        self.max_score = 100
        self.current_score = 0


        roll = Die()



        while max(self.players_scores) < self.max_score:
            for player_id in range(self.players):
                self.current_score = 0  # reset the current score to 0 after ever turn
                print(f'\nPlayer number, {player_id +1}')
                current_player = player_id +1
                print(f'Your total score is: {self.players_scores[player_id]} \n')
                while True:
                    turn = input('Would you like to roll (r) or hold (h)? ')
                    if turn != 'r':
                        break
                    value = roll.random_roll()
                    if value == 1:
                        self.current_score = 0
                        print(f'You rolled a 1. Your turn is over.')
                        print(f'Your turn total is: {self.current_score}')
                        break
                    else:
                        self.current_score += value
                        print(f'You rolled a {value}')
                        print(f'Your turn total is: {self.current_score}')
                        print(f'Your total score is: {self.players_scores[player_id]}')

                if max(self.players_scores) >= self.max_score:
                    print(f'Your total score is: {self.players_scores[player_id]}')
                    print('You won!')
                    break
                self.players_scores[player_id] += self.current_score
                print(f'Your total score is: {self.players_scores[player_id]}')
        print('You won!')






if __name__ == "__main__":
    players = 2
    Game(players)


