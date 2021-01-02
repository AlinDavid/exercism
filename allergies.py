class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergies_dict = {"eggs": 1,
                               "peanuts": 2,
                               "shellfish": 4,
                               "strawberries": 8,
                               "tomatoes": 16,
                               "chocolate": 32,
                               "pollen": 64,
                               "cats": 128}

    def allergic_to(self, item):
        return self.allergies_dict[item] & self.score != 0

    @property
    def lst(self):
        allergies = []

        for n, m in self.allergies_dict.items():
            if m & self.score != 0:
                allergies.append(n)

        return allergies
