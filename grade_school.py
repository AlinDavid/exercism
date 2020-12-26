class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade not in self.directory:
            self.students[grade] = []

        self.students[grade].append(name)
        self.students[grade].sort()

    def roster(self):
        students_list = []
        for student in sorted(self.students.keys()):
            students_list += self.students[student]

        return result

    def grade(self, grade_number):
        if grade_number not in self.students:
            return []
        return self.students[grade_number]
