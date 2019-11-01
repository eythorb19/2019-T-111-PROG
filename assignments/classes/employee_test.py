from employee import HourlyEmployee, SalariedEmployee, Manager

def print_salaries(staff):
    for employee in staff:
        name = employee.get_name()
        hours = int(input("Hours worked by " + name + ": "))
        pay = employee.weekly_pay(hours)
        print("{}: {:.2f}".format(name, pay))

# The main program starts here
staff = []
staff.append(HourlyEmployee("Harry Morgan", 35.0))  # 30.0 is the hourly wage
staff.append(SalariedEmployee("Sally Lin", 78000.0)) # 52000 is the annual salary
staff.append(Manager("Mary Smith", 91000.0, 60.0))  # 104000 is the annual salary, 50.0 is the weekly bonus
print_salaries(staff)
