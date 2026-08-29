class Rectangle:
    """Representa una figura geométrica rectangular."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self) -> int:
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def get_perimeter(self) -> int:
        """Calcula el perímetro del rectángulo."""
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        """Calcula la diagonal del rectángulo."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        """Dibuja el rectángulo usando asteriscos.

        Retorna 'Too big for picture.' si alguna dimensión supera 50.
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        row = "*" * self.width + "\n"
        return row * self.height

    def get_amount_inside(self, shape) -> int:
        """Calcula cuántas veces cabe otra figura dentro del rectángulo."""
        width_count = self.width // shape.width
        height_count = self.height // shape.height
        return width_count * height_count

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """Representa una figura geométrica cuadrada, heredando de Rectangle."""

    def __init__(self, side: int):
        super().__init__(side, side)

    def set_side(self, side: int):
        self.width = side
        self.height = side

    def set_width(self, width: int):
        self.set_side(width)

    def set_height(self, height: int):
        self.set_side(height)

    def __str__(self) -> str:
        return f"Square(side={self.width})"


if __name__ == "__main__":
    # Ejemplo de uso estándar de freeCodeCamp
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.diagonal) if hasattr(sq, 'diagonal') else print(sq.get_diagonal())
    print(sq)

    rect.set_picture_dim = Rectangle(15, 10)
    print(rect.get_picture())

    rect.set_width(16)
    rect.set_height(14)
    sq2 = Square(4)
    print(rect.get_amount_inside(sq2))