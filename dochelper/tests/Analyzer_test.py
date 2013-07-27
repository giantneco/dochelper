#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import main,TestCase
from dochelper.main import Document
from dochelper.main import Tagger
from dochelper.main import EosAnalyzer

class TestEosAnalyzer(TestCase):

    def test_tagging_one_sentence_end_with_verb(self):
        """
        EosAnalyzer は文末が助動詞で終わるセンテンスに警告を出さない。
        """

        doc = Document()
        doc.appendSentence(u'これはペンです。')

        tagger = Tagger()
        tagger.tagDoc(doc)

        an = EosAnalyzer()
        results = an.analyze(doc)

        self.assertEqual(len(results), 0)

    def test_tagging_one_sentence_with_auxiliay_verb(self):
        """
        EosAnalyzer は文末が動詞で終わるセンテンスに警告を出さない。
        """

        doc = Document()
        doc.appendSentence(u'あなたはペンをもつ。')

        tagger = Tagger()
        tagger.tagDoc(doc)

        an = EosAnalyzer()
        results = an.analyze(doc)

        self.assertEqual(len(results), 0)

    def test_tagging_one_sentence(self):
        """
        EosAnalyzer は文末が名詞で終わるセンテンスに警告を出す。
        """

        doc = Document()
        doc.appendSentence(u'これはペン。')

        tagger = Tagger()
        tagger.tagDoc(doc)

        an = EosAnalyzer()
        results = an.analyze(doc)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].content, u'これはペン。')
