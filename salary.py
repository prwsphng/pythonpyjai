def notsalary(a,b,c,d):
    total = 750 + a + b + c + d
    return total

def salary(realsalary,bonus,total):
    salary = realsalary + bonus - total
    return salary

realsala = int(input('your salary: '))
realbo = int(input('bonus: '))

kad = int(input('kad:'))
la = int(input('la: '))
tax = int(input('tax: '))
other = int(input('other: '))

tmp = notsalary(kad,la,tax,other)

print(notsalary(kad,la,tax,other), ' is other')

print(salary(realsala,realbo,tmp), ' is realtotal')

