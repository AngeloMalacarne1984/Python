class Plant:
    def __init__(
        self,
        name: str,
        starting_height: float,
        starting_age: int
    ) -> None:
        self._name = name
        if starting_height >= 0:
            self._height = round(starting_height, 1)
        else:
            print(f"{self._name}: Error, height can't be negative")
        if starting_age >= 0:
            self._current_age = starting_age
        else:
            print(f"{self._name}: Error, age can't be negative")

    def grow(self, amount: float = 0.8) -> None:
        self._height = round(self._height + amount, 1)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._current_age} days old")

    def age(self) -> None:
        self._current_age = self._current_age + 1
        self.grow()

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = round(new_height, 1)
            print(f"Height updated: {self._height}cm")
        else:
            print(
                f"{self._name}: Error, height can't be negative\n"
                f"Height update rejected"
            )

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._current_age = new_age
            print(f"Age updated: {self._current_age} days")
        else:
            print(
                f"{self._name}: Error, age can't be negative\n"
                f"Age update rejected"
            )

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._current_age


class Flower(Plant):
    def __init__(
        self,
        name: str,
        starting_height: float,
        starting_age: int,
        color: str
    ) -> None:
        super().__init__(name, starting_height, starting_age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        starting_height: float,
        starting_age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, starting_height, starting_age)
        self._trunk_diameter = round(trunk_diameter, 1)

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        starting_height: float,
        starting_age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, starting_height, starting_age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.age()
    tomato.show()
