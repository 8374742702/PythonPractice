#type conversion

salary = 20000.50
isCredited = bool(1)

print("The datatype of credit is :",type(isCredited))
strCredited = str(isCredited)
print("the datatype of strCredited is : ",type(strCredited))
print("is salary credited :",strCredited[2],"   check :",str(salary))
oldSalary = str(salary)
print("The Old salary is : ",oldSalary)
newSalary = oldSalary + "1000"
print("The new Salary is : ",newSalary)

cmplxNumber = 0.0j
print("The Data type of cmplxNumber is :",type(cmplxNumber))
icmplxNumber = bool(str(cmplxNumber))
print("The Data type of icmplxNumber is :",(icmplxNumber))