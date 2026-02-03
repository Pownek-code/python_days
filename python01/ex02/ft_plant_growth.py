class Plant:
    def __init__(self, name: str, init_height: int, init_age: int):
        self.name = name
        self.height = init_height
        self.days_old = init_age

    def grow(self, cm = 1):
        self.height += cm
    def age(self):
        self.days_old += 1
    def get_info(self) -> str:
        return f"{self.name}, {self.height}, {self.days_old}"


if __name__ == "__main__":
    p = Plant("Rose", 5, 3)
    p.grow()
    p.age()
    print(p.get_info())
