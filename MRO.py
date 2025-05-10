class A:
    def show(self):
        print("A's show method.")

class B(A):
    def show(self):
        print("B's show method.")

class C(A):
    def show(self):
        print("C's show method.")

class D(B, C):
    pass  # No override of show(), so it will inherit from B and C

# Example usage
d = D()
d.show()
