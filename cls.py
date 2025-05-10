class Counter:
    count = 0  # Class variable to track number of objects

    def __init__(self):
        Counter.count += 1  # Increase count whenever an object is created

    @classmethod
    def show_count(cls):
        print("Total objects created:", cls.count)

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.show_count()  # Output: Total objects created: 3
