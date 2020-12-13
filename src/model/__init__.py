import random
from flask_sqlalchemy import SQLAlchemy

class BridgeModel():
    UNPLAYED = 0
    WON = 1
    LOST = 2

    def __init__(self, db):

        class Game(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            player_1 = db.Column(db.String(80), nullable=False)
            player_2 = db.Column(db.String(80), nullable=False)
            player_3 = db.Column(db.String(80), nullable=False)
            player_4 = db.Column(db.String(80), nullable=False)

            hand_1_1 = db.Column(db.Integer(), nullable=False)
            hand_1_1_played = db.Column(db.Integer(), nullable=False)
            hand_1_2 = db.Column(db.Integer(), nullable=False)
            hand_1_2_played = db.Column(db.Integer(), nullable=False)
            hand_1_3 = db.Column(db.Integer(), nullable=False)
            hand_1_3_played = db.Column(db.Integer(), nullable=False)
            hand_1_4 = db.Column(db.Integer(), nullable=False)
            hand_1_4_played = db.Column(db.Integer(), nullable=False)
            hand_1_5 = db.Column(db.Integer(), nullable=False)
            hand_1_5_played = db.Column(db.Integer(), nullable=False)
            hand_1_6 = db.Column(db.Integer(), nullable=False)
            hand_1_6_played = db.Column(db.Integer(), nullable=False)
            hand_1_7 = db.Column(db.Integer(), nullable=False)
            hand_1_7_played = db.Column(db.Integer(), nullable=False)
            hand_1_8 = db.Column(db.Integer(), nullable=False)
            hand_1_8_played = db.Column(db.Integer(), nullable=False)
            hand_1_9 = db.Column(db.Integer(), nullable=False)
            hand_1_9_played = db.Column(db.Integer(), nullable=False)
            hand_1_10 = db.Column(db.Integer(), nullable=False)
            hand_1_10_played = db.Column(db.Integer(), nullable=False)
            hand_1_11 = db.Column(db.Integer(), nullable=False)
            hand_1_11_played = db.Column(db.Integer(), nullable=False)
            hand_1_12 = db.Column(db.Integer(), nullable=False)
            hand_1_12_played = db.Column(db.Integer(), nullable=False)
            hand_1_13 = db.Column(db.Integer(), nullable=False)
            hand_1_13_played = db.Column(db.Integer(), nullable=False)


            hand_2_1 = db.Column(db.Integer(), nullable=False)
            hand_2_1_played = db.Column(db.Integer(), nullable=False)
            hand_2_2 = db.Column(db.Integer(), nullable=False)
            hand_2_2_played = db.Column(db.Integer(), nullable=False)
            hand_2_3 = db.Column(db.Integer(), nullable=False)
            hand_2_3_played = db.Column(db.Integer(), nullable=False)
            hand_2_4 = db.Column(db.Integer(), nullable=False)
            hand_2_4_played = db.Column(db.Integer(), nullable=False)
            hand_2_5 = db.Column(db.Integer(), nullable=False)
            hand_2_5_played = db.Column(db.Integer(), nullable=False)
            hand_2_6 = db.Column(db.Integer(), nullable=False)
            hand_2_6_played = db.Column(db.Integer(), nullable=False)
            hand_2_7 = db.Column(db.Integer(), nullable=False)
            hand_2_7_played = db.Column(db.Integer(), nullable=False)
            hand_2_8 = db.Column(db.Integer(), nullable=False)
            hand_2_8_played = db.Column(db.Integer(), nullable=False)
            hand_2_9 = db.Column(db.Integer(), nullable=False)
            hand_2_9_played = db.Column(db.Integer(), nullable=False)
            hand_2_10 = db.Column(db.Integer(), nullable=False)
            hand_2_10_played = db.Column(db.Integer(), nullable=False)
            hand_2_11 = db.Column(db.Integer(), nullable=False)
            hand_2_11_played = db.Column(db.Integer(), nullable=False)
            hand_2_12 = db.Column(db.Integer(), nullable=False)
            hand_2_12_played = db.Column(db.Integer(), nullable=False)
            hand_2_13 = db.Column(db.Integer(), nullable=False)
            hand_2_12_played = db.Column(db.Integer(), nullable=False)


            hand_3_1 = db.Column(db.Integer(), nullable=False)
            hand_3_1_played = db.Column(db.Integer(), nullable=False)
            hand_3_2 = db.Column(db.Integer(), nullable=False)
            hand_3_2_played = db.Column(db.Integer(), nullable=False)
            hand_3_3 = db.Column(db.Integer(), nullable=False)
            hand_3_3_played = db.Column(db.Integer(), nullable=False)
            hand_3_4 = db.Column(db.Integer(), nullable=False)
            hand_3_4_played = db.Column(db.Integer(), nullable=False)
            hand_3_5 = db.Column(db.Integer(), nullable=False)
            hand_3_5_played = db.Column(db.Integer(), nullable=False)
            hand_3_6 = db.Column(db.Integer(), nullable=False)
            hand_3_6_played = db.Column(db.Integer(), nullable=False)
            hand_3_7 = db.Column(db.Integer(), nullable=False)
            hand_3_7_played = db.Column(db.Integer(), nullable=False)
            hand_3_8 = db.Column(db.Integer(), nullable=False)
            hand_3_8_played = db.Column(db.Integer(), nullable=False)
            hand_3_9 = db.Column(db.Integer(), nullable=False)
            hand_3_9_played = db.Column(db.Integer(), nullable=False)
            hand_3_10 = db.Column(db.Integer(), nullable=False)
            hand_3_10_played = db.Column(db.Integer(), nullable=False)
            hand_3_11 = db.Column(db.Integer(), nullable=False)
            hand_3_11_played = db.Column(db.Integer(), nullable=False)
            hand_3_12 = db.Column(db.Integer(), nullable=False)
            hand_3_12_played = db.Column(db.Integer(), nullable=False)
            hand_3_13 = db.Column(db.Integer(), nullable=False)
            hand_3_13_played = db.Column(db.Integer(), nullable=False)


            hand_4_1 = db.Column(db.Integer(), nullable=False)
            hand_4_1_played = db.Column(db.Integer(), nullable=False)
            hand_4_2 = db.Column(db.Integer(), nullable=False)
            hand_4_2_played = db.Column(db.Integer(), nullable=False)
            hand_4_3 = db.Column(db.Integer(), nullable=False)
            hand_4_3_played = db.Column(db.Integer(), nullable=False)
            hand_4_4 = db.Column(db.Integer(), nullable=False)
            hand_4_4_played = db.Column(db.Integer(), nullable=False)
            hand_4_5 = db.Column(db.Integer(), nullable=False)
            hand_4_5_played = db.Column(db.Integer(), nullable=False)
            hand_4_6 = db.Column(db.Integer(), nullable=False)
            hand_4_6_played = db.Column(db.Integer(), nullable=False)
            hand_4_7 = db.Column(db.Integer(), nullable=False)
            hand_4_7_played = db.Column(db.Integer(), nullable=False)
            hand_4_8 = db.Column(db.Integer(), nullable=False)
            hand_4_8_played = db.Column(db.Integer(), nullable=False)
            hand_4_9 = db.Column(db.Integer(), nullable=False)
            hand_4_9_played = db.Column(db.Integer(), nullable=False)
            hand_4_10 = db.Column(db.Integer(), nullable=False)
            hand_4_10_played = db.Column(db.Integer(), nullable=False)
            hand_4_11 = db.Column(db.Integer(), nullable=False)
            hand_4_11_played = db.Column(db.Integer(), nullable=False)
            hand_4_12 = db.Column(db.Integer(), nullable=False)
            hand_4_12_played = db.Column(db.Integer(), nullable=False)
            hand_4_13 = db.Column(db.Integer(), nullable=False)
            hand_4_13_played = db.Column(db.Integer(), nullable=False)

        self.Game = Game

    def make_game(self, players):
        game_state = players
        cards = set(range(1,53))
        for i in range(1,14):
            card = self.pick_card(cards)
            cards.discard(card)
            game_state['hand_1_' + str(i)] = card
            game_state['hand_1_' + str(i) + "_played"] = self.UNPLAYED
            card = self.pick_card(cards)
            cards.discard(card)
            game_state['hand_2_' + str(i)] = card
            game_state['hand_2_' + str(i) + "_played"] = self.UNPLAYED
            card = self.pick_card(cards)
            cards.discard(card)
            game_state['hand_3_' + str(i)] = card
            game_state['hand_3_' + str(i) + "_played"] = self.UNPLAYED
            card = self.pick_card(cards)
            cards.discard(card)
            game_state['hand_4_' + str(i)] = card
            game_state['hand_4_' + str(i) + "_played"] = self.UNPLAYED




        newGame = self.Game(**game_state)

    def pick_card(self, cards):
        val = random.choice(list(cards))
        return val

