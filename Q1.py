import Simulation as Games

NUMBER_GAMES = 1000 # number of games within each simulation

NUMBER_FLIPS = 20 # number of coin flips within each game
HEADS_PROB = 0.5 # probability of heads

# Create simulation called myMoney
myMoney = Games.Simulation(1, NUMBER_GAMES, HEADS_PROB)
# Run each game within myMoney
myMoney.simulate(NUMBER_FLIPS)

# Calculate the Expected Value
print(myMoney.get_expected_value())