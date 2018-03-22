
#Day 9, making a class from a function
#classes are all about "getting" something or "setting" something
import datetime

class MessageUser():
    user_details = []
    messages = []
    base_message = """Hi {name}! Thank you for the purchase on {date}.  We hope you are excited about using it.  Just
as a reminder, the purchase total was ${total}.
Have a great one.
CFE Team
"""
    def add_user(self, name, amount, email=None): #add methods to class
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        detail ={               #add dictionary for users
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail["date"] = date_text
        if email is not None: #if email != None
            detail["email"] = email
        self.user_details.append(detail) #adds the user to user_details list above
    def get_details(self):
        return self.user_details        
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(  #unformatted message
                name = name,
                date = date,
                total = amount 
                )
                self.messages.append(new_msg)
            return self.messages
        return []  #if the if statement results in nothing, return an empty list



obj = MessageUser() #create an instance of class MessageUser
#add some users
obj.add_user("justin", 123.32, email="me.gmail.com")
obj.add_user("john", 94.23)
obj.add_user("emilee", 124.32)
obj.add_user("jim", 323.4)
obj.add_user("marie", 13.23)
obj.get_details()

obj.make_messages() #makes a message for each user


# the class above is letting us set the data below dynamically
default_names = ["justin", "john", "emilee", "jim", "Ron", "sandra", "veronica", "whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

