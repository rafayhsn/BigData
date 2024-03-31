#!/usr/bin/env python

from __future__ import division, print_function
import sys
import os
from collections import defaultdict
import math

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    # Get input paths from command line arguments
    input_paths = sys.argv[1:-1]
    output_path = sys.argv[-1]

    # Create dictionary to store word counts per file
    word_counts = defaultdict(list)

    # Find the total number of files
    total_files = len(input_paths)

    # Process input files
    for input_path in input_paths:
        filename = os.path.split(input_path)[-1]

        with open(input_path, 'r') as f:
            for words in read_input(f):
                for word_freq in words:
                    word, freq = word_freq.split('=')
                    word_counts[word].append((filename, float(freq)))

    # Calculate IDF
    idf_values = {}
    for word, file_list in word_counts.items():
        num_docs = len(file_list)
        idf_values[word] = math.log10(1 + (total_files / num_docs))

    # Calculate TFIDF and write output
    with open(output_path, 'w') as output_file:
        for word, file_list in word_counts.items():
            for filename, freq in file_list:
                tfidf = freq * idf_values[word]
                output_file.write('{}#####{}{}{}\n'.format(word, filename, separator, tfidf))

if __name__ == "__main__":
    main()
