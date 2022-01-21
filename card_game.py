from mimetypes import common_types
from time import sleep
from card import Card
from game_common import Game_Common

class Card_Game():
    
    def __init__(self):
        self.common_data = Game_Common()
        self.name = input(str("What is your username/display name? "))
        print(f"Welcome to {self.common_data.game_name}, {self.name}!")

    def start_game(self):
        self.card1 = self.draw_card()
        if self.ask_question("Would you like to play game (Y/N)? "):
            print("Great! Let's get started!")
            sleep(0.5)
            print("To play this game, you start with 300 point. \nA card will be picked. You will guess if the current card is higher or lower than the next one.\nYou earn 100 points if you guess right and loose 75 if you guess wrong.\n")
            sleep(0.5)
            print("Now... Shall we begin?")
            self.run_game()
        else:
            print("Come again soon! :)")
            sleep(1)
            exit(0)

    def run_game(self):
        question = self.ask_question("Would you like to play game (Y/N)? ")      
        self.new_card = None
        while question != False:
            self.common_data.current_turn += 1
            if self.common_data.current_turn == 1:
                self.prev_card = self.card1
            else:
                self.prev_card = self.draw_card()
                print(f"The current card is: {self.card1}")
                guess = input(str("Is the next card higher or lower than the previous card [h/l]? "))
                if guess in ["H".upper(), "HIGHER".upper()]:
                    self.new_card = self.draw_card()
                    if self.card1 > self.new_card:
                        score = self.get_and_update_score(True)
                        print(self.common_data.get_encouragement())
                        print(f"The card number is : {self.new_card}.")
                    print(f"Your score is : {score}.")
                if guess in ["L".upper(), "LOWER".upper()]:    
                    self.new_card = self.draw_card()
                    if self.card1 < self.new_card:
                        score = self.get_and_update_score(True)
                        print(self.common_data.get_encouragement())
                        print(f"The card number is : {self.new_card}.")
                    print(f"Your score is : {score}.")
                else:
                    score = self.get_and_update_score(False)
                    print(self.common_data.get_wrong_choice())
                    print(f"The card number is : {str(self.new_card)}.")
                    print(f"Your score is : {score}.")
                self.common_data.current_turn += 1
                question = self.ask_question("Would you like to play game (Y/N)? ") 
            self.common_data.current_turn += 1

    def draw_card(self):
        card = Card()
        return card.card_num

    def get_and_update_score(self, correct):
        if correct:
            self.common_data.player_score += 100
            return self.common_data.player_score
        else:
            self.common_data.player_score = self.common_data.player_score - 75
            return self.common_data.player_score

    def ask_question(self, question):
        query = input(str(question))
        return query in ["Y".upper(), "YES".upper(), "CONFIRM".upper()]


if __name__ == "__main__":
    game = Card_Game()
    game.start_game()