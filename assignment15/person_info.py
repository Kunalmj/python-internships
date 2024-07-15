class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Example usage:
if __name__ == "__main__":
    # Creating an instance of Person
    person1 = Person("Kunal", 19, "male")
    
    # Calling the introduce method
    person1.introduce()
