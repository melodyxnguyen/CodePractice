import marimo

__generated_with = "0.9.9"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    # Rock, Paper, Scisscors Game
    return


@app.cell
def __():
    class Player: # Encapsulation 
        # init (initializer method)
        def __init__(self, name):
            # attributes
            self.name = name
            self.score = 0 # set score to zero

        def make_move(self):
            move = input(f"{self.name}, choose one of the following: rock, paper, or scissors.").lower()
            while move not in ["rock", "paper", "scissors"]:
                print("Invaild move! Accepting only rock, paper, or scissors.")
                move = input(f"{self.name}, choose one of the following: rock, paper, or scissors.").lower()
            return move

        def increment_score(self):
            self.score += 1
    return (Player,)


@app.cell
def __():
    class Game: # Abstraction
        def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2
            self.valid_moves = ["rock", "paper", "scissors"]

        def play_round(self): # Handling logic
            move1 = self.player1.make_move()
            move2 = self.player2.make_move()

            print(f"{self.player1} chose {move1}")
            print(f"{self.player2} chose {move2}")

            # check who wins
            if move1 == move2:
                print("It's a tie!")
            # All possible winning combinations
            elif (move1 == "rock" and move2 == "scissors") or \
                (move1 == "scissors" and move2 == "paper") or \
                (move1 == "paper" and move2 == "rock"):
                print(f"{self.player1.name} won the round!")
                self.player1.increment_score()
            else:
                print(f"{self.player2.name} won this round!")
                self.player2.increment_score()

        def display_winner(self): # Deciding the winner
            print("\nFinal results:")
            print(f"{self.player1.name}: {self.player1.score}")
            print(f"{self.player2.name}: {self.player2.score}")

            if self.player1.score > self.player2.score:
                print(f"{self.player1.name} has won the game!")
            elif self.player2.score > self.player1.score:
                print(f"{self.player2.name} has won the game!")
            else:
                print("It's a overall tie!")
    return (Game,)


@app.cell
def __(Game, Player):
    # Main Program
    def main():
        print("Welcome to Rock-Paper-Scissors")
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        game = Game(player1, player2)

        rounds = 3
        for i in range(rounds):
            print("\nStarting a new round...")
            game.play_round()

        game.display_winner()

    if __name__ == "__main__":
        main()
    return (main,)


if __name__ == "__main__":
    app.run()