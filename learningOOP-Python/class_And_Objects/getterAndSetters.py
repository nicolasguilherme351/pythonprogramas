# Getters and setters
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email 
        self.password = password
    def get_email(self): # allows you acess inaccessible data
        return self._email
    
    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    
user1 = User("Peter", "Peter@gmail.com", "peter123")
print(user1.get_email())

user1.set_email("dannyoutlook.com")
print(user1.get_email())
