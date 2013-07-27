#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import main,TestCase
from dochelper.main import Document
from dochelper.main import Tagger

class TestTagger(TestCase):

    def test_tagging_one_sentence(self):
        """
        主語、助詞、名詞、述語、読点でなる 1 センテンスの document を読み込んでタギングする。
        """

        doc = Document()
        doc.appendSentence(u'これはペンです。')

        tagger = Tagger()
        tagger.tagDoc(doc)

        self.assertEqual(len(doc.sentence(0).tags), 5)

    
