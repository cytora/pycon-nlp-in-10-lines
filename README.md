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

If you are using the Miniconda release of Python, you can use [conda virtual environments](http://conda.pydata.org/docs/using/envs.html) so your virtual environment setup will be slightly different. 

	conda create --name venv python=3
	source activate venv

To install all the required Python dependencies needed in this tutorial, you need to run this command in the cloned directory:

    pip install -r requirements.txt

To install the spaCy model you need to run:

    sputnik --name spacy --repository-url http://index.spacy.io install en==1.1.0

To run jupyter notebook run:

    jupyter notebook

The solution to the tutorial notebook for the workshop can  be found in [`tutorial.ipynb`](tutorial.ipynb) in this branch.

