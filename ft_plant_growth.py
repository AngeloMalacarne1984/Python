#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = round(height, 1)
        self.initial_height = round(height, 1)
        self.age = age

    def grow(self, amount: float = 0.8) -> None:
        self.height = round(self.height + amount, 1)

    def age(self) -> None:
        self.age = self.age + 1
        self.grow()

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    
    rose = Plant("Rose", 25.0, 30)

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        print(f"{rose.name}: {round(rose.height, 1)}cm, {rose.age} days old")
        rose.age()

    total_increase = round(rose.height - rose.initial_height)
    print(f"Growth this week: {total_increase}cm")
