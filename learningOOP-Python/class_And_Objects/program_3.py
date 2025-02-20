class Dog: 
    def __init__(self, name, breed): # Allows create some data field
        self.name = name # Atributtes
        self.breed = breed 
    def bark(self): # Defines method for the class Dog
        print("Whoof Whoof")

dog1 = Dog("Bruce", "Scottich Terrifier") # This instaciate the object
dog1.bark()
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Freya", "Greyhound") # This instaciate the object
dog2.bark()
print(dog2.name)
print(dog2.breed)