**MoneyManager**
===================


# Functionality:

The MoneyManager application is designed to perform the following tasks:

1. Preprocess and compile spending information from two credit card statements into one main excel file (Spending Summary.xlsx) for each month.

2. Read the compiled monthly statements line by line, and break down spending into several categories as specified by the user.

3. If the category of a certain expense is unknown, the application asks the user to choose a category. Once the user makes a selection, the application saves this selection and automatically identifies the category of the expense next time it is encountered. If the user wishes not to include a specific expense in the analysis, he/she can simply skip this step. 

##picture

4. Once the application is done parsing the monthly statements, it generates visual representations of the spending in a specified month. In addition, it compares the spending in a certain month with that in previous months. (Figures below were produced using dummy data)
##pictures
 
5. Finally, the application displays the "big picture" that summarizes the financial activity for the specified month. 
(Numbers below were produced using dummy data)
##picture


# Side Notes: 

* This application was inspired by a book titled "Your money or your life" by Vicki Robin who emphasized the importance of tracking _every penny_ spent in order to have a financially healthy life. 
 
* This application will be further modified to add the ability to read credit card statements in pdf format in addition to excel format. 

