class Dog: 
    def __init__(self, name, breed, owner): # Allows create some data field
        self.name = name # Atributtes
        self.breed = breed 
        self.owner = owner # You can combine different objects! 

    def bark(self): # Defines method for the class Dog
        print("Whoof Whoof")

class Owner: 
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number 
         
owner1 = Owner("Danny ", "122 Springfield Drive", "888-999")
dog1 = Dog("Bruce", "Scottich Terrifier", owner1) # This instaciate the object
print(dog1.owner.name)

owner2 = Owner("Sally", "122 Springfield Drive", "888-999")
dog2 = Dog("Freya", "Greyhound", owner2) # This instaciate the object
print(dog2.owner.name)


