'''x=int(input("enter number in x:"))
y=int(input("enter number in y:"))
z=int(input("enter number in z:"))
avg=(x+y+z)/3
print("average of given number  is :",avg)



gross_income = int(input("salary:"))

number_of_dependents=int(input("dependents:"))

standard_deduction=10000

dependent_deduction=3000
tax_rate=0.2
taxable_income=gross_income-standard_deduction-(dependent_deduction*number_of_dependents)
tax=taxable_income*tax_rate
print(tax)


time=int(input("time:"))
minutes=time//60
seconds=time%60
print(minutes)
print(seconds)
'''


x=25
y='25'               
z=25.0
result=x+int(y)+int(z)
print(str(result))
