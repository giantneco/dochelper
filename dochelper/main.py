#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import MeCab

class Sentence:
    """
    Represents single sentence.
    """

    def __init__(self, string):
        self.content = string
        self.tagged = False
        self.tags = None

    def tag(self, value):
        """
        Tags to this sentence.
        """
        self.tags = value
        self.tagged = True

    def printTags(self):
        for tag in self.tags:
            self._printTag(tag)

    def _printTag(self, tag):

        # surface
        print tag[0], ",",
        # features
        for feature in tag[1]:
            print feature, ",",
        # cost
        print tag[2]

class Document:
    """
    represent document

    """

    def __init__(self):
        """
        
        Arguments:
        - `self`:
        """
        self.sentences = []

    def __len__(self):
        return len(self.sentences)

    def __getitem__(self, key):
        return self.sentences[key]

    def appendSentence(self, content):
        self.sentences.append(Sentence(content))

    def sentences(self):
        for sentence in self.sentences:
            yield sentence

    def printTags(self):
        for sentence in self.sentences:
            sentence.printTags()

class PlainTextFrontEnd:
    """
    FrontEnd for Plain text.
    """

    def append(self, document, string):
        """
        append string to an internal document.

        Arguments:
        - `self`:
        - `string`:
        """
        if self.rest is None:
            target = string
        else:
            target = self.rest.encode('utf-8') + string
        splited = target.replace('\n', '').decode('utf-8').strip().split(u'。')
        for s in splited[0:-1]:
            if len(s):
                s = s + u'。'
                document.appendSentence(s)
        if target.endswith('。'):
            document.appendSentence(splited[-1])
            self.rest = None
        else:
            self.rest = splited[-1]

    def readFromFile(self, filename):
        """
        Translate file to Document

        - `filename`: the file to be traslated
        """
        doc = Document()
        with codecs.open(filename, 'r', 'utf-8') as plainText:
            for line in plainText:
                encoded = line.encode('utf-8')
                self.append(doc, encoded)
        if self.rest is not None:
            doc.appendSentence(self.rest)
        return doc

    def readStdin(self):
        """
        Traslate standard input to Document
        """
        doc = Document()
        plainText  = codecs.getreader('utf-8')(sys.stdin)
        for line in plainText:
            encoded = line.encode('utf-8')
            self.append(doc, encoded)
        if self.rest is not None:
            doc.appendSentence(self.rest)
        return doc

    def read(self, filename):
        self.rest = None
        if filename == "-":
            return self.readStdin()
        else:
            return self.readFromFile(filename)

class Tagger:
    """
    MeCab Tagger Wrapper
    """
    
    def __init__(self, ):
        self.tagger = MeCab.Tagger()
        
    def tagDoc(self, document):
        """
        Add tags to sentences in document.
        """
        for sentence in document.sentences:
            self.tagSentence(sentence)

    def tagSentence(self, sentence):
        """
        Add tags to sentence.
        """
        encoded = sentence.content.encode('utf-8')
        node = self.tagger.parseToNode(encoded)
        tags = []
        while node:
            if node.surface:
                surface = node.surface.decode('utf-8')
                features = node.feature.decode('utf-8').split(',')
                cost = node.cost
                tags.append((surface,features,cost))
            node = node.next
        sentence.tags = tags
        sentence.tagged = True

if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) < 2:
        print ("Usage: python %s filename" % argvs[0])
    fe = PlainTextFrontEnd()
    doc = fe.read(argvs[1])
    tagger = Tagger()
    tagger.tagDoc(doc)
    doc.printTags()
