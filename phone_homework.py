class Phone:
    def __init__(self, number):
        self.phone_number = number
        self.count = 0

    def accept_call(self):
        self.count += 1    

phone1 = Phone("222-3333-44")
phone1.accept_call()
phone1.accept_call()

phone2 = Phone("999-000-333")
phone2.accept_call()
phone2.accept_call()
phone2.accept_call()
phone2.accept_call()

phone3 = Phone("867-980-822")
phone3.accept_call()