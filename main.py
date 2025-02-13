import string
from time import sleep


class SimplePipeline:
    def __init__(self):
        print("Pipeline initialisée.")

    def preprocess(self, text):
        """ Nettoie et tokenize le texte """
        text = text.lower()  # Minuscule
        text = text.translate(str.maketrans('', '', string.punctuation))  # Suppression ponctuation
        tokens = text.split()  # Tokenisation
        return tokens

# Test si exécuté directement
def main():
    pipeline = SimplePipeline()
    while True:
        print(pipeline.preprocess("Hello, World! Ceci est un TEST."))
        sleep(3)
