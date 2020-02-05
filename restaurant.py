class Restaurant():
    def __init__(self, name, ty):
        self.name = name
        self.ty = ty
        self.served = 0
        
    def describe(self):
        print('the name of the restuant is ' + self.name.title() + '!')
        print('the type of cuisine is ' + self.ty.title() + '!')
        
    def Open(self):
        print(self.name.title()+" is now open!")
        
    def read(self):
        print("you have served " + str(self.served) + " people today.")
    
    def served(self, serves):
            self.served = serves
    def number(self, people):
        self.served += people