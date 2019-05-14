import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import tkinter as ttk
from tkinter import *
import string
from PreAnalysis import PreAnalysis
letters = list(string.ascii_uppercase)


class Analysis :
    PreAnalysis=PreAnalysis()

    def plotting (self, ID_values_summed,month , Write_workbook):

        [Savings, Rent, Net_Income] = PreAnalysis.Fixed_Values (ID_values_summed,Write_workbook, month)

        Monthly_Expenses,months_names = PreAnalysis.Previous_Expenses(Write_workbook)

        Catagories , Expenses = PreAnalysis.RemoveZero (ID_values_summed)


        ###################
        ## Plotting
        ###################
        y_pos = np.arange(len(Catagories))

        # Plot 1 -- bar chart
        f1 = plt.figure(1,figsize=(13,6))
        plt.bar(y_pos, Expenses, align='center', alpha=1.0) # alpha is for transperancy
        plt.xticks(y_pos, Catagories)

        plt.yticks(np.arange(0, max(Expenses)+100, 50))
        plt.grid(b=True, which='major', axis='y')
        plt.ylabel('USD')
        plt.title('Money spent per catagory in '+month)

        # Plot 2 -- pie chart 1
        f2 = plt.figure(2)
        plt.pie(Expenses,  labels=Catagories,
        autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('Expenses Percentage for '+month)
        plt.axis('equal')

        # Plot 3 -- pie chart 2
        f3 = plt.figure(3)
        All_Expenses = [ sum(Expenses)  , Rent ]
        plt.pie(All_Expenses,  labels=['Everything else' , 'Rent'],
        autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('Expenses Percentage for '+month)
        plt.axis('equal')

        # Plot 4 - Line chart
        f4 = plt.figure(4)
        plt.plot(months_names, Monthly_Expenses, 'r', marker='x')
        plt.yticks(np.arange(400, max(Monthly_Expenses)+200, 100))
        plt.grid(b=True, which='major', axis='y')
        plt.ylabel('USD')
        plt.title('Historical Spendings')

        plt.show()

    def Summary (self,ID_values_summed,month,Write_workbook):

        [ Savings, Rent, Net_Income ]= PreAnalysis.Fixed_Values (ID_values_summed,Write_workbook, month)
        Monthly_Expenses,months_names = PreAnalysis.Previous_Expenses(Write_workbook)


        Expenses =  sum(ID_values_summed.values())+Rent
        avg_Spend = np.mean(Monthly_Expenses)+Rent
        avg_Saving = Net_Income - avg_Spend

        Spent_msg = "Your total Spending for "+month+" : \n "+"{:,}".format(round(Expenses,2))+" $"
        Saved_msg ="Your total Savings for "+month+" : \n "+"{:,}".format(round(Savings,2))+" $"
        pct_Saved_msg = "This month you saved " +str(round(Savings/Net_Income *100,2)) +" % from your income"

        avg_Spend_msg = "Your average monthly spending is: \n" +str("{:,}".format(round(avg_Spend,2))) +" $" #since March
        avg_Saving_msg = "Your average monthly saving is: \n" +str("{:,}".format(round(avg_Saving,2))) +" $"

        root = Tk()
        root.title("Analysis Summary")
        mainframe = Frame(root)
        mainframe.grid(column=50,row=50, sticky=(N,W,E,S) )
        mainframe.pack(pady = 0, padx = 0)
        root.geometry("550x450") #You want the size of the app to be 500x500
        root.resizable(0, 0) #Don't allow resizing in the x or y direction


        Label(mainframe, text= Spent_msg ).grid(row = 2, column = 1)
        Label(mainframe, text= " \n \n  " ).grid(row = 3, column = 1)
        Label(mainframe, text= Saved_msg ).grid(row = 4, column = 1)
        Label(mainframe, text= " \n \n  " ).grid(row = 5, column = 1)
        Label(mainframe, text= pct_Saved_msg ).grid(row = 6, column = 1)

        Label(mainframe, text= " \n \n  " ).grid(row = 7, column = 1)
        Label(mainframe, text= avg_Spend_msg ).grid(row = 8, column = 1)
        Label(mainframe, text= " \n \n  " ).grid(row = 9, column = 1)
        Label(mainframe, text= avg_Saving_msg ).grid(row = 10, column = 1)

        Label(mainframe, text= " \n \n  " ).grid(row = 11, column = 1)
        Button(root, text='Close', command=root.destroy).pack(side = BOTTOM)
        root.mainloop()
