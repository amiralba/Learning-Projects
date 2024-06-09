class Circle:
    __diameter: int
    __filled: bool

    def __init__(self, diameter: int, filled = False):
        self.__diameter = diameter
        self.__filled = filled


    def draw(self):
        pixels_in_line: int = 0
        pixels_per_line: list[int] = []

        offset_radius = (self.__diameter / 2) - 0.5

        for i in range(self.__diameter):
            for j in range(self.__diameter):
                x = i - offset_radius
                y = j - offset_radius
                if x * x + y * y <= offset_radius * offset_radius + 1:
                    print('*', end='  ')
                    pixels_in_line += 1
                else:
                    print(' ', end='  ')
            pixels_per_line.append(pixels_in_line)
            pixels_in_line = 0
            print()

