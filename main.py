import CRD as op #importing the crd.py file to call the various functions created and referecning it as "op" stanging for output
import time         #USED FOR TIMEOUT USEAGE
import threading    #USE IMPORT THREAD FOR PYTHON VERSIONS BELOW 3.0
from threading import *

#CREATING OR ADDING A NEW VALUE
op.create("apple",35)

op.create("banana",45)

op.create("carrot",30)

op.create("dates",50,300) #CREATING A KEY PAIR WITH A TIMEOUT WITH TIMEOUT MENTIONED IN (number of seconds)

#READING THE VALUES
op.read("apple") #RETURNS THE VALUE IN THE JSON object FORMAT OF "key:pair" OF A NON-TIMEOUT ELEMENT

op.read("dates")#RETURNS THE VALUE IN THE JSON object FORMAT OF "key:pair" OF A TIMEOUT APPLICABLE ELEMENT


#UPDATE THE VALUE
op.update("apple",40) #UPDATING OR MODIFYING THE EXISTING VALUES OF THE APPLE KEY BY INITIALIZING A NEW VALUE 

#DELETING THE VALUE 
op.delete("banana") #REMOVING A PARTICULAR VALUE FROM THE DATA STORE

#CHECKING IF THE TIMEOUT ELEMENT HAS EXPIRED OR NOT AFTER 300 SECS
op.read("dates")

#DISPLAYING ALL THE ELEMENTS PRESENT IN DATA STORE
op.display()

#USING MULTIPLE THREADS TO ACCESS THE PROGRAM IS POSSIBLE BUT IT'S NOT GONNA CAUSE ANY TROUBLE SINCE THE DATA STORE IS ACCESSED ONE OPERATION AT A TIME
th_1=Thread(target=(op.create),args=("plum",45,)) #ASSIGNING EACH OPERATION WITH ITS NECESSARY VALUES
th_1.start()
th_1.join()
#YOU CAN MAKE MULTIPLE THREADS UPTO "th_n" and there is still going to be no problems though multiple threads are used since the race conditions are not going to affect it.


