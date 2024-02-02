"""
Mavzu:OOP,obyektaga yo'naltirilgan dastrulash yoki Object oriented programming
Amaliyot
Sana:10.03.2023
Muallif:Atadjanov
telegram:@atadjanovd
"""
# Veb-sahifangiz uchun foylanuvchi (user) klassini tuzing.
# Klassning xususiyatlari sifatida,odatda,ijtimoiy tarmoqlar
# talab qiladigan ma'lumotlarni kiriting(ism,familiya,foyalanuvchi ismi,email va hokazolar)

class User:
    """User nomi klass yaratamiz:"""
    def __init__(self,name,lastname,username,email):
        self.name = name
        self.username = username
        self.email = email
        self.lastname = lastname
    def get_name(self):
        """Returns name the user """
        return self.name
    def get_username(self):
        """Returns username the user."""
        return self.username
    def get_email(self):
        """Returns email the user"""
        return self.email
    def get_lastname(self):
        """Returns lastname the user."""
        return self.lastname
    def get_fullname(self):
        """Returns all information about the user."""
        return f"User:{self.username},Ismi: {self.name} {self.lastname},email:{self.email}"
user1 = User("Davronbek","Atadjanov","atadjanovd","davronbekatadjanov@gmail.com")
print(user1.get_fullname())

user2 = User("Sandibek","Kenjaliyev","sandibek123","sandibekkenjaliyev@gmail.com")
user3 = User("Amirbek","Xudayberganov","amirbek123","amirbekxudayberganov@gmail.com")
print(user2.get_name())
print(user3.get_lastname())
print(user2.get_username())
print(user3.get_fullname())
