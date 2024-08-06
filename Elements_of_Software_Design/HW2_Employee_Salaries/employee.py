#  File: EmployeeSalaries.py
#  Student Name: Ian Salinas



class Employee:

    def __init__(self, **kwargs):
        '''##### ADD CODE HERE #####'''

        for key, value in kwargs.items():                   # **kwargs allows us to enter in ANY amount of keyword arguements
                                                            # kwargs.items() basically helps us organize the attributes into a dictionary
            setattr(self, key, value)                       # setattr() function sets values of ANY given attribute(key) of an object (WHICH IS AMAZING)                         
                                                            # This is how you utilize this function: setattr( object , name (or key), value)
    def cal_salary(self):
        salary = getattr(self, "salary")                    # getattr() function retrieves the value of an attribute of an object utilizing object keys & values 
                                                            # resulting in the associated attribute
        return salary                                       # returns whatever value is stored in any given object with "salary" attribute

    def __str__(self):
        '''##### ADD CODE HERE #####''' 
        return f'Employee\n{getattr(self,"name")},{getattr(self,"id")},{getattr(self,"salary")}'           
        # Simply returns the attribute value from the kwargs dictionary using an object as the key and given "string" as the value 


############################################################
############################################################
############################################################
    

class Permanent_Employee(Employee):
    def __init__(self, **kwargs):
        '''##### ADD CODE HERE #####'''
        for key, value in kwargs.items():                           # Nothing changes here from my Employee Class
            setattr(self, key, value)

    def cal_salary(self):
        base_salary = getattr(self, "salary")                       # returns whatever value is stored in any given object with "salary" attribute
        benefits = getattr(self, "benefits", [])                    # I kept getting AttributeErrors and found that this extra parameter acts as a safety precaution to mitigate these errors
                                                                    # returns whatever value is stored in any given object with "benefits" attribute

        if 'health_insurance' in benefits and 'retirement' in benefits:                 # Checks if strings "health_insurance" and "retirement" are in the benefits variable list
            return base_salary * 0.7
        elif 'retirement' in benefits:                                                  # Checks if string "retirement" is in the benefits variable list
            return base_salary * 0.8
        elif 'health_insurance' in benefits:                                            # Checks if string "health_insurance" is in the benefits variable list
            return base_salary * 0.9
        else:
            return base_salary

    def __str__(self):
        '''##### ADD CODE HERE #####'''
        return f'Permanent_Employee\n{getattr(self,"name")},{getattr(self,"id")},{getattr(self,"salary")},{getattr(self,"benefits")}'
        # Added a new getattr() for "benefits" as Permanent Employees get to choose this as an option


############################################################
############################################################
############################################################


class Manager(Employee):
    def __init__(self, **kwargs):
        '''##### ADD CODE HERE #####'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def cal_salary(self):
        base_salary = getattr(self, "salary")
        bonus = getattr(self, "bonus")

        return base_salary + bonus

    def __str__(self):
        pass
        '''##### ADD CODE HERE #####'''
        return f'Manager\n{getattr(self,"name")},{getattr(self,"id")},{getattr(self,"salary")},{getattr(self,"bonus")}'
        # Added a new getattr() for "bonus" as Managers get a bonus 


############################################################
############################################################
############################################################


class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        '''##### ADD CODE HERE #####'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def cal_salary(self):
        base_salary = getattr(self, "salary")
        hours = getattr(self, "hours")
        
        return base_salary * hours
        

    def __str__(self):
        '''##### ADD CODE HERE #####'''
        return f'Temporary_Employee\n{getattr(self,"name")},{getattr(self,"id")},{getattr(self,"salary")},{getattr(self,"hours")}'
        # Added a new getattr() for "hours" as Temp Employees get paid hourly
    

############################################################
############################################################
############################################################
    

class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        '''##### ADD CODE HERE #####'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def cal_salary(self):
        base_salary = getattr(self, "salary")
        hours = getattr(self, "hours")
        trips = getattr(self, "travel")

        return (base_salary * hours) + (trips * 1000)

    def __str__(self):
        '''##### ADD CODE HERE #####'''
        return f'Consultant\n{getattr(self,"name")},{getattr(self,"id")},{getattr(self,"salary")},{getattr(self,"hours")},{getattr(self,"travel")}'
        # Added a new getattr() for "hours" and "travel" as Consultants are hourly and get paid for travel


############################################################
############################################################
############################################################
    

class Consultant_Manager(Consultant, Manager):
    def __init__(self, **kwargs):
        '''##### ADD CODE HERE #####'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def cal_salary(self):
        base_salary = getattr(self, "salary")
        hours = getattr(self, "hours")
        trips = getattr(self, "travel")
        bonus = getattr(self, "bonus")

        return (base_salary * hours) + (trips * 1000) + bonus

    def __str__(self):
        '''##### ADD CODE HERE #####'''
        return f'Consultant_Manager\n{getattr(self,"name")},{getattr(self,"id")},{getattr(self,"salary")},{getattr(self,"hours")},{getattr(self,"travel")},Consultant_Manager\n{getattr(self,"name")},{getattr(self,"id")},{getattr(self,"salary")},{getattr(self,"bonus")}'
        # Added a new getattr() for "hours","travel" as Consultant Managers are hourly, get paid for travel and recieve a bonus
    

############################################################
############################################################
############################################################


def calculate_total_salaries(employee_list):
    '''##### ADD CODE HERE #####'''
    total_salaries = 0

    for employee in employee_list:                                                      # Loops through given employee list
        total_salaries = total_salaries + employee.cal_salary()                         # For each employee in the list... call the cal_salary() on each employee and add to tot_salaries variable

    return f'Total Salary of all employees: {total_salaries}'


def calculate_manager_salaries(employee_list):
    '''##### ADD CODE HERE #####'''
    total_manager_salaries = 0

    for manager in employee_list:                                                       # Loops through given employee_list
        if isinstance(manager, Manager) or isinstance(manager, Consultant_Manager):     # isinstance checks if an object is an instance of a class 
            total_manager_salaries = total_manager_salaries + manager.cal_salary()      # If they are indeed a manager... then call cal_salary() on the manager object

    return f'Total Salary of all managers: {total_manager_salaries}'


''' ##### DRIVER CODE #####
    ##### Do not change. '''

# create employees
chris = Employee(name="Chris", id="UT1", salary=80000)
emma = Permanent_Employee(name="Emma", id="UT2",salary=100000, benefits=["health_insurance"])
sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
matt = Consultant_Manager(name="Matt", id="UT6",salary=1000, hours=40, travel=4, bonus=10000)

# print employees
print(chris, "\n")
print(emma, "\n")
print(sam, "\n")
print(john, "\n")
print(charlotte, "\n")
print(matt, "\n")

# calculate and print salaries
print("Check Salaries")
print("Emma's Salary is:", emma.cal_salary())
emma.benefits = ["health_insurance"]
print("Emma's Salary is:", emma.cal_salary())
emma.benefits = ["retirement", "health_insurance"]
print("Emma's Salary is:", emma.cal_salary())
print("Sam's Salary is:", sam.cal_salary())
print("John's Salary is:", john.cal_salary())
print("Charlotte's Salary is:", charlotte.cal_salary())
print("Matt's Salary is:",  matt.cal_salary())


 
# Testing

# print(calculate_total_salaries([chris, emma, sam, john, charlotte, matt]))
# print(calculate_manager_salaries([chris, emma, sam, john, charlotte, matt]))
