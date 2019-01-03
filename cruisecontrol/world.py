"""
world.py

Contains the core container for the "world".
The "world" contains the elements of the simulation.
It is responsible for holding them and making sure everything goes tick.
"""

import abc


class World:
    """
    This is the World.
    It hold things and it makes those things go tick.
    """

    def __init__(self, tick_length=0.001):
        """
        :param tick_length: The length of time in seconds that a tick equates to.
        """
        self.tick_length = tick_length
        self.objects = []

    def add_object(self, world_object):
        """
        Add an object to the world.
        :param world_object: An instance of the class WorldObject.
        :return:
        """



class WorldObject(abc.ABC):
    @abc.abstractmethod
    def tick(self):
        """
        Let one unit of time pass.
        :return:
        """
        pass

class Clock(WorldObject):
    """
    A clock!
    """
    def tick(self):
        print("Tick!")