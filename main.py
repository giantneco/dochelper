#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

import MeCab

if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) < 2:
        print 'Usage: python %s filename' % argvs[0]
    tagger = MeCab.Tagger()

    with codecs.open(argvs[1], 'r', 'utf-8') as f:
        for line in f:
            encoded = line.encode('utf-8')
            node = tagger.parseToNode(encoded)
            while node:
                print node.surface + '\t' + node.feature
                node = node.next
