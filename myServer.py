import random 

users = "root"
age = random.randint(10,25)

def main():
    while True:
        if age == 18 and users == "root":
            print("Доступ на сервер безумные зомби разрешен")
            break
        else:
            print("Вход запрещен!")

if __name__ == "__main__":
    main()