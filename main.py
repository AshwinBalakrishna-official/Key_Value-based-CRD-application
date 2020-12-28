import CRD as op #importing the crd.py file to call the various functions created and referecning it as "op" stanging for output
import time #FOR ADDING DELAY TO KILL THE TIMEOUT DATA

#CREATING OR ADDING A NEW VALUE
op.create("apple",35)

op.create("banana",45)

op.create("carrot",30,45) #CREATING A KEY PAIR WITH A TIMEOUT WITH TIMEOUT MENTIONED IN (number of seconds)

#READING THE VALUES
op.read("apple") #RETURNS THE VALUE IN THE JSON object FORMAT OF "key:pair"

op.read("carrot")


#UPDATE THE VALUE
op.update("apple",40) #UPDATING OR MODIFYING THE EXISTING VALUES OF THE APPLE KEY BY INITIALIZING A NEW VALUE 

#DELETING THE VALUE 
op.delete("banana") #REMOVING A PARTICULAR VALUE FROM THE DATA STORE

time.sleep(50)#DELAY BEING ADDED TO CHECK THE PROCESS OF TIMEOUT ELEMENT WORKING OR NOT

op.read("carrot")

#DISPLAYING ALL THE ELEMENTS
op.display()
