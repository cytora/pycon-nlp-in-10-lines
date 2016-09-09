### PyCon UK 2016 
![NLP in 10 Lines of Code](images/displacy_title.png)
# Natural Language Processing in 10 Lines of Code
##### from Andraz Hribernik, Matic Horvat, Aeneas Wiener, Tom Sherborne

At [Cytora](http://www.cytora.com) we use NLP to extract and analyse plain text to build our structured information product.

This is the repo for [our workshop at PyCon UK](http://2016.pyconuk.org/workshops/natural-language-processing-in-10-lines-of-code/).
In this repository you will find the step by step tutorial from the workshop on some basic Natural Language Processing tasks using [spaCy](http://spacy.io/),
a powerful (and super fast) NLP library.

## Getting started
Clone this repo from GitHub and open the directory, on a UNIX machine these actions will look like this.

	git clone git@github.com:cytora/pycon-nlp-in-10-lines.git
	cd pycon-nlp-in-10-lines

We recommend you to install all the required dependencies in a virtual environment such as [virtualenv](https://virtualenv.pypa.io/en/stable/), however this step could be skipped.

    virtualenv -p python3 venv
    source venv/bin/activate

If you are using the Miniconda release of Python, you can use [conda virtual environments](http://conda.pydata.org/docs/using/envs.html) so your virtual environments will be slightly different.

	conda create --name venv python=3
	source activate venv

To install all the required Python dependencies needed in this tutorial, you need to run this command in the cloned directory:

    pip install -r requirements.txt

To install the spaCy model you need to run:

    sputnik --name spacy --repository-url http://index.spacy.io install en==1.1.0

To run jupyter notebook run:

    jupyter notebook

Tutorial notebook could be found in [`tutorial.ipynb`](tutorial.ipynb).

## Common terms in NLP

#### Token

A token is a single chopped up element of the sentence, which could be a word or a group of words to analyse. The task of chopping the sentence up is called "tokenisation".

Example: The following sentence can be tokenised by splitting up the sentence into individual words.

	"Cytora is going to PyCon!"
	["Cytora","is","going","to","PyCon!"]

#### Corpus

A corpus (plural: corpora) is a large collection of text or documents. A corpus might be built from transcribed speech or a collection of manuscripts. Corpora provide useful training data for NLP models. Each item in a corpus is not necessarily unique and frequency counts of words can assist in uncovering the structure in a corpus.

Examples:

1. Every word written in the complete works of Shakespeare
2. Every word spoken on BBC Radio channels for the past 30 years 

#### Speech Tag

A speech tag is a context sensitive description of what a word means in the context of the whole sentence.
More information about the kinds of speech tags which are used in NLP can be [found here](http://www.winwaed.com/blog/2011/11/08/part-of-speech-tags/).

Examples:

1. CARDINAL, Cardinal Number - 1,2,3
2. PROPN, Proper Noun, Singular - "John", "Andraz", "Cardiff"
3. INTJ, Interjection - "Uhhhhhhhhhhh"

#### Noun Chunk

Noun chunks are the phrases based upon nouns recovered from tokenized text using the speech tags.

Example:

The sentence "The boy saw the yellow dog" has 2 noun objects, the boy and the dog. 
Therefore the noun chunks will be

	1. "The boy"
	2. "the yellow dog"

#### Named Entities

A named entity is any real world object such as a person, location, organisation or product with a proper name. 

Example:

	1. Barack Obama
	2. Edinburgh
	3. Ferrari Enzo

#### Word Embeddings

A word embedding is a representation of a word, and by extension a whole language corpus, in a vector or other form of numerical mapping. This allows words to be treated numerically with word similarity represented as spatial difference in the dimensions of the word embedding mapping.

Example:
	
With word embeddings we can understand that vector operations describe word similarity. This means that we can see vector proofs of statements such as:

	king-queen==man-woman


#### Stop Words

Stop words are the common words in a vocabulary which are of little value when considering word frequencies in text. This is because they don't provide much useful information about what the sentence is telling the reader.

Example: _"the","and","a","are","is"_


