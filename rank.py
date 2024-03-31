import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RankerEngine:
    def __init__(self, index_file):
        self.index = self.load_index(index_file)

    def load_index(self, index_file):
        index = {}
        with open(index_file, 'r') as f:
            for line in f:
                term, doc_id, tfidf = line.strip().split('\t')
                if term not in index:
                    index[term] = {}
                index[term][doc_id] = float(tfidf)
        return index

    def query_vectorizer(self, query):
        query_vector = {}
        words = query.split()
        for word in words:
            if word in self.index:
                query_vector[word] = 1  # Using binary weighting for simplicity
        return query_vector

    def calculate_tf_idf_query(self, query_vector):
        tfidf_query = {}
        num_docs = len(self.index.values())
        for term, doc_dict in self.index.items():
            df = len(doc_dict)
            idf = np.log(num_docs / df)
            tfidf_query[term] = query_vector.get(term, 0) * idf
        return tfidf_query

    def rank_documents(self, query, top_n=10):
        query_vector = self.query_vectorizer(query)
        tfidf_query = self.calculate_tf_idf_query(query_vector)

        relevance_scores = {}
        for doc_id in set.union(*[set(doc_dict.keys()) for doc_dict in self.index.values()]):
            doc_vector = {term: doc_dict.get(doc_id, 0) for term, doc_dict in self.index.items()}
            relevance_scores[doc_id] = cosine_similarity([list(tfidf_query.values())], [list(doc_vector.values())])[0][0]

        sorted_docs = sorted(relevance_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
        return sorted_docs

ranker = RankerEngine("tfdifout")
relevant_docs = ranker.rank_documents("query text")
print(relevant_docs)

