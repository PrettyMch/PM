#Declaring and assigning for inputs
mark1 = int(input("Please Enter your Test 1 mark:"))
mark2 = int(input("Please Enter your Test 2 mark:"))
mark3 = int(input("Please Enter your Test 3 mark:"))

#Calculating semester mark
semester_mark =0.0
total = 0

total = mark1 + mark2 + mark3

semester_mark = (total/3)

print(semester_mark)
#grading for semester mark
if semester_mark >= 39.5:
    print("Congradulaion, You qualify for exam")

elif semester_mark < 39.4:
    print("Unfortunately, you do not qualify for exam")

