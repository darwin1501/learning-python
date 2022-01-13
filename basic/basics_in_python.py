class BasicPython:

    name = "jhon"
    fruits = ["apple", "banana", "mango"]
    new_fruits = []
    @staticmethod
    def print_a_message():
        print(f"Hello World {BasicPython.name}")

    @staticmethod
    def fill_the_list():
        # inline for loop inside list
        new_fruits = [
            f
            for f in BasicPython.fruits
        ]
        print(new_fruits)
