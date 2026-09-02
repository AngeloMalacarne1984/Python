class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0

        def display(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, "
                f"{self.show_calls} show"
            )

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
        self._stats = self.Statistics()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount: float = 1.0) -> None:
        self._stats.grow_calls += 1
        self._height = round(self._height + amount, 1)

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"{self._name}: {self._height}cm, {self._current_age} days old")

    def age(self) -> None:
        self._stats.age_calls += 1
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

    def grow(self, amount: float = 8.0) -> None:
        super().grow(amount)

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls: int = 0

        def display(self, name: str) -> None:
            super().display(name)
            print(f"{self.shade_calls} shade")

    def __init__(
        self,
        name: str,
        starting_height: float,
        starting_age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, starting_height, starting_age)
        self._trunk_diameter = round(trunk_diameter, 1)
        self._stats = self.TreeStatistics()

    def produce_shade(self) -> None:
        if isinstance(self._stats, Tree.TreeStatistics):
            self._stats.shade_calls += 1
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


class Seed(Flower):
    def __init__(
        self,
        name: str,
        starting_height: float,
        starting_age: int,
        color: str
    ) -> None:
        super().__init__(name, starting_height, starting_age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def grow(self, amount: float = 30.0) -> None:
        super().grow(amount)

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def age(self) -> None:
        self._stats.age_calls += 1
        self._current_age = self._current_age + 20
        self.grow()


def display_statistics(plant: Plant) -> None:
    plant._stats.display(plant._name)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)
