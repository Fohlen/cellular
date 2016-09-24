from Room import Room
from Cell import Cell
from Coordinate import Coordinate
from Color import Color

class Machine:
    """A machine operates cells within a room according to it's neighbourhood-law"""
    def __init__(self):
        self._room = Room()

    def initialise(self, number):
        """Initialises a machine with a number of cells"""
        for index in range(number):
            coordinate = self._room.getNextCoordinate()
            cell = Cell()
            self._room.add(coordinate, cell)

    def cycle(self):
        """Cycles through the Automat according to Conways rules"""
        # Implements the rules of Conways Game of Life
        past_room = self._room # Calculate all operations on the expired room

        for coordinate in past_room._space.keys():
            neighbours = past_room.neighbours(coordinate)
            if len(neighbours) > 2 or len(neighbours) > 3:
                self._room.killCell(coordinate)
            elif len(neighbours) == 2 or len(neighbours) == 3:
                pass
            elif len(neighbours) == 3 and past_room.getCellColor(coordinate) == Color.black: # if dead
                self._room.spawnCell(coordinate)

    def __str__(self):
        """Returns a string representation of a machine"""
        # TODO: This is a bit performance-consuming
        border = self._room.border
        str = ''
        while (border % 2) > 0 or border > self._room.border: # Find the next matching number for 2 sane rasters
            border = border - 1

        columns = range(int(border / 2))
        first_colum = min(columns)

        def getSign(coordinate):
            if self._room.exists(coordinate):
                if self._room.getCellColor == Color.black:
                    return 'B'
                else:
                    return 'W'
            else:
                return 'N'

        for x in columns:
            if x is not first_colum:
                str = str + '\n' # Start a new line
            for y in columns:
                coordinate = Coordinate(x, y)
                if y is first_colum:
                    str = str + getSign(coordinate) + ' '
                else:
                    str = str + getSign(coordinate) + ' '

        return str.format()
