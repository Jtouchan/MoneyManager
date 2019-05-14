
import openpyxl as xl
import string
from tkinter import *
import tkinter as ttk
ID= { }
letters = list(string.ascii_lowercase)
## setting up the file to read and write catagories

class BackEnd :
    def DictCreater (slef,Read_Full_pth):

        Read_workbook = xl.load_workbook(Read_Full_pth)
        SheetName= "Catagories"
        Read_sheet=Read_workbook.get_sheet_by_name(SheetName)

        keys   = Read_sheet['1'][:9]
        # write the keys
        for i in range (len(keys)):
            ID[ keys[i].value] = [ ]
            values = Read_sheet[letters[i]]

            for ii in range (len ( values)-1):
                ID[ keys[i].value].append (values[ii+1].value)

        return ID,Read_sheet

    def GUI (self, Read_Full_pth,NewEntry):

        Read_workbook = xl.load_workbook(Read_Full_pth)
        SheetName= "Catagories"
        Read_sheet=Read_workbook.get_sheet_by_name(SheetName)
        keys   = Read_sheet['1'][:9]
        Skip_Column = Read_sheet['L']

        root = Tk()
        root.title("New entry Detected")
        skip=0

        mainframe = Frame(root)
        mainframe.grid(column=50,row=50, sticky=(N,W,E,S) )
        mainframe.pack(pady = 0, padx = 0)


        root.geometry("280x200") #You want the size of the app to be 500x500
        root.resizable(0, 0) #Don't allow resizing in the x or y direction
        Label(mainframe, text=" ").grid(row = 2, column = 1)

        # Create a Tkinter variable
        tkvar = StringVar(root)

        # Dictionary with options
        tkvar.set(' ') # set the default option

        popupMenu = OptionMenu(mainframe, tkvar, *ID)
        popupMenu.grid(row = 4, column =1)
        Label(mainframe, text="Chose an existing catagory").grid(row = 2, column = 1)

        Label(mainframe, text="").grid(row = 5, column = 1)
        Label(mainframe, text="").grid(row = 6, column = 1)
        Label(mainframe, text="").grid(row = 7, column = 1)

        t="The new entry is " + NewEntry +". Chose the catagory of the entry \n"
        t2="If the entry is not an expense, just close the window"
        Label(mainframe, text=t+t2).grid(row = 8, column = 1)

        Button(root, text='Done', command=root.destroy).pack(side = BOTTOM)

        root.mainloop()
        Var2 = tkvar.get()


        for i in range (len (keys)):
            if (keys[i].value == Var2):
                for ii in range (len(ID [Var2])):
                    if (ID [Var2][ii] == None):
                        Read_sheet[letters[i]+str(ii+2)] = NewEntry # replace the newentry with the next "None"
                        ID[Var2][ii]=NewEntry
                        break

        if (Var2 not in ID.keys()): ## write the new catagory in the skipable section

            for i in range(len(Skip_Column)):
                if (Skip_Column[i].value == None ):
                    Skip_Column[i].value = NewEntry
                    skip =1
                    break

        Read_workbook.save(Read_Full_pth)
        return Var2 , skip


    def Identifier_cleaner (self, Transaction_Description,x,id_1,id_2):

        temp = Transaction_Description[x+1].value # the entire description
        list = []
        identifier= ''
        for i in range(len(temp.split())):
             if (any (char.isdigit() for char in temp.split()[i])):
                 continue
             if ('-' in temp.split()[i]):
                 break
             if ('#' in temp.split()[i]):
                 break
             list.append(i) ## this is the indecies of what you want to display ( i think)

        for i in range(len(list)):
            identifier = identifier +" "+ temp.split()[list[i]]

        return identifier
