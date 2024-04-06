"'create a class, functions with init function '"

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def check_balance(self):
        print(f"Current balance for {self.owner}: {self.balance}")

    def transfer(self, recipient, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transfer of {amount} to {recipient.owner} successful.")
        else:
            print("Insufficient funds or invalid amount for transfer.")

    def change_owner(self, new_owner):
        self.owner = new_owner
        print(f"Account owner changed to {self.owner}.")

    def add_interest(self, rate):
        if rate >= 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            print(f"Interest added: {interest}")
        else:
            print("Invalid interest rate.")

    def close_account(self):
        self.balance = 0
        print("Account closed.")

acc1 = BankAccount("Bhuvi", 1000)
acc2 = BankAccount("Muku", 500)

acc1.deposit(200)
acc1.check_balance()

acc1.transfer(acc2, 300)

acc1.check_balance()
acc2.check_balance()

acc2.withdraw(100)
acc2.check_balance()

acc1.add_interest(5)
acc1.check_balance()

acc1.close_account()
acc1.check_balance()

"""
 Deposit of 200 successful.
Current balance for Bhuvi: 1200
Transfer of 300 to Muku successful.
Current balance for Bhuvi: 900
Current balance for Muku: 800
Withdrawal of 100 successful.
Current balance for Muku: 700
Interest added: 45.0
Current balance for Bhuvi: 945.0
Account closed.
Current balance for Bhuvi: 0
"""


"' Add a match case,try and exception '"



class Actor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Director:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

class Movie:
    def __init__(self, title, director, actors, budget):
        self.title = title
        self.director = director
        self.actors = actors
        self.budget = budget

class Studio:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def produce_movie(self, title, director, actors, budget):
        try:
            if isinstance(director, Director) and all(isinstance(actor, Actor) for actor in actors):
                movie = Movie(title, director, actors, budget)
                self.movies.append(movie)
                print(f"{title} successfully produced by {self.name}.")
            else:
                raise ValueError("Invalid input types for producing movie.")
        except ValueError as e:
            print(e)

    def cast_actor(self, movie, actor):
        try:
            if movie in self.movies and isinstance(actor, Actor):
                movie.actors.append(actor)
                print(f"{actor.name} cast in {movie.title}.")
            else:
                raise ValueError("Movie not found or invalid actor.")
        except ValueError as e:
            print(e)

    def assign_director(self, movie, director):
        try:
            if movie in self.movies and isinstance(director, Director):
                movie.director = director
                print(f"{director.name} assigned as director for {movie.title}.")
            else:
                raise ValueError("Movie not found or invalid director.")
        except ValueError as e:
            print(e)

studio = Studio("360 Entertainment Production")

director1 = Director("Suriavelan", "Experienced")
actor1 = Actor("Stephen Zechariah", 35)
actor2 = Actor("Vikneswary Se", 30)

studio.produce_movie("NAAM", director1, [actor1, actor2], 100000000)

actor3 = Actor("Abbdul Kather", 40)
studio.cast_actor(studio.movies[0], actor3)

director2 = Director("Rupini", "Veteran")
studio.assign_director(studio.movies[0], director2)


"""
NAAM successfully produced by 360 Entertainment Production.
Abbdul Kather cast in NAAM.
Rupini assigned as director for NAAM.
"""