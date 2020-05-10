import logging
import spacy
from flask import current_app
import os

logger = logging.getLogger(__name__)

# Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')
# nlp = en_core_web_sm.load()
stopwords = spacy.lang.en.stop_words.STOP_WORDS


# Function to preprocess text
def lemmatize(text):

    # Create Doc object
    doc = nlp(text, disable=['ner', 'parser'])
    # Generate lemmas
    lemmas = [token.lemma_ for token in doc]
    # Remove stopwords and non-alphabetic characters
    a_lemmas = [lemma for lemma in lemmas
                if lemma.isalpha() and lemma not in stopwords]

    return ' '.join(a_lemmas)


# Returns number of proper nouns
def pos_tag(text):
    doc = nlp(text)

    result = [(ent.text, ent.pos_) for ent in doc]

    logger.debug("result: {}".format(result))

    return result


def extract_ent(text):
    """
    accepts list contains texts

    :param text:
    :return:
    """
    doc = nlp(text)

    result = [(ent.text, ent.label_) for ent in doc.ents]

    logger.debug("result: {}".format(result))

    return result

def read_txt_file(filename):

    file_with_path = os.path.join(current_app.config['UPLOAD_TXT_FOLDER'], filename)

    with open(file_with_path, 'r') as txt_file:
        lines = txt_file.readlines()

    return lines
