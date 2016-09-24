from Coordinate import Coordinate
from Cell import Cell
from Color import Color

class Room:
    """ The room class describes the space and raster where cells belong to. R square is used"""
    def __init__(self, border = 100):
        self._space = {} # The room is an assigment of coordinate: cell
        self.border = border # The room's border. Can be changed
        self._lastCoordinate = Coordinate(1, 1)

    def add(self, coordinate, cell = Cell()):
        """Add a cell to the room."""
        if isinstance(coordinate, Coordinate):
            if coordinate not in self._space:
                if isinstance(cell, Cell):
                    self._space[coordinate] = cell
                else:
                    raise TypeError('Room should only be filled with cells')
            else:
                raise StandardError('Requested space is already taken.')
        else:
            raise TypeError('Cannot apply room operation with a non-coordinate.')

    def exists(self, coordinate):
        """Check wether a cell exists at given coordinate. Returns bool."""
        if isinstance(coordinate, Coordinate):
            return coordinate in self._space
        else:
            raise TypeError('Cannot apply room operation with a non-coordinate')

    def remove(self, coordinate):
        """Removes everything from given coordinate"""
        if self.exists(coordinate):
            del self._space[coordinate]
        else:
            raise StandardError('No cell found at specified coordinate')

    def getNextCoordinate(self):
        """Returns the next free coordinate"""
        # TODO: Cycle on removed coordinates (FIFO)
        # Right-to-left order incrementation
        while self.exists(self._lastCoordinate):
            if self._lastCoordinate[0] > self.border or self._lastCoordinate[1] > self.border:
                raise StandardError('Operating out of border')
            if self._lastCoordinate[0] > self._lastCoordinate[1]:
                self._lastCoordinate = Coordinate(self._lastCoordinate[0], self._lastCoordinate[1] + 1) # Increment y + 1
            elif self._lastCoordinate[0] == self._lastCoordinate[1]:
                self._lastCoordinate = Coordinate(self._lastCoordinate[0] + 1, 1) # Increment x + 1 AND reset y to 1

        return self._lastCoordinate

    def neighbours(self, coordinate):
        """Returns a list of neighbour cells (coordinates)"""
        if isinstance(coordinate, Coordinate):
            if self.exists(coordinate):
                coordinates = []

                for x in range(coordinate[0] - 1, coordinate[0] + 2):
                    for y in range(coordinate[0] - 1, coordinate[0] + 2):
                        if self.exists(Coordinate(x, y)):
                            cor = Coordinate(x, y)
                return coordinates
        else:
            raise TypeError('Cannot apply room operation with non-coordinate')

    def getCellColor(self, coordinate):
        """Returns the color of the cell at given coordinate"""
        if self.exists(coordinate):
            cell = self._space[coordinate]
            return cell.color

    def killCell(self, coordinate):
        """Kills a cell at given coordinate"""
        if self.exists(coordinate):
            cell = self._space[coordinate]
            cell.color = Color.black
            self._space[coordinate] = cell

    def spawn(self, coordinate):
        """Spawns or revives a cell at given coordinate"""
        if self.exists(coordinate):
            cell = self._space[coordinate]
            cell.color = Color.white
            self._space[coordinate] = cell
