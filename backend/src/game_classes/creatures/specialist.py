from backend.src.game_classes.creatures.statistics import Statistics


class Specialist:
    def __init__(self, name, taughtStatistics: Statistics, startGoldCost=25, costModifier=5):
        self.name = name
        self.taughtStatistics = taughtStatistics

    def teachHero(self, heroID):
        pass  # TODO gives hero statistic and increments the cost multiplying it by cost modifier - db should store data
        # TODO about current cost of development for a hero from this specialist
