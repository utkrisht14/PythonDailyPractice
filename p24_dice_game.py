import random

class Die:
    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value


    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value



class Player:
    def __init__(self, die: Die, is_computer:bool = False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 3


    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


class DiceGame:
    def __init__(self, player: Player, computer: Player):
        self.player = player
        self.computer = computer

    def play(self):
        print("Starting the game...")
        while True:
            self.play_round()
            game_over = self._check_game_over()
            if game_over:
                break


    def play_round(self):
        # Welcome the player
        self._print_welcome()

        # Roll the player and computer dice
        player_value = self.player.roll_die()
        computer_value = self.computer.roll_die()

        # Show the value of the dice
        self._show_dice(player_value, computer_value)

        # Check round winner
        self._check_round_winner(player_value, computer_value)

        # Display the counters
        self._show_counters()

    @staticmethod
    def _print_welcome():
        print("Welcome to the Dice Game!")
        print("Roll the dice to determine the winner!")
        print("Press Enter to roll the dice.")
        input()


    @staticmethod
    def _show_dice(player_value, computer_value):
        print(f"Player's value on the dice is: {player_value}")
        print(f"Computer's value on the dice is: {computer_value}")


    def _check_round_winner(self, player_value, computer_value):
        if player_value > computer_value:
            print("Player wins this round!")
            self.player.decrement_counter()
        elif computer_value > player_value:
            print("Computer wins this round!")
            self.computer.decrement_counter()
        else:
            print("It's a tie!")


    def _show_counters(self):
        print(f"\n Your counter: {self.player.counter}")
        print(f"\n Computer counter is: {self.computer.counter}")


    def _check_game_over(self):
        if self.player.counter == 0:
            print("Player wins the game!")
            return True
        elif self.computer.counter == 0:
            print("Computer wins the game!")
            return True
        else:
            return False

player_die = Die()
computer_die = Die()


my_player = Player(player_die, is_computer=False)
computer_gamer = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_gamer)
game.play()















