# Базовий клас Dot
class Dot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(f"Dot created with coordinates ({self.x}, {self.y})")

    def __del__(self):
        print(f"Dot at ({self.x}, {self.y}) is being destroyed")

    def display(self):
        print(f"Dot coordinates: ({self.x}, {self.y})")

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        print(f"Coordinates updated to ({self.x}, {self.y})")


# Похідний клас ColorDot
class ColorDot(Dot):
    def __init__(self, x=0, y=0, color="black"):
        # Виклик конструктора батьківського класу для ініціалізації координат
        super().__init__(x, y)
        self.color = color
        print(f"ColorDot created with color {self.color}")

    def __del__(self):
        print(f"ColorDot at ({self.x}, {self.y}) with color {self.color} is being destroyed")

    def display(self):
        # Перевизначення функції виведення з додаванням кольору
        print(f"ColorDot coordinates: ({self.x}, {self.y}), color: {self.color}")

    def set_color(self, color):
        self.color = color
        print(f"Color updated to {self.color}")

    def set_coordinates(self, x, y):
        # Перепризначення функції установки координат
        super().set_coordinates(x, y)  # Виклик методу батьківського класу
        print(f"ColorDot's coordinates updated to ({self.x}, {self.y})")


# Демонстрація роботи з класами
if __name__ == "__main__":
    # Створення екземпляру класу Dot
    dot1 = Dot(1, 2)
    dot1.display()
    dot1.set_coordinates(5, 6)
    
    print("---")

    # Створення екземпляру класу ColorDot
    color_dot = ColorDot(3, 4, "red")
    color_dot.display()
    color_dot.set_color("blue")
    color_dot.set_coordinates(7, 8)
    color_dot.display()

    print("---")

    # Створення ColorDot за замовчуванням
    default_color_dot = ColorDot()
    default_color_dot.display()
