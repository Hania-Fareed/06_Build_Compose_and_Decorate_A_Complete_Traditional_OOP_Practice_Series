class Logger:
    def __init__(self):
        print("🔵 Logger initialized. Object created.")

    def __del__(self):
        print("🔴 Logger destroyed. Object deleted.")

# Example usage
log = Logger()

# Optional: manually delete to trigger destructor
del log
