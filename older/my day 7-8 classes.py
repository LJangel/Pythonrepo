#we started with this class below
class Dog():
    name = 'larry' #attribute
    color = 'brown' #attribute
    def get_color(self): #this function is a method
        return self.color

obj.get_color() #obj is an instance of class Dog
#obj == self 

obj.color = "White"
#sets the obj color to white
#for this instance called obj

#then to inheritance
class Animal():
    noise = "grunt"
    size = "large"
    color = "brown"
    hair = "covers body"
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise

dog = Animal() #instance of Animal class called dog
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"

#class attribute inheritance shown below
class Dog(Animal):
    name = 'larry' #attribute

larry = Dog() #"larry" is instance of Dog which inherits from Animal
larry.color = "white"
larry.name = "John Snow"

#my practice with class inheritance
class furniture():
    base_unit = "tables"
    extras = "sofa"
    lamps = 2
    leaf = 2
    num_legs = 6
    def get_legs(legs):
        return legs.num_legs
    def num_lamps(lamp_num):
        return lamp_num.lamps
    def num_leafs(leaves):
        return leaves.leaf

class tables(furniture): #inherits from furniture class
    num_legs = 4
    top_style = "oval"
    wood_type = "ash"
    lamps = 3
    
party = tables # defines an instance of "tables" called "party"
party.leaf #this results in "2" because it inherits from furniture
party.lamps # this results in "3" because it overrides the parent class
party.get_legs # returns 4
party.num_lamps # returns 3
party.num_leafs # returns 2

#continue on day 8 adding another argument to the function
class Animal():
    noise = "grunt"
    size = "large"
    color = "brown"
    hair = "covers body"
    def get_color(self, abc): #self is a built in argument referring to any instance of this class
        return self.color
    def make_noise(self):
        return self.noise

dog = Animal()
dog.get_color() #this returns an error because the 2nd argument is missing


#more about functions
#arg == Positional Argument, these are required
#kwarg == key word Argument, these are optional, set like a variable
#kwargs must be before positional arguments in statement
def some_func(arg_1, arg_2, arg_3, kwarg_="abc"): 
pass #minimum "do nothing" statement to not get an error
#return arg_1
def some_func(arg_1=None, arg_2, arg_3, kwarg_=None): 
    #setting to "None" avoids errors, as optional, but 
    #this is now a kwarg before positional args and will
    #result in an error

def some_func(arg_1, arg_2, kwarg_1=None, kwarg_2=None):
    print(arg_1, arg_2)
    if kwarg_1 !=None:
        print(kwarg_1)

#lesson takeaway is if you have arguments and they aren't
#equal to something, they must be passed

#example
some_func("abc", "car", kwarg_1="not a big deal")
#returns abc car "not a big deal"

def send_email(email_address, to_list, from_list):
#this won't make a lot of sense, so use version below

email_address = "another@gmail.com"
to_list = ["abc@gmail.com"]
from_list = ["another2@gmail.com", "hello@cfe.com"]
def send_email(email=email_address, to_list=to_list, from_list=from_list):
    pass

send_email(email="hello@cfe.com", to_list="abc@gmail.com", from_list="another2@gmail.com"):

#revisit earlier function with arg error
class Animal():
    noise = "grunt"
    size = "large"
    color = "brown"
    hair = "covers body"
    def get_color(self, abc): #self is a built in argument referring to any instance of this class
        return self.color + " " + abc
    def make_noise(self):
        return self.noise

dog = Animal()
dog.get_color("red") #self arg doesn't need to be called out, so this is the value for abc
#results in "brown red"

#making a method function a property to call it as such
class Animal():
    noise = "grunt"
    size = "large"
    color = "brown"
    hair = "covers body"
    def get_color(self, abc): #self is a built in argument referring to any instance of this class
        return self.color + " " + abc
    @property
    def make_noise(self):
        return self.noise

dog = Animal()
dog.make_noise() #calling it as a function
dog.make_noise #calling as a property



