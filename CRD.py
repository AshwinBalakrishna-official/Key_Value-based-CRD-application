#IMPORT THE NECESSARY PACKAGES FOR THREADING AND TIMEOUTS
import threading    #USE IMPORT THREAD FOR PYTHON VERSIONS BELOW 3.0
import time
from threading import *

#intialize a dictionary for storing key pair values
in1={} #in1 declaring a dictionary which would contain key value pairs

#OPERATION 1: "CREATING" A NEW PAIR 
#CONDITION : TIMEOUT OPTION TO BE INCLUDED. INITIALLY SET TO 0
def create(key,value,time_out=0):
    if key in in1: #CHECK IF THE KEY IS ALREADY PRESENT IN THE DICTIONARY
        print("Key is already present")
    else:
        if(key.isalpha()):
            if len(in1)<(1024*1020*1024) and value<=(16*1024*1024): #FOR CHECKING FILE SIZE LESS TAN 1GB AND DATA STORE VALUE LESS THAN 16KB
                if time_out==0:
                    in2=[value,time_out]
                else:
                    in2=[value,time.time()+time_out]
                if len(key)<=32: #CHECKING INPUT KEY_NAME CAPPED AT 32CHARS
                    in1[key]=in2
            else:
                print("MEMORY LIMIT EXCEEDED PLEASE CHECK")#MEMORY CHECK ERROR
        else:
            print("PLEASE CHECK YOUR INPUT, ONLY ALPHABETS ARE ACCEPTED")#INPUT TYPECHECK

#OPERATION 2: "READING / DISPLAYING" THE KEYPAIR OF A SINGLE KEY
def read(key):
    if key not in in1: #CHECKING AVAILABILITY
        print("THE KEY YOU SEARCHED FOR DOES NOT EXIST") 
    else:
        in3=in1[key] #STORING KEY VALUE FOR EASY ACCESS
        if in3[1]!=0:
            if time.time()<in3[1]: #CHECKING THE AVAILABILITY OF KEY BASED ON TIMEOUT
                ob1=str(key)+":"+str(in3[0]) #IF KEY IS STILL PRESENT THEN RETURN IT IN JSON OBJECT FORMAT AS A KEY PAIR
                return ob1
            else:
                print(key," HAS ALREADY EXPIRED") #EXPIRED MESSAGE FOR TIMEOUT
        else:
            ob1=str(key)+":"+str(in3[0])
            return ob1

#OPERATION 3: "DELETING" A KEYPAIR
def delete(key):
    if key not in in1: #CHECKING AVAILABILITY
        print("THE KEY YOU SEARCHED FOR DOES NOT EXIST") 
    else:
        in3=in1[key]
        if in3[1]!=0:
            if time.time()<in3[1]: #CHECKING THE AVAILABILITY OF KEY BASED ON TIMEOUT
                del in1[key]
                print("THE KEY HAS BEEN REMOVED SUCCESSFULLY")
            else:
                print(key," HAS ALREADY TIMEDOUT") #EXPIRED MESSAGE FOR TIMEOUT
        else:
            del in1[key]
            print("KEY HAS BEEN REMOVED SUCCESSFULLY")

#IN ADDITION TO THE REQUIREMENTS SPECICFIED I WOULD ALSO LIKE TO ADD THE UPDATE OPTION TO COMPLETE THE REQUIREMENTS OF A CRUD APPLICATION

#OPERATION 4: "UPDATE/MODIFY"
def update(key,value):
    in3=in1[key]
    if in3[1]!=0:
        if time.time()<in3[1]:
            if key not in in1:
                print("KEY DOES NOT EXIST") #CHECKING AVAILABILITY
            else:
                in2=[]
                in2.append(value)
                in2.append(in1[1])
                in1[key]=in2
        else:
            print(key," HAS ALREADY EXPIRED") #EXPIRY CHECK
    else:
        if key not in in1:
            print("KEY DOES NOT EXIST") #AVAILABILITY CHECK
        else:
            in2=[]
            in2.append(value)
            in2.append(in3[1])
            in1[key]=in2

#OPERATION 5 : TO DISPLAY ALL ELEMENTS OF THE KEY VALUE PAIR
def display():
    print(in1)
