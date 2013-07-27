#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import main,TestCase
from dochelper.main import PlainTextFrontEnd

class TestPlainTextFrontEnd(TestCase):

    def test_parse_one_line(self):
        """
        1 センテンスを含む文字列を読み込んで 1 センテンスを返す。
        """

        frontend = PlainTextFrontEnd()
        frontend.append(u'これはペンです。')
        doc = frontend.parse()
        self.assertEqual(len(doc), 1)
        self.assertEqual(doc[0].content, u'これはペンです。')

    def test_parse_two_sentences(self):
        """
        2 センテンスを含む文字列を読み込んで 2 センテンスを返す。
        """

        frontend = PlainTextFrontEnd()
        frontend.append(u'これはペンです。それは犬です。')
        doc = frontend.parse()
        self.assertEqual(len(doc), 2)
        self.assertEqual(doc[0].content, u'これはペンです。')
        self.assertEqual(doc[1].content, u'それは犬です。')

    def test_parse_truncated_one_sentence(self):
        """
        折り返しされた 1 センテンスを含む文字列を読み込んで 1 センテンスを返す。
        """

        frontend = PlainTextFrontEnd()
        frontend.append(u'これは\nペンです。')
        frontend.parse()
        doc = frontend.parse()
        self.assertEqual(len(doc), 1)
        self.assertEqual(doc[0].content, u'これはペンです。')

if __name__ == '__main__':
    main()
