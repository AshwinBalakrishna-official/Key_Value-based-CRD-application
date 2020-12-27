import CRD as op #importing the crd.py file to call the various functions created and referecning it as "op" stanging for output

#CREATING OR ADDING A NEW VALUE
op.create("apple",35)

op.create("banana",45)

op.create("carrot",30,45000) #CREATING A KEY PAIR WITH A TIMEOUT WITH TIMEOUT MENTIONED IN (number of seconds)

op.read("apple") #RETURNS THE VALUE IN THE JSON object FORMAT OF "key:pair"

op.read("carrot")

op.update("apple",40) #UPDATING OR MODIFYING THE EXISTING VALUES OF THE APPLE KEY BY INITIALIZING A NEW VALUE 



op.display()
