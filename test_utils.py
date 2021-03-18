from unittest import TestCase

from utils import create_machine_state


class TestUtils(TestCase):
    
    def test_create_machine_state(self):
        expected = 100
        result = len(create_machine_state(100))
        self.assertEquals(expected, result)
