from tests.context import world
import unittest
import nose


class TestWorld(unittest.TestCase):
    """
    Tests for cruisecontrol.world.
    """

    #####################################
    # Creating the world
    #####################################

    def test_the_world(self):
        """
        Ensure that we can create the world.
        :return:
        """
        the_world = world.World()

    def test_world_created_with_nothing(self):
        """
        Create the world and check it has nothing to it.
        :return:
        """
        the_world = world.World()
        self.assertEqual(
            the_world.objects == [],
            True,
            "World was created with non-empty list of objects."
        )

    def test_time_passes_in_world(self):
        """
        When we tick tick tick, time should pass.
        :return:
        """
        the_world = world.World(tick_length=1)
        for _ in range(100):
            the_world.tick()

        self.assertEqual(
            the_world.time == 100,
            True,
            "Time in the world was not 100 seconds as expected."
        )

    ############################################
    # Interactions between the world and objects
    ############################################

    def test_create_world_and_add_clock(self):
        """
        Create the world, add a clock.
        :return:
        """
        the_world = world.World()
        the_world.add_object(world.Clock())

        self.assertEqual(
            len(the_world.objects) == 1,
            True,
            "Number of objects in the world did not equal 1 when clock was added."
        )

    # TODO(Goyder): Figure out what's going on with issubclass()
    @unittest.skip("Skip until I figure out what's going on with issubclass() and abc.ABC().")
    def test_world_rejects_non_world_object(self):
        """
        Create the world, add something that's not a world object, and ensure we get an error.
        :return:
        """
        the_world = world.World()
        with self.assertRaises(TypeError):
            the_world.add_object("I am not an instance of the WorldObject base class.")

    def test_clock_can_track_the_passing_of_time(self):
        """
        Create the world, add a clock, let time pass, and check the time.
        :return:
        """
        the_world = world.World(tick_length=1)
        clock = world.Clock()
        the_world.add_object(clock)

        for _ in range(100):
            the_world.tick()

        self.assertEqual(
            clock.time == 100,
            True,
            "Time on the clock did not equal 100. \nActual time: {}".format(clock.time)
        )

    def test_clock_can_track_the_passing_of_time_at_different_tick_lengths(self):
        """
        Create the world with a non-standard tick-length, let time pass, check the time.
        :return:
        """
        the_world = world.World(tick_length=0.001)
        clock = world.Clock()
        the_world.add_object(clock)

        for _ in range(1000):
            the_world.tick()

        self.assertEqual(
            clock.time - 1. < 1e-05,
            True,
            "Time on the clock did not equal 1. \nActual time: {}".format(clock.time)
        )


class TestCar(unittest.TestCase):
    """
    Tests to test the performance of a car.
    """

    def setUp(self):
        """
        :return:
        """
        self.car = world.Car()

    def test_min_power_output(self):
        min_power = 1000
        max_power = 10000
        accelerator_pos = 0
        assumed_power_output = 1000

        self.car = world.Car(min_power=min_power, max_power=max_power, accelerator_pos=accelerator_pos)

        self.assertAlmostEqual(
            self.car.power_output,
            assumed_power_output,
            "Actual car power output did not match assumed power output."
        )

    def test_mid_power_output(self):
        min_power = 1000
        max_power = 10000
        accelerator_pos = 0.5
        assumed_power_output = 5500

        self.car = world.Car(min_power=min_power, max_power=max_power, accelerator_pos=accelerator_pos)

        self.assertAlmostEqual(
            self.car.power_output,
            assumed_power_output,
            "Actual car power output did not match assumed power output."
        )

    def test_max_power_output(self):
        min_power = 1000
        max_power = 10000
        accelerator_pos = 0
        assumed_power_output = 1000

        self.car = world.Car(min_power=min_power, max_power=max_power, accelerator_pos=accelerator_pos)

        self.assertAlmostEqual(
            self.car.power_output,
            assumed_power_output,
            "Actual car power output did not match assumed power output."
        )


class TestRoad(unittest.TestCase):
    """
    Tests to assess the performance of a road.
    """

    def test_implementation_of_flat_road(self):
        """
        Test to instantiate a road.
        Returns:
        """
        self.road = world.FlatRoad()

    def test_angle_of_flat_road(self):
        """
        Test to ensure the flat road is indeed flat.
        Returns:
        """
        self.flatroad = world.FlatRoad()
        self.assertAlmostEqual(
            self.flatroad.angle(0),
            0,
            msg="Road is indeed flat."
        )

