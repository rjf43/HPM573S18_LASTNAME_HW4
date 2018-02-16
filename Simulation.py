from enum import Enum
import numpy as np

class CoinFlip(Enum):
    """ outcome of each coin flip"""
    HEADS = 1
    TAILS = 0

class Game:
    def __init__(self, id, heads_prob):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)

        self.heads_prob = heads_prob
        self._flipList = []

    def simulate(self, numberFlips):
        """ simulate a game of numberFlips coin flips """
        for i in range(numberFlips):
            toss = self._rnd.binomial(1, self.heads_prob)
            if toss == 1:
                toss = CoinFlip.HEADS # convert binary output to H
            else:
                toss = CoinFlip.TAILS
            self._flipList.append(toss) # convert binary output to T

    def get_payout(self):
        """ determine how many times desired series of coin flip arises
        and calculate payout"""
        payout = -250
        n = 0 # number of times that [Tails, Tails, Heads] occurs
        for i in range(len(self._flipList)-2):
            if self._flipList[i] == CoinFlip.TAILS and self._flipList[i+1] == CoinFlip.TAILS and self._flipList[i+2] == CoinFlip.HEADS:
                n +=1
        payout += 100*n
        return payout

class Simulation:
    def __init__(self, id, number_games, heads_prob):
        """

        :param id: cohort ID
        :param number_games: number of games, each of which consist of number of coin flips according to numberFlips
        :param heads_prob: probability of heads on coin toss
        """

        self._games = []
        self._payouts = []

        # simulate multiple games and populate lists
        for i in range(number_games):
            game = Game(id*number_games+i, heads_prob)
            self._games.append(game)

    def simulate(self, numberFlips):
        for game in self._games:
            game.simulate(numberFlips) # run each of the games included in the games list

            payout = game.get_payout() # calculate payout for each game in the list
            self._payouts.append(payout) # add payout for each game to payouts list

    def get_expected_value(self):
        return sum(self._payouts)/len(self._payouts)



