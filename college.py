# College class for lab2.py
import numpy as np
import matplotlib.pyplot as plt

class College:
    '''class that reads csv and plots datasets (numpy arrays) with matplotlib'''
    filename = "tuition.csv" #class attributes
    startyear = 1971
    endyear = 2018
    def __init__(self):
        '''constructor for College class that reads in data from csv file and stores in numpy array''' 
        self.trendType = ['Private 4-year', '', 'Public 4-year', '', 'Public 2-year'] #for legend
        self._currentDollar = College.endyear - College.startyear + 1
        try: 
            data = np.loadtxt(College.filename, delimiter=",")
            self._nparray = np.array(data)
        except IOError:
            print("The file is invalid. Please try again. Program will end.")
            raise SystemExit

    def plotTuition(self): 
        '''plots the tuition trend with a loop'''
        for i in range(0, 6, 2):
            plt.plot(range(College.startyear, College.endyear + 1), self._nparray[0:self._currentDollar, i], ".-", label=self.trendType[i])
        plt.xticks(range(College.startyear, College.endyear + 1), rotation="vertical")
        plt.xlabel("Year")
        plt.ylabel("Tuition (dollars)")
        plt.title("Tuition Trend")
        plt.legend(loc="best")

    def plotRoomAndBoard(self): 
        '''plots the room and board trend without a loop'''
        plt.plot(range(College.startyear, College.endyear + 1), self._nparray[0:self._currentDollar, 6] - self._nparray[0:self._currentDollar, 0], '.-', label=self.trendType[0])
        plt.plot(range(College.startyear, College.endyear + 1), self._nparray[0:self._currentDollar, 8] - self._nparray[0:self._currentDollar, 2], '.-', label=self.trendType[2])
        plt.legend(loc="best")
        plt.xticks(range(College.startyear, College.endyear + 1), rotation="vertical")
        plt.title("Room and Board Trend")
        plt.xlabel("Year")
        plt.ylabel("Room and Board (dollars)")

    def retVal(f):
        '''decorator to print out the costs for 4 degree paths'''
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            print("{:18s}{:18s}{:35s}{:65s}".format('Private 4-Year', 'Public 4-Year','2-Year + 2-Year Private 4-year', '2-Year + 2-Year Public 4-year'))
            print ("{:18s}{:18s}{:35s}{:65s}".format('$' + str(result[0]), '$' + str(result[1]), '$' + str(result[2]), '$' + str(result[3])))
            return result
        return wrapper

    @retVal
    def plotFourYears(self, year):
        '''plots the costs for 4 different degree paths on a bar graph'''
        schoolPath = ['Private 4-year', 'Public 4-year', '2-Year + 2 Year at Private 4-year', '2-Year + 2 Year at Public 4-year']
        userYear = year-College.startyear

        privateFour = self._nparray[userYear-4:userYear, 0] #view
        privateTwo = self._nparray[userYear-4:userYear-2, 0] #2 years at a private 4-year

        publicFour = self._nparray[userYear-4:userYear, 2]
        publicTwo = self._nparray[userYear-4:userYear-2, 2] #2 years at a public 4-year
        
        juniorCollege = self._nparray[userYear-4:userYear-2, 4]
        
        plt.bar(schoolPath[0], sum(privateFour), label=schoolPath[0], align="center") #private 4-year
        plt.bar(schoolPath[1], sum(publicFour), label=schoolPath[1], align="center") #public 4-year
        plt.bar(schoolPath[2], sum(juniorCollege) + sum(privateTwo), label=schoolPath[2], align="center") #transfer private
        plt.bar(schoolPath[3], sum(juniorCollege) + sum(publicTwo), label=schoolPath[3], align="center") #transfer public

        plt.xticks(schoolPath, rotation=10)
        plt.xlabel("Year")
        plt.legend(loc="best")
        plt.ylabel("Price (for 4 years)")
        return (sum(privateFour), sum(publicFour), sum(juniorCollege) + sum(privateTwo), sum(juniorCollege) + sum(publicTwo))
        