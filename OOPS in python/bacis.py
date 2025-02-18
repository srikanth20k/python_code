

class car :
    def __init__(self,milage,year,make,model):
        self.milage = milage
        self.year = year
        self.make = make
        self.model = model
    def age(a,current_year):
        return current_year - a.year
    def __str__(self):
        return f'{self.make} {self.model} has milage of {self.milage} and made in {self.year}'
    
    
nano = car(30,2019,'TATA','nano')
nano.age(2021)
# nano.milage
# print(nano.year)