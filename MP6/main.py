from student import Student

def makeStudent(studentInfo):
    numTests = len(studentInfo) - 3
    localStudent = Student(studentInfo[0],[studentInfo[1],studentInfo[2]])
    for i in range(numTests):
        localStudent.addTest(studentInfo[i+3])
    return localStudent
    
    
def getStudent():
    #
    # Opens the data file of student info... studentID, firstName, lastName, then
    # testScores - the number of test scores is variable, from zero up... reads
    # each line of data as a str, divides the line into the values... str, str, str,
    # int, int, int... (a variable number of int values - could be none)...
    # instantiates a new Student object, uses the Student object's instance methods
    # to add those values to the object, adds the Student object to a list of objects,
    # and returns the list of Student objects.
    #
    # There are no parameters.
    #
    # Returns a list of objects from the Student class
    #
    roster = []
    with open('1300 - MP6 Data.txt') as file:
        lines = file.readlines()
        print(lines)
        for i in range(len(lines)):
            roster.append(makeStudent(lines[i].split()))
    return roster


def printStudents(roster):

    for i in range(len(roster)):
       print(roster[i])
       
printStudents(getStudent())