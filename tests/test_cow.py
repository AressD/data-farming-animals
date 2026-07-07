import unittest
from farm.cow import Cow


class TestCow(unittest.TestCase):

    def setUp(self):
        self.cow = Cow()

    def test_initialize_sets_milk_to_zero(self):
        """Cow'un sütü 0 ile başlamalı."""
        self.assertEqual(self.cow.milk, 0)

    def test_initialize_sets_energy_to_zero(self):
        """Cow'un enerjisi 0 ile başlamalı."""
        self.assertEqual(self.cow.energy, 0)

    def test_feed_extends_method(self):
        """Cow'un feed metodu olmalı."""
        self.assertTrue(hasattr(self.cow, 'feed'))

    def test_feed_adds_milk(self):
        """Beslenince 2 litre süt eklenmeli."""
        self.cow.feed()
        self.assertEqual(self.cow.milk, 2)
        self.cow.feed()
        self.assertEqual(self.cow.milk, 4)

    def test_feed_adds_energy(self):
        """Beslenince enerji 1 artmalı."""
        self.cow.feed()
        self.assertEqual(self.cow.energy, 1)

    def test_talk_returns_moo(self):
        """talk 'moo' döndürmeli."""
        self.assertEqual(self.cow.talk(), "moo")