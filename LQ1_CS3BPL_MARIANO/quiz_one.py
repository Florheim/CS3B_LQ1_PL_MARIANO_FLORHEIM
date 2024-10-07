# DATA STORAGE, STRINGS & PRINTING
# CREATE VARIABLES THAT WILL STORE THE NAMES OF THE OF OUR GROUPMATES
mem1= "Mariano, Florheim Wizard V."
mem2 = "Gazmen, Jenny B."
mem3 = "Cortez, Joshua"

#CREATE VARIABLES THAT CONTAINS THEIR AGE IN VALUE NUMBER 
mem1_Age = "22"
mem2_Age = "23"
mem3_Age = "20"

#CREATE VARIABLES THAT CONTAINS THEIR WEEKLY ALLOWANCE IN DECIMAL FORM.
mem1_allowance = float(1700)
mem2_allowance = float(500)
mem3_allowance = float(1500)

# create a variable contain the name of the group.
TeamName = "J-Query"

# PRINT ALL RESULTS IN FORMATTED AS FOLLOWS: USE CONCAT
print("Team Name: ", TeamName)
print("Member1:", mem1, "his age is", mem1_Age, "allowance per week is", mem1_allowance)
print("Member2:", mem2, "her age is", mem2_Age, "allowance per week is", mem2_allowance)
print("Member3:", mem3, "his age is", mem3_Age, "allowance per week is", mem3_allowance)

# create variables to store the lenght of the names of the members & and print them formatter as follows:
Mem1_Name_Lenght = len(mem1)
Mem2_Name_Lenght = len(mem2)
Mem3_Name_Lenght = len(mem3)

# print members length
print("Member 1 consist of",Mem1_Name_Lenght,"characters!")
print("Member 2 consist of",Mem2_Name_Lenght,"characters!")
print("Member 3 consist of",Mem3_Name_Lenght,"characters!")