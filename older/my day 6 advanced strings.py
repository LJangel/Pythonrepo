This is variable based formatted string

text = "This is a argument {0}".format("Here")
# results in 'This is a argument Here'

text = "This is a argument {0} {1}".format("Here", "another")
# results in 'This is a argument Here another'

#this next one is used more frequently
"hi there %s! thanks" %("Larry")
#results in 'hi there Larry! thanks'

#float substitution
text = "2 decimal places: %.2f" %(20)
print(text)
#results in '2 decimal places: 20.00'.  the last
#parenthesis is the number being used

#date substitution
#get today's date
import datetime #this is a built in Python object
today = datetime.date.today()
today
#results in "datetime.date(2018, 2, 25)"

import datetime

default_names = ["justin", "john", "emilee", "jim", "Ron", "sandra", "veronica", "whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}!  Thank you for the purchase on 
{date}.  We hope you are excited about using it.  Just
as a reminder, the purchase total was ${total}.
Have a great one.
CFE Team
"""

def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            name = name[0].upper() + name[1:].lower()
            new_amount = "%.2f" %(amounts[i])
            new_msg = unf_message.format(  #unformatted message
                name = name,
                date = text,
                total = new_amount 
                )
            i += 1
            print(new_msg)

make_messages(default_names, default_amounts)

