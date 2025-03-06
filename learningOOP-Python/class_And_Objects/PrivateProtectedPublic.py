# Encapsulament
# Acessin
# Protected attributes
class User:
    def __init__(self, username, email, password):
        self.username = username
        # self.email = email public
        # self._email = email protected
        self.__email = email # email private
        self.password = password
    def clean_email(self):
        return self.__email.lower().strip()
    
user1 = User("Peter", "   Peter@gmail.com  ", "peter123")

# print(user1.__email) Not works with private
print(user1.clean_email())

