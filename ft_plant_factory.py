class Plant:
    def __init__(
        self,
        name: str,
        starting_height: float,
        starting_age: int
    ) -> None:
        self._name = name
        self._height = round(starting_height, 1)
        self._current_age = starting_age

    def grow(self, amount: float = 0.8) -> None:
        self._height = round(self._height + amount, 1)

    def show(self):
        print(
            f"Created: {self._name}: {self._height}cm, "
            f"{self._current_age} days old"
        )

    def age(self) -> None:
        self._current_age = self._current_age + 1
        self.grow()


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    for plant in plants:
        plant.show()
