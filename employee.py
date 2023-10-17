import datetime
class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    def __init__(self, name, payment, email):
        self.payment_m = payment
        self.name = name
        self.email = email
        self.save_email() 
    def save_email(self):
        f = open("emails.csv", "a")    
        f.write(self.email)
        f.close()
    def validate(self):
        f = open("emails.csv", "r")    
        for e in f:
            if e == self.email:
                raise EmailAlreadyExistsException()
            

        
    
    def work(self):
        return "я прихожу в офис"  
    
    def __str__(self):
        return f"Должность {self.__class__.__name__}, Имя: {self.name}"
    
    def __lt__(self, other):
        return self.payment_m < other.payment_m 
    
    def __repr__(self):
        return self.__str__()
    
    def check_salary(self, days=None):
        if days is None:
            vremya = datetime.date.today()
     
            working_day = 0

            while vremya.day != 1:
                if vremya.weekday() < 5:
                    working_day += 1
                vremya -= datetime.timedelta(days = 1)
            if vremya.weekday() < 5:
                working_day += 1 
            days = working_day 
        return self.payment_m*days
            
        



class Recruiter(Employee):
    def work(self):
        return "я прихожу в офис и начинаю нанимать сотрудников"    
    
class Developer(Employee):
    tech_stack = []
    def __init__(self,tech_stack, *args):
        self.tech_stack = tech_stack
        super().__init__(*args)
    def work(self):
        return "я прихожу в офис и начинаю програмировать"
    def compare(self,other):
        return len(self.tech_stack)<len(other.tech_stack)
    def __add__(self,other):
         return Developer(
            list(set(self.tech_stack).union(set(other.tech_stack))),
            self.name + " " + other.name, 
            max(self.payment_m, other.payment_m)
        )


# l = [Employee("Oleg", 100), Employee("Marina", 50), Employee("Kolya", 7)]
# print(sorted(l))
# print(Employee("oly", 3).check_salary())

# a = Developer(["a","b","c"],"marina",5000)
# b = Developer(["c","e"], "nency", 800)
# print(a.compare(b))
# c = a + b 
# print(c)
# print(c.tech_stack)
a = Employee("marina",9000,"djdjk@mail.ru")
a.validate()