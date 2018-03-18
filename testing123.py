from day_9_importing import some_rando, make_messages
#importing class MessageUser and functions "some_rando" and "make_messages"
# from a file called "day_9_importing"
from py_day_mod.make_messages import MessageUser
#imports from the folder "py_day_mod" (callable because of "__init__" file appearing in the folder)

obj = MessageUser()
obj.add_user("justin", 123.32, email="me.gmail.com")
obj.add_user("john", 94.23)
obj.add_user("emilee", 124.32)
obj.add_user("jim", 323.4)
obj.add_user("marie", 13.23)
obj.get_details()

print(obj.make_messages())

#some_rando()

default_names = ["justin", "john", "emilee", "jim", "Ron", "sandra", "veronica", "whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]
#function below relies on the defaults above
make_messages(default_names, default_amounts)
