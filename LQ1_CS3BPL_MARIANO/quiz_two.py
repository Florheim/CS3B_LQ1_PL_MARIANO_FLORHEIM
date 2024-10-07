# USE ALL VARIABLES FROM quiz_one.py
# DATA STORAGE, STRINGS & PRINTING
# CREATE VARIABLES THAT WILL STORE THE NAMES OF THE OF OUR GROUPMATES
mem1= "Mariano, Florheim Wizard V."
mem2 = "Gazmen, Jenny B."
mem3 = "Cortez, Joshua"

#CREATE VARIABLES THAT CONATAINS THEIR AGE IN VALUE NUMBER 
mem1_Age = "22"
mem2_Age = "23"
mem3_Age = "20"

#CREATE VARIABLES THAT CONTAINS THEIR WEEKLY ALLOWANCE IN DECIMAL FORM.
mem1_allowance = float(1700)
mem2_allowance = float(500)
mem3_allowance = float(1500)

# create variables to store the lenght of the names of the members & and print them formatter as follows:
Mem1_Name_Lenght = len(mem1)
Mem2_Name_Lenght = len(mem2)
Mem3_Name_Lenght = len(mem3)

# PERFORM 4 PRINT THE FOLLOWING MATH OPERATIONS FOR ALL AGE AND ALLOWANCES
Add_Total_Group_Mem = int(mem1_Age) + int(mem1_allowance), int(mem2_Age) + int(mem2_allowance), int(mem3_Age) + int(mem3_allowance)
Subtract_Total_Group_Mem = int(mem1_Age) - int(mem1_allowance), int(mem2_Age) - int(mem2_allowance), int(mem3_Age) - int(mem3_allowance)
Multiply_Total_Group_Mem = int(mem1_Age) * int(mem1_allowance), int(mem2_Age) * int(mem2_allowance), int(mem3_Age) * int(mem3_allowance)

# PRINT THE 4 COMPUTED FOR ALL AGE AND NAME USE OF MATH OPERATIONS
print(Add_Total_Group_Mem)
print(Subtract_Total_Group_Mem)
print(Multiply_Total_Group_Mem)

# PERFORM FOR THE AGE COMPARE
Compare_Age_1_2_3 = (mem1_Age == mem2_Age), (mem2_Age == mem3_Age)
print(Compare_Age_1_2_3)

# PERFORM FOR THE NAME COMPARE
Compare_Name_1_2_3 = (Mem1_Name_Lenght == Mem2_Name_Lenght), (Mem2_Name_Lenght == Mem3_Name_Lenght)
print(Compare_Name_1_2_3)

