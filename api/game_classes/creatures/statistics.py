from random import randint


class Statistics:
    def __init__(self, strength=0, intelligence=0, dexterity=0, constitution=0, luck=0, persuasion=0, trade=0,
                 leadership=0,
                 protection=0, initiative=0):
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.constitution = constitution
        self.luck = luck

        self.protection = protection

        self.hp = constitution * 100

        self.persuasion = persuasion
        self.trade = trade
        self.leadership = leadership
        self.initiative = initiative

    def setFightStatistics(self, freeDevelopmentPoints):
        for i in range(0, freeDevelopmentPoints):
            rand_num = randint(0, 4)
            if rand_num == 0:
                self.strength += 1
            elif rand_num == 1:
                self.intelligence += 1
            elif rand_num == 2:
                self.dexterity += 1
            elif rand_num == 3:
                self.constitution += 1
            else:
                self.luck += 1

        self.protection = randint(0, 50)
        self.hp = self.constitution * 100

    def __str__(self):
        return 'strength: ' + str(self.strength) + '\n' + 'intelligence: ' + str(self.intelligence) + \
               '\n' + 'dexterity: ' + str(self.dexterity) + '\n' + 'constitution: ' + str(self.constitution) + \
               '\n' + 'luck: ' + str(self.luck) + '\n' + 'persuasion: ' + str(self.persuasion) + \
               '\n' + 'trade: ' + str(self.trade) + '\n' + 'leadership: ' + str(self.leadership) + \
               '\n' + 'protection: ' + str(self.protection) + '\n' + 'initiative: ' + str(self.initiative) + \
               '\n' + 'hp: ' + str(self.hp)

    def __add__(self, other):
        strength = self.strength + other.strength
        intelligence = self.intelligence + other.intelligence
        dexterity = self.dexterity + other.dexterity
        constitution = self.constitution + other.constitution
        luck = self.luck + other.luck

        protection = self.protection + other.protection

        persuasion = self.persuasion + other.persuasion
        trade = self.trade + other.trade
        leadership = self.leadership + other.leadership
        initiative = self.initiative + other.initiative

        return Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                          leadership,
                          protection, initiative)

    def __sub__(self, other):
        strength = self.strength - other.strength
        intelligence = self.intelligence - other.intelligence
        dexterity = self.dexterity - other.dexterity
        constitution = self.constitution - other.constitution
        luck = self.luck - other.luck

        protection = self.protection - other.protection

        persuasion = self.persuasion - other.persuasion
        trade = self.trade - other.trade
        leadership = self.leadership - other.leadership
        initiative = self.initiative - other.initiative

        return Statistics(strength, intelligence, dexterity, constitution, luck, persuasion, trade,
                          leadership,
                          protection, initiative)

