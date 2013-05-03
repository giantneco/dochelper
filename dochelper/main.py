#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

import MeCab

class PlainTextFrontEnd:
    """
    FrontEnd for Plain text.
    """

    def __init__(self):
        self.document = []
        pass

    def append(self, string):
        """
        append string to an intrnal document.

        Arguments:
        - `self`:
        - `string`:
        """
        for s in string.split(u'。'):
            if len(s):
                s = s.replace('\n', '')
                self.document.append(s + u'。')

    def parse(self):
        """
        parse an internal document.

        """
        pass

    def getDocument(self):
        """
        return an internal document.
        
        """
        return self.document

# if __name__ == '__main__':
#     argvs = sys.argv
#     if len(argvs) < 2:
#         print ("Usage: python %s filename" % argvs[0])
#     tagger = MeCab.Tagger()

#     with codecs.open(argvs[1], 'r', 'utf-8') as f:
#         for line in f:
#             encoded = line.encode('utf-8')
#             node = tagger.parseToNode(encoded)
#             while node:
#                 print (node.surface + '\t' + node.feature)
#                 node = node.next
