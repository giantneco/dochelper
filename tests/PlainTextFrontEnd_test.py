#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import main,TestCase

class TestPlainTextFrontEnd(TestCase):
    from dochelper.main import PlainTextFrontEnd

    def test_construct(self):
        """
        最初のテスト

        Arguments:
        - `self`:
        """
        frontend = PlainTextFrontEnd('test.txt')
        self.assertEqual(frontend.file, 'test.txt')

if __name__ == '__main__':
    main()
