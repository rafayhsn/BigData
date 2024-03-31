from mrjob.job import MRJob
import csv

class WordEnumerationAndDocWordCount(MRJob):

    def mapper_word_enum(self, _, line):
        article_id, text = line.split(',', 1)
        words = text.split()
        for word in words:
            yield word, 1

    def reducer_word_enum(self, word, counts):
        total_count = sum(counts)
        yield word, total_count

    def mapper_doc_word_count(self, _, line):
        article_id, text = line.split(',', 1)
        words = set(text.split())
        for word in words:
            yield word, 1

    def reducer_doc_word_count(self, word, counts):
        total_count = sum(counts)
        yield word, total_count

    def steps(self):
        return [
            self.mr(mapper=self.mapper_word_enum, reducer=self.reducer_word_enum),
            self.mr(mapper=self.mapper_doc_word_count, reducer=self.reducer_doc_word_count)
        ]

if __name__ == '__main__':
    WordEnumerationAndDocWordCount.run()

