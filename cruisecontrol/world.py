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
        self.time = 0

    def add_object(self, world_object):
        """
        Add an object to the world.
        :param world_object: An instance of the class WorldObject.
        :return:
        """
        self.objects.append(world_object)

    def tick(self):
        """
        Make time pass in the world.
        :return:
        """
        for world_object in self.objects:
            world_object.tick(self.tick_length)
        self.time += self.tick_length


class WorldObject(abc.ABC):
    """
    General abstract base class for objects that will function within the world.
    """

    @abc.abstractmethod
    def tick(self, tick_length):
        """
        Let one unit of time pass.
        :return:
        """
        pass


class Clock(WorldObject):
    """
    A clock.
    Goes tick tick tick.
    Useful for tracking the passing of time.
    """
    def __init__(self):
        self.time = 0

    def tick(self, tick_length):
        self.time += tick_length


class Car(WorldObject):
    """
    A car.
    """
    def __init__(self, environment=None, velocity=0, acceleration=0, accelerator_pos=0, min_power=0, max_power=10000, area=2,
                 drag_coefficient=0.5, air_density=1.20, mass=1000, horizontal_displacement=0, ):
        self.velocity = velocity  # m/s, parallel to the road surface
        self.acceleration = acceleration  # m/s^2
        self.horizontal_displacement = horizontal_displacement  # m
        self.accelerator_pos = accelerator_pos  # [0-1]
        self.min_power = min_power  # kW
        self.max_power = max_power  # kW
        self.area = area  #m^2
        self.drag_coefficient = drag_coefficient  # unitless
        self.air_density = air_density  # kg/m^3
        self.mass = mass  # kg

        self.environment = environment

    def tick(self, tick_length):
        pass

    @property
    def power_output(self):
        return self.min_power + self.accelerator_pos * (self.max_power - self.min_power)
