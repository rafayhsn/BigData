import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

csv_file = "inputData.csv"  
df = pd.read_csv(csv_file, nrows=250000)

#Only keeping article_id and section text
df = df[['ARTICLE_ID', 'SECTION_TEXT']]

df.dropna(subset=['ARTICLE_ID', 'SECTION_TEXT'], inplace=True)

#Lowering the Text
df['SECTION_TEXT'] = df['SECTION_TEXT'].str.lower()

def remove_non_alphabetic(text):
    return re.sub(r'[^a-z\s]', '', text)

# Remove non-alphabetic characters from 'SECTION_TEXT'
df['SECTION_TEXT'] = df['SECTION_TEXT'].apply(remove_non_alphabetic)

# Remove '\n' characters from 'SECTION_TEXT'
df['SECTION_TEXT'] = df['SECTION_TEXT'].str.replace('\n', '')

df = df.groupby('ARTICLE_ID')['SECTION_TEXT'].apply(' '.join).reset_index()
