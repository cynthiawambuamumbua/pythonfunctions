def year_of_birth(name,age):
    year_of_birth=2023-age
    print(f"Hello {name} you were born in {year_of_birth}")

marks=[34,55,78,98]
length=len(marks)
print("The length is",length)

# # function tofind the average marks
def find_average(marks):
    sum_marks=sum(marks)
    total_subjects=len(marks)
    average_marks=sum_marks/total_subjects
    return average_marks
# calculate the grade and return it
def grade(average_marks):
    if average_marks==80:
     grade ="A"
    elif average_marks ==60:
       grade="B"
    elif average_marks == 50:
       grade="C"
    else:
       grade="D"
    return grade
grade=grade(grade)
print("your average is",grade)

average_marks=[24,67,89,54,90]
average_marks=find_average(marks)
print("average_marks",average_marks)
