class Garden:
    names = {"Alice": 0, "Bob": 1, "Charlie": 2, "David": 3, "Eve": 4, "Fred": 5, "Ginny": 6, "Harriet": 7,
             "Ileana": 8, "Joseph": 9, "Kincaid": 10, "Larry": 11}
    letters = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}

    def __init__(self, diagram, students=None):
        if students is not None:
            students.sort()
            self.names = {}
            for i, name in enumerate(students):
                self.names[name] = i
        self.diagram = diagram.splitlines()

    def garden_plants(self, student):
        result = []
        for diagram_row in self.diagram:
            i = self.names[student]
            for j in range(i * 2, i * 2 + 2):
                result.append(self.letters[diagram_row[j]])
        return result


