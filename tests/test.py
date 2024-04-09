from main import main
import unittest

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello 10x!")
        print("Test passed")

if __name__ == "__main__":
    unittest.main()