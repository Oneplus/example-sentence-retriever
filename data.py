#!/usr/bin/env python
import sys
import marshal
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
            self.corpus = marshal.loads(buff)
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

        fpo.write(marshal.dumps(
            self.corpus,
            True))

        fpo.close()

    # compress the raw data into compressed data
    def compress(self, filename):
        try:
            fp=open(filename, "r")
        except:
            print >> sys.stderr, "Failed to open file"
            return

        self.corpus = []
        for line in fp:
            words=[word.rsplit("_", 1) for word in line.strip().split()]
            sentence = "".join(word[0] for word in words)
            self.corpus.append((sentence, words))

        fp.close()

    # iteration method
    def __iter__(self):

        for sentence in self.corpus:
            yield sentence

def test():
    d = Data()
    d.compress("corpus.small.raw")
    d.dump("corpus.small.db")
    d.load("corpus.small.db")

    for sent, words in d:
        print sent
        print " ".join(
                ["%s(%s)" % (word[0], word[1]) for word in words])

def main():
    d = Data()
    d.compress(sys.argv[1])
    d.dump(sys.argv[2])

if __name__=="__main__":
    #test()
    main()
