#!/usr/bin/python3
"""Magic class from Python bytecode"""
import math


class MagicClass:
    """Initialization of the class"""
    def __init__(self, radius=0):
        """Initialization of data"""
        self.MagicClass__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Computes the area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference"""
        return 2 * math.pi * self._MagicClass__radius
