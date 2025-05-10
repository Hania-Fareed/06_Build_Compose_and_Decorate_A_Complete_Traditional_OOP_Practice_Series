class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The iterator object is the class itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Required to stop the loop
        else:
            value = self.current
            self.current -= 1
            return value

# Example usage
cd = Countdown(5)
for number in cd:
    print(number)
