#!/usr/bin/env python3

import unittest
import _11


class WizText(unittest.TestCase):
    def test_travel_tower(self):
        wiz = _11.Wizard(location="village")
        self.assertEqual(
            wiz.task("tower"),
            "You travel to your modest one-story wizard tower."
            )

    def test_travel_tower_already_there(self):
        wiz = _11.Wizard(location="tower")
        self.assertEqual(
            wiz.task("tower"),
            "You are already in the tower, silly wizard!"
            )

if __name__=='__main__':
    unittest.main()
