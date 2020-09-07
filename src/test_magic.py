#!/usr/bin/env python3
import unittest

import magic


class TestMagic(unittest.TestCase):
    def test_magic(self):
        for n in range(3, 20):
            self.assertTrue(magic.is_magic(magic.generate(n)))


if __name__ == '__main__':
    unittest.main()
