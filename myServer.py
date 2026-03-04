import random 

users = "root"
age = random.randint(10,25)

def main():
    if age == 18 and users == "root":
        print("Доступ на сервер безумные зомби разрешен")