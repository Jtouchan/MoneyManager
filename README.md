**MoneyManager**
===================


# Functionality:

The MoneyManager application is designed to perform the following tasks:

1. Preprocess and compile spending information from two credit card statements into one main excel file (Spending Summary.xlsx) for each month.

2. Read the compiled monthly statements line by line, and break down spending into several categories as specified by the user.

3. If the category of a certain expense is unknown, the application asks the user to choose a category (see below). Once the user makes a selection, the application saves this selection and automatically identifies the category of the expense next time it is encountered. If the user wishes not to include a specific expense in the analysis, he/she can simply skip this step. 

![1](https://user-images.githubusercontent.com/34410616/71704204-e2bbc900-2da6-11ea-8d10-bb2503387878.PNG)
![2](https://user-images.githubusercontent.com/34410616/71704209-e7807d00-2da6-11ea-9610-c73fadf54603.PNG)


4. Once the application is done parsing the monthly statements, it generates visual representations of the spending in a specified month. In addition, it compares the spending in a certain month with that in previous months. (Figures below were produced using dummy data)
![31](https://user-images.githubusercontent.com/34410616/71704393-29f68980-2da8-11ea-96a2-93939b4aa864.PNG)
![32](https://user-images.githubusercontent.com/34410616/71704394-2a8f2000-2da8-11ea-81ff-fc741586a85b.PNG)
![33](https://user-images.githubusercontent.com/34410616/71704395-2a8f2000-2da8-11ea-868a-521619b94d89.PNG)


5. Finally, the application displays the "big picture" that summarizes the financial activity for the specified month. 
(Numbers below were produced using dummy data)
![4](https://user-images.githubusercontent.com/34410616/71704401-32e75b00-2da8-11ea-9787-dc07f811eebe.PNG)



# Side Notes: 

* This application was inspired by a book titled "Your money or your life" by Vicki Robin who emphasized the importance of tracking _every penny_ spent in order to have a financially healthy life. 
 
* This application will be further modified to add the ability to read credit card statements in pdf format in addition to excel format. 
