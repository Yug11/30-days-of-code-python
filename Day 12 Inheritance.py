class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        # print(len(self.scores))
        # print(type(scores))
        # print(scores)
        sum = 0
        for i in range(len(self.scores)):
            sum = sum + int(scores[i])
        a =  sum/len(self.scores)
        # print(a)
        if 90<=a<=100:
            return "O"
        if 80<=a<90:
            return "E"
        if 70<=a<80:
            return "A"
        if 55<=a<70:
            return "P"
        if 40<=a<55:
            return "D"
        if a<40:
            return "T"            

            
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())