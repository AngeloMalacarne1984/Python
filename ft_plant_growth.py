class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = round(height, 1)
        self._initial_height = round(height, 1)
        self._current_age = age

    def grow(self, amount: float = 0.8) -> None:
        self._height = round(self._height + amount, 1)

    def age(self) -> None:
        self._current_ageage = self._current_age + 1
        self.grow()


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30)

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        print(f"{rose._name}: {round(rose._height, 1)}cm, {rose.age} days old")
        rose.age()

    total_increase = round(rose._height - rose._initial_height)
    print(f"Growth this week: {total_increase}cm")
