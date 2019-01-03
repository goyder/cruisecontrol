from tests.context import world
import unittest
import nose


class TestWorld(unittest.TestCase):
    """
    Tests for cruisecontrol.world.
    """
    def test_the_world(self):
        the_world = world.World()

