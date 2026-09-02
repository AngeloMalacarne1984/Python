class Plant:

    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30).show()
    Plant("Sunflower", 80, 45).show()
    Plant("Cactus", 15, 120).show()
