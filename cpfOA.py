def cpf(salary, years):
    if (salary>6800):
        salary = 6800
    contribution = salary * 0.23
    i = 0
    savings = 0
    while i < years:
        a = 0
        i+=1
        while a<13:
            savings = (savings + contribution) * (1+ 0.025/365*30)
            a+=1
    print('$'+'{:10,.2f}'.format(savings))

if __name__ == '__main__':
    salary = float(input('Salary: '))
    years = int(input('Years: '))
    cpf(salary, years)
