class user():
    def __init__(self, first, job, hobby):
        self.first = first
        self.job = job
        self.hobby = hobby
    def des(self):
        
        print('Name is ' + self.first.title()+'!')
        print('their job is '+self.job.title()+'!')
        print('their favorite hobby is '+self.hobby.title()+'!')
        
    def greet(self):
        print('Hi '+ self.first.title()+'. i see that you work at/as a '
              + self.job.title()+'. i see that your favorite hobby is '
              + self.hobby.title()+', that is my favorite hobby too!')
        
class Admin(user):
    def __init__(self, first, job, hobby):
        super().__init__(first, job, hobby)
        self.privileges = Privileges()
    
class Privileges():
    def __init__(self, privileges = ['ban users', 'can add post', 'can delete post']):
        self.privileges = privileges
        
    def show_priv(self):
        print(self.privileges)
        
admin = Admin('Noah', "Banker", 'videos')
admin.privileges.show_priv()