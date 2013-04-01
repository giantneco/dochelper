#!/usr/bin/env python
# -*- coding: utf-8 -*-

import main
import unittest

class TestPlainTextFrontEnd(unittest.TestCase):

    def test_construct(self):
        """
        最初のテスト

        Arguments:
        - `self`:
        """
        
        frontend = PlainTextFrontEnd("test.txt")
        self.assertEqual(frontend.file, "test.txt")
