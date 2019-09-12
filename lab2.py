# Kristi Luu ; Partner: Amir Alaj
# A program that works with college tuition data in the US. 
# The program lets the user view the tuition trend, the room and board trend, 
# and the total cost of 4 years of college for a range of years.
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # tell matplotlib about Canvas object
import matplotlib.pyplot as plt
import  tkinter.messagebox as tkmb
from college import College

class DisplayFour(tk.Toplevel):
    '''class for the Top-level window that prompts user to enter a year'''
    def __init__(self,master):
        '''Constructor for the top-level window'''
        super().__init__(master)
        self._year = 0
        self._entryText = tk.StringVar()
        
        L = tk.Label(self, text="Enter year of graduation or click and Press Enter for latest year: ")
        L.grid()
        
        self._E = tk.Entry(self, textvariable=self._entryText)   
        self._E.grid(row=0, column=1)
        self._E.bind("<Return>", self.returnYear)
        self._E.grab_set() #prevents user from clicking other menu options when this window is open
        self._E.focus_set()
    def returnYear(self, event):
        '''function that returns the year after checking if it's in the range 1975-2018 and if it's a 4-digit number'''
        userText = self._entryText.get().replace(' ', '')
        if len(userText) == 0:
            self._year = 2018 #default
        elif len(userText) != 4 or not userText.isdigit() or int(userText) < College.startyear+4 or int(userText) > College.endyear:
            tkmb.showerror("Invalid Input", "Please enter a number from 1975 to 2018 or click X", parent=self)
            self._E.delete(0, tk.END)
            self._E.wait_window(self)
        else:
            self._year = userText
            self._E.delete(0, tk.END)            
        self.destroy()
    def getYear(self):
        '''getter for the year'''
        return int(self._year)       

class DisplayTrends(tk.Toplevel): 
    '''class for top-level window to plot the graphs in tkinter'''
    def __init__(self, master): 
        '''constructor for the DisplayTrends class; it creates a College object'''
        super().__init__(master)
        self.c = College()
    def plotCollegeTrend(self):
        '''plots the tuition trend for 4-year (both public and private) and 2-year universities from 1971-2018'''
        fig = plt.figure(figsize=(7,7))
        self.c.plotTuition()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid()
        canvas.draw()
    def plotRoomBoard(self):
        '''plots the room and board trend for 4-year (both public and private) and 2-year universities from 1971-2018'''
        fig = plt.figure(figsize=(7,7))
        self.c.plotRoomAndBoard()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid()
        canvas.draw()
    def plotFourYears(self, year):
        '''plots the cost of 4 years of college for each the 4 paths'''
        fig = plt.figure(figsize=(7,7))
        self.c.plotFourYears(year)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid()
        canvas.draw()

class MainWin(tk.Tk):
    '''class for the main window of the GUI'''
    def __init__(self):
        '''constructor that creates the 3 buttons to the main window'''
        super().__init__()        
        self.title('College Pricing')
        self.resizable(False, False)
        self._tuitiontrendbutton = tk.Button(self, text="Tuition Trend", fg="blue", command = self.tuitionTrend).grid(row = 0, column = 0, padx = 20, pady = 20)
        self._roomboardbutton = tk.Button(self, text="Room and Board Trend",  fg="blue", command = self.roomBoardTrend).grid(row=0, column = 1, padx = 20, pady = 20)
        self._fouryearbutton = tk.Button(self, text="4-year Cost Trend",  fg="blue", command = self.fourYearTrend).grid(row = 0, column = 2, padx = 20, pady = 20)
    def tuitionTrend(self):
        '''function to display tuition trend plot'''
        top = DisplayTrends(self)    
        top.plotCollegeTrend()
    def roomBoardTrend(self):
        '''function to display room and board trend plot'''
        top = DisplayTrends(self)    
        top.plotRoomBoard() 
    def fourYearTrend(self):
        '''function to display the bar graph of total costs for 4 years based on the user-input graduation year'''
        d = DisplayFour(self)
        self.wait_window(d)
        top = DisplayTrends(self)
        if d.getYear() == 0:
            top.destroy()
        else:
            top.plotFourYears(d.getYear())

def main():
    app = MainWin()
    app.mainloop()
main()

'''
The most effective way to earn a 4-year degree is to attend a 2-year community 
college and transfer to a 4-year public university. This is the most 
cost-efficient because you will spending least going to a 2-year community college, 
and between a private and public university, public universities are immensely more affordable. 

Ranking of least costly to most costly: 
1. 2-year + Transfer to 4-year public for 2 years
2. Public 4-year for all 4 years
3. 2-year + Transfer to a 4-year private for 2 years
4. Private 4-year for all 4 years

==2018==
Private 4-Year    Public 4-Year     2-Year + 2-Year Private 4-year     2-Year + 2-Year Public 4-year                                    
$138040.0         $40040.0          $74360.0                           $26760.0                           
==2010==
Private 4-Year    Public 4-Year     2-Year + 2-Year Private 4-year     2-Year + 2-Year Public 4-year                                    
$114520.0         $30500.0          $61540.0                           $20250.0 
==2006==
Private 4-Year    Public 4-Year     2-Year + 2-Year Private 4-year     2-Year + 2-Year Public 4-year                                    
$104980.0         $26020.0          $56200.0                           $17070.0    
==1975==
Private 4-Year    Public 4-Year     2-Year + 2-Year Private 4-year     2-Year + 2-Year Public 4-year                                    
$45590.0          $11170.0          $25620.0                           $8230.0    

Based on the data, in the recent decade, the prices have been consistently low for 
the community college to a 4-year public university route. 
A private 4-year has always been the most expensive route and 
thus, for any future decisions, it can easily be predicted that future students
will encounter the same price range pattern. 

The reason why I chose the years is to present the recent decade (for relativity) 
and the oldest year in the data set to show that the pattern remains the same
even in old times.
'''