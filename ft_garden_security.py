class Plant:
    def __init__(
        self,
        name: str,
        starting_height: float,
        starting_age: int
    ) -> None:
        self._name = name
        if starting_height >= 0:
            self._height = starting_height
        else:
            print(f"{self._name}: Error, height can't be negative")
        if starting_age >= 0:
            self._current_age = starting_age
        else:
            print(f"{self._name}: Error, age can't be negative")
        print(
            f"Plant created: {self._name}: {self._height}cm, "
            f"{self._current_age} days old"
        )

    def grow(self, amount: float = 0.8) -> None:
        self._height = self._height + amount

    def show(self):
        print(
            f"Current state: {self._name}: {self._height}cm, "
            f"{self._current_age} days old"
        )

    def age(self) -> None:
        self._current_age = self._current_age + 1
        self.grow()

    def set_heigth(self, new_height: int) -> None:
        if new_height >= 0:
            self._height = new_height
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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)

    print("")

    rose.set_heigth(25)
    rose.set_age(30)

    print("")

    rose.set_heigth(-5)
    rose.set_age(-5)

    print("")

    rose.show()
    print("or")
    print(
        f"Current state: {rose._name}: {rose.get_height()}cm, "
        f"{rose.get_age()} days old"
    )
