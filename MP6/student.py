class Student:
    def __init__(self, initalStuID, initalName:list):
        self._stuID = initalStuID
        self._name = initalName
        self._testScores = []
        self._avg = 0
        
    def getID(self):
        return self._stuID
    
    def getName(self):
        return self._name
    
    def getTestScores(self):
        return self._testScores
    
    def getAvg(self):
        return self._avg
    
    def setName(self, firstName, lastName):
        self._name = [firstName, lastName]
        
    def _calcAvg(self):
        total = 0
        if len(self._testScores) == 0:
            self._avg = 0
            
        for i in range(len(self._testScores)):
            total = total + eval(self._testScores[i])
        if len(self._testScores) == 0:
            self._avg = 0.0
        else:
            self._avg = total/len(self._testScores)
    
    def addTest(self, testScore):
        self._testScores.append(testScore)
        self._calcAvg()
        
    def __str__(self):
        
        #adjust for _testScores
        if len(self._testScores) == 0:
            return f'Student:{self._stuID} {self._name[0]} {self._name[1]} \nTests Scores: \nTest Average:{self._avg}\n'
        else:
            payload =  f'Student:{self._stuID} {self._name[0]} {self._name[1]}\nTest Scores:'
            for i in range(len(self._testScores)-1):
                payload =  payload + f' {self._testScores[i]}'
            payload = payload + f'\nTest Average:{self._avg:.2f}\n'
        return payload