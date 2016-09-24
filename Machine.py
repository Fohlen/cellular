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
        for coordinate in self._room._space.keys():
            neighbours = self._room.neighbours(coordinate)
            if len(neighbours) > 2 or len(neighbours) > 3:
                self._room.killCell(coordinate)
            elif len(neighbours) == 2 or len(neighbours) == 3:
                pass
            elif len(neighbours) == 3 and this._room.getCellColor(coordinate) == Color.black: # if dead
                self._room.spawnCell(coordinate)

    def __str__(self):
        """Returns a string representation of a machine"""
        # TODO: This is a bit performance-consuming
        bord = this._room.border
        str = ''
        while (bord % 2) > 0 or bord > this._room.border: # Find the next matching number for 2 sane rasters
            bord = bord - 1

        for x in range(bord / 2):
            for y in range(bord / 2):
                # Implement
        return str
