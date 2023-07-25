print('Exercise 1:')

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self) -> str:
        s = 's' if self.amount > 1 else ''
        return(f'{self.amount} {self.currency}{s}')

    def __int__(self) -> int:
        return(self.amount)

    def __repr__(self) -> str:
        s = 's' if self.amount > 1 else ''
        return(f'{self.amount} {self.currency}s')

    def __add__(self, other):
        try:
            if self.currency != other.currency:
                raise TypeError  
        except AttributeError:
            if type(other) == int:
                print(self.amount + other)
            elif type(self) == int:
                print(self + other.amount)
        except TypeError:
            print("TypeError: Cannot add between Currency type <{c1}> and <{c2}>"
            .format(c1=self.currency, c2=other.currency))
        else:
            print(self.amount + other.amount) 

    def __iadd__(self, other):
        try:
            if self.currency != other.currency:
                raise TypeError  
        except AttributeError:
            if type(other) == int:
                self.amount += other
            elif type(self) == int:
                self + other.amount
        except TypeError:
            print("TypeError: Cannot add between Currency type <{c1}> and <{c2}>"
            .format(c1=self.currency, c2=other.currency))
        else:
            self.amount += other.amount
        return(self)            

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1) 
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
c1 + 5
c1 + c2
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
c3 += c2
c1 + c3


print('\n----------------\nExercise 2:')
from func import my_add
my_add(5, 10)

print('\n----------------\nExercise 3:')
import random
def numbers(num= int(input('Enter a number between 1 and 100: '))):        
    if num == random.randint(1, 101):
        print('Success')

numbers() 

print('\n----------------\nExercise 4:')
import string

def string_module(length=5):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    print(random_string)

string_module()

print('\n----------------\nExercise 5:')
import datetime as date

def date_time():
    print(date.datetime.now().strftime('%d-%m-%Y'))

date_time()

print('\n----------------\nExercise 6:')
from datetime import datetime

def amount_time():
    now = datetime.now()
    until = datetime(2024, 1, 1, 0, 0, 0)
    count = until - now 
    m, s = divmod(count.seconds, 60)
    h, m = divmod(m, 60)
    print(f"the 1st of January is in {count.days} days and {h:02}:{m:02}:{s:02} hours")

amount_time()

print('\n----------------\nExercise 7:')

def minutes_of_live(birth_date = input('Enter your birth date (DD-MM-YYYY): ')):
    birth_date = datetime.strptime(birth_date, '%d-%m-%Y')
    now = datetime.now()
    count = now - birth_date
    m = count.days * 24 * 60
    print(f"You have lived {m:02} minutes")

minutes_of_live()    

print('\n----------------\nExercise 8:')
import faker

users = []

def create_users():
    for _ in range(5):
        fake = faker.Faker()
        users.append({"name" : fake.name(), "address" : fake.address(), "langage_code" : fake.language_code()})
    print(users)    

create_users()