import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import nltk

nltk.download('stopwords')

def clean_text(text):
    if isinstance(text, str):
        scores = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')', '[', ']', '{', '}', '@', '#', '$', '%', '&']
        text = text.lower()

        for score in scores:
            text = text.replace(score, '')

        parts = text.split()
        text = ' '.join([part for part in parts if not part.startswith('http://') and not part.startswith('www.')])

        parts = text.split()
        text = ' '.join([parte for parte in parts if not parte.startswith('@')])

        parts = text.split()
        text = ' '.join([parte for parte in parts if not parte.startswith('#')])

        text = ''.join([caracter for caracter in text if not caracter.isdigit()])

        text = ' '.join(text.split())

    return text


data = pd.read_csv('train.csv', encoding='ISO-8859-1')
data['selected_text'] = data['selected_text'].apply(clean_text)
data['selected_text'].fillna('', inplace=True)
data['sentiment'] = data['sentiment'].apply(lambda x: 0 if x == 1 else x)

X_train, X_test, y_train, y_test = train_test_split(data['selected_text'], data['sentiment'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
classifier = LogisticRegression()
classifier.fit(X_train_vectorized, y_train)
y_pred = classifier.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, y_pred)

print(f'Resultado: {accuracy * 100:.2f}%')
