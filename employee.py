import datetime


class Employee:
    def __init__(self, name, payment,):
        self.payment_m = payment
        self.name = name
        
    
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
    def work(self):
        return "я прихожу в офис и начинаю програмировать"

l = [Employee("Oleg", 100), Employee("Marina", 50), Employee("Kolya", 7)]
print(sorted(l))
print(Employee("oly", 3).check_salary())
