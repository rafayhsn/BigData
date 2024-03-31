class ContentExtractor:
    def __init__(self, corpus):
        self.corpus = corpus

    def extract_content(self, relevant_ids):
        relevant_content = []
        for doc_id in relevant_ids:
            relevant_content.append(self.corpus.get(doc_id, "Document not found"))
        return relevant_content


