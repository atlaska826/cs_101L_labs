import time

""" ----------- """
""" CLOCK CLASS """
""" ----------- """


class Clock:
    def __init__(self, hour, minute, second, clock_type=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    def __str__(self):
        if self.clock_type == 0:
            return '{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second)
        else:
            if self.hour == 0:
                return '12:{:02}:{:02} am'.format(self.minute, self.second)
            elif self.hour == 12:
                return '{:02}:{:02}:{:02} pm'.format(self.hour, self.minute, self.second)
            elif self.hour < 12:
                return '{:02}:{:02}:{:02} am'.format(self.hour, self.minute, self.second)
            else:
                return '{:02}:{:02}:{:02} pm'.format(self.hour - 12, self.minute, self.second)

    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second %= 60
            self.minute += 1

        if self.minute == 60:
            self.minute %= 60
            self.hour += 1

        if self.hour == 24:
            self.hour = 0


""" ------------------------- """
""" MAIN PROGRAM - USER INPUT """
""" ------------------------- """
while True:  # Gets hour from user input
    try:
        hour = int(input('What is the current hour? ==> '))
        while not (0 <= hour <= 24):
            print('Invalid hour value!')
            hour = int(input('What is the current hour? ==> '))
        if hour == 24:
            hour = 0
        break
    except ValueError:
        print('Invalid input type!')

while True:  # Gets minute from user input
    try:
        minute = int(input('What is the current minute? ==> '))
        while not (0 <= minute <= 60):
            print('Invalid minute value!')
            minute = int(input('What is the current minute? ==> '))
        if minute == 60:
            minute = 0
        break
    except ValueError:
        print('Invalid input type!')

while True:  # Gets second from user input
    try:
        second = int(input('What is the current second? ==> '))
        while not (0 <= second <= 60):
            print('Invalid second value!')
            second = int(input('What is the current second? ==> '))
        if second == 60:
            second = 0
        break
    except ValueError:
        print('Invalid input type!')

while True:  # Gets clock_type from user input
    try:
        clock_type = int(input('What is the clock type? (Enter 0 or 1) ==> '))
        while clock_type != 0 and clock_type != 1:
            print('Invalid clock type value!')
            clock_type = int(input('What is the clock type? (Enter 0 or 1) ==> '))
        break
    except ValueError:
        print('Invalid input type!')

""" -------------------- """
""" MAIN PROGRAM - CLOCK """
""" -------------------- """
clock = Clock(hour, minute, second, clock_type)
while True:
    try:
        print(clock)
        time.sleep(1)
        clock.tick()
    except KeyboardInterrupt:
        break
