#!/usr/bin/env python
import sys
import cPickle as pickle
import gzip

class Data(object):

    def __init__(self):
        self.i = -1

    # load compressed data from filename
    def load(self, filename):
        try:
            fp = gzip.GzipFile(filename, 'rb')
        except IOError:
            print >> sys.stderr, "failed to open file"
            return

        buff = ""
        while True:
            data = fp.read()
            if data == "":
                break
            buff += data

        try:
            self.vocab, self.pos, self.corpus = pickle.loads(buff)
        except IOError:
            print >> sys.stderr, "failed to open file."
            return

        self.i = 0

    # dump compressed data into filename
    def dump(self, filename):

        try:
            fpo = gzip.GzipFile(filename, "wb")
        except:
            print >> sys.stderr, "Failed to open file."
            return

        fpo.write(
                pickle.dumps(
                    (self.vocab, self.pos, self.corpus),
                    True))

        fpo.close()

    # compress the raw data into compressed data
    def compress(self, filename):
        try:
            fp=open(filename, "r")
        except:
            print >> sys.stderr, "Failed to open file"
            return

        vocabmap = {}
        posmap   = {}

        self.vocab  = []
        self.pos    = []
        self.corpus = []

        for line in fp:
            sentence = []

            for wordstr, posstr in [
                    word.rsplit("_") for word in line.strip().split()]:

                if wordstr not in vocabmap:
                    vocabmap[wordstr] = len(self.vocab)
                    self.vocab.append(wordstr)

                if posstr not in posmap:
                    posmap[posstr] = len(self.pos)
                    self.pos.append(posstr)

                sentence.append((vocabmap[wordstr], posmap[posstr]))

            self.corpus.append(sentence)

        self.i = 0
        fp.close()

    # iteration method
    def __iter__(self):
        for sentence in self.corpus:

            sentstr = ""
            words = []

            for word, pos in sentence:
                sentstr += self.vocab[word]
                words.append((
                    self.vocab[word], self.pos[pos]))

            yield sentstr, words

def test():
    d = Data()
    d.compress("corpus.small.raw")
    d.dump("corpus.small.db")
    d.load("corpus.small.db")

    for sent, words in d:
        print sent, words

def main():
    d = Data()
    d.compress(sys.argv[1])
    d.dump(sys.argv[2])

if __name__=="__main__":
    #test()
    main()
