class Bus():
    def __init__(self, speed, capacity, max_speed, empty_seats):
        self.speed = speed
        self.capacity = capacity
        self.max = max_speed
        self.empty = empty_seats

    def posadka(self, kolvo):
        if self.empty >= kolvo:
            self.empty -= kolvo
            print('Посадили - ', kolvo)
        else:
            print('Посадили -', self.empty)
            self.empty = 0
    def razgon(self, speed):
        if speed + self.speed < self.max:
            print(self.speed + speed)
            self.speed = speed
        else:
            print(self.max)
            self.speed = self.max

bus1=Bus(40, 80, 120, 10)
bus1.posadka(20)
bus1.razgon(70)








