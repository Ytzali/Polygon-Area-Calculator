import pytest
from shape_calculator import Rectangle, Square


def test_rectangle_basic_calculations():
    """Prueba el cálculo de área, perímetro y diagonal de un rectángulo."""
    rect = Rectangle(4, 5)
    assert rect.get_area() == 20
    assert rect.get_perimeter() == 18
    assert rect.get_diagonal() == (4 ** 2 + 5 ** 2) ** 0.5


def test_rectangle_str_representation():
    """Prueba la representación en cadena de Rectangle."""
    rect = Rectangle(3, 6)
    assert str(rect) == "Rectangle(width=3, height=6)"


@pytest.mark.parametrize(
    "width,height,expected",
    [
        (2, 2, "**\n**\n"),
        (3, 1, "***\n"),
        (1, 3, "*\n*\n*\n"),
    ],
)
def test_rectangle_get_picture_small(width, height, expected):
    """Prueba la salida gráfica de get_picture para rectángulos pequeños."""
    rect = Rectangle(width, height)
    assert rect.get_picture() == expected


def test_rectangle_get_picture_too_big():
    """Verifica que se retorne el mensaje límite cuando excede 50 de ancho o alto."""
    rect1 = Rectangle(51, 10)
    rect2 = Rectangle(10, 51)
    rect3 = Rectangle(51, 51)
    
    assert rect1.get_picture() == "Too big for picture."
    assert rect2.get_picture() == "Too big for picture."
    assert rect3.get_picture() == "Too big for picture."


def test_rectangle_get_amount_inside():
    """Prueba cuántas veces cabe una figura dentro de otra."""
    rect = Rectangle(10, 10)
    sq = Square(3)
    other_rect = Rectangle(2, 5)

    assert rect.get_amount_inside(sq) == 9  # (10//3) * (10//3) = 3 * 3 = 9
    assert rect.get_amount_inside(other_rect) == 10  # (10//2) * (10//5) = 5 * 2 = 10


def test_square_inheritance_and_properties():
    """Verifica herencia y métodos básicos de Square."""
    sq = Square(5)
    assert isinstance(sq, Square)
    assert isinstance(sq, Rectangle)
    assert issubclass(Square, Rectangle)

    assert sq.get_area() == 25
    assert sq.get_perimeter() == 20
    assert sq.get_diagonal() == (5 ** 2 + 5 ** 2) ** 0.5
    assert str(sq) == "Square(side=5)"


def test_square_setters_maintain_shape():
    """Comprueba que actualizar cualquier lado modifique ambos por igual."""
    sq = Square(4)
    
    sq.set_side(7)
    assert sq.width == 7
    assert sq.height == 7
    assert str(sq) == "Square(side=7)"

    sq.set_width(10)
    assert sq.width == 10
    assert sq.height == 10

    sq.set_height(3)
    assert sq.width == 3
    assert sq.height == 3


@pytest.mark.parametrize(
    "side,expected_area,expected_perimeter",
    [
        (1, 1, 4),
        (5, 25, 20),
        (12, 144, 48),
    ],
)
def test_square_parametrized_dimensions(side, expected_area, expected_perimeter):
    """Evalúa múltiples dimensiones y perímetros para cuadrados usando parametrize."""
    sq = Square(side)
    assert sq.get_area() == expected_area
    assert sq.get_perimeter() == expected_perimeter