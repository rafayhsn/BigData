# BigData

The primary objective of this project was to create a search engine capable of retrieving documents based on their relevance to a user-provided query. To achieve this, we implemented several key components, including Word Enumeration, Document Word Count, TF-IDF calculation, Ranking, and Searching.
Report: Implementation of a TF-IDF-based Search Engine


The task was to create a search engine capable of retrieving documents based on their relevance to a user-provided query. To achieve this, we implemented several key components, including Word Enumeration, Document Word Count, TF-IDF calculation, Ranking, and Searching.

1.The first step involved enumerating unique words in the document corpus and calculating the frequency of each word within each document. This process provided the foundational data required for subsequent TF-IDF calculation.

2.TF-IDF is a numerical statistic used to reflect the importance of a word in a document relative to a collection of documents. In this project, we computed TF-IDF scores for each term-document pair, capturing both the frequency of a term in a document (TF) and its rarity across the entire corpus (IDF).

3.Once TF-IDF scores were computed for each document-term pair, we implemented a ranking algorithm to sort documents based on their relevance to a given query. Documents with higher TF-IDF scores, indicating a stronger association with the query terms, were ranked higher in the search results.

4.The final step involved searching the corpus for documents containing the relevant query terms. Leveraging the TF-IDF scores computed during the ranking phase, we identified and returned documents deemed most relevant to the user's query.

The implemented search engine demonstrated promising performance in retrieving relevant documents from the corpus. By leveraging TF-IDF scores, the engine effectively ranked documents based on their relevance to the user query, enabling more accurate and targeted search results.
