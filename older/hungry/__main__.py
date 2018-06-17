import argparse
from argparse import ArgumentParser
from data_class import UserManager
#from data_manager import read_data  #since data_manager is in the same folder, this function can be imported by __main__.py
from utils.templates import get_template, render_context #import functions from utils folder

parser = argparse.ArgumentParser(prog="hungry") #directory is a valid module with "__init__.py" in it
parser.add_argument("type", type=str, choices=['view', 'message'])
parser.add_argument('-id','--user_id', type=int)
parser.add_argument('-e','--email', type=str)

args = parser.parse_args()

#print(args)
#print(args.user_id)
#print(read_data(user_id=args.user_id)) #allows to get data based on what we are passing
#print(read_data(email=args.email))

if args.type == "view":
    print(UserManager().get_user_data(user_id=args.user_id, email=args.email)) #allows to get data based on what we are passing
elif args.type == "message":
    print(UserManager().message_user(user_id=args.user_id, email=args.email))
    #print("send message")