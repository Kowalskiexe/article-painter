#!/usr/bin/env python3

import unittest
from articlepainter import remove_color_tag

class TestRemoveColorTag(unittest.TestCase):

    def test_romove_color_tag_simple(self):
        text = '<span color="#ff0000">some text</span>'
        output = remove_color_tag(text)
        self.assertEqual(output, 'some text', 'Should be: some text')


if __name__ == '__main__':
    unittest.main()
