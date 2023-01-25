class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width
        return self.width

    def set_height(self, new_height):
        self.height = new_height
        return self.height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        picture = ""
        if self.width < 50 and self.height < 50:
            for lines in range(0, self.height):
                picture += "*" * self.width + "\n"
            return picture

        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        if hasattr(shape, 'side') == True:
            amount= (self.width/(getattr(shape, 'side'))) * (self.height/(getattr(shape, 'side')))
            return int(amount)
        else:
            amount= (self.width/(getattr(shape, 'width'))) * (self.height/(getattr(shape, 'height')))
            return int(amount)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        self.side = side

    def set_side(self, new_side):
        self.side = new_side

    def set_width(self, new_width):
        self.side = new_width
        return self.side

    def set_height(self, new_height):
        self.side = new_height
        return self.side

    def get_area(self):
        return (self.side * self.side)

    def get_perimeter(self):
        return (2 * self.side + 2 * self.side)

    def get_diagonal(self):
        return ((self.side ** 2 + self.side ** 2) ** .5)

    def get_picture(self):
        picture = ""
        if self.side < 50:
            for lines in range(0, self.side):
                picture += "*" * self.side + "\n"
            return picture

        else:
            return "Too big for picture."


    def __str__(self):
        return f"Square(side={self.side})"
