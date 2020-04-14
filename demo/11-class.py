class Car:
    def __init__(self, color, address):
        self.color = color
        self.address = address

    def go(self, distance):
        self.address += distance

    def show_self(self):
        print(f'Hi, I\'m a {self.color} car, I\'m at {self.address}')


car01 = Car(
    color='red',
    address=0,
)

car01.show_self()
car01.go(10)
car01.show_self()
car01.go(10)
car01.show_self()
