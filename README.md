# UoA-NLP
This is a summary on how to run the work done on this project and alter the parameters.

## Dependencies
- Python3
- NLTK, don't forget to run nltk.download('popular') to install popular resources
- PostgreSQL and the python driver psycopgl
- scikit-learn for Machine Learning
- gensim for LDA/LSA
- Optional:
    - IPython (IPyKernel, Jupyter) for LDA visualisation
    - pandas and redis for the recommender

The project needs a postgresql server running a specific database,
which creation and population scripts are available on the VM under /data/uoa-xero-db/.
The Configuration.py in the Database module should also be modified correctly.

## Usage
### Running the algorithms
the main scripts are located at the root of the repository.
To run the classifier and a clustering algorithm:

```python break_classify.py [algorithm]```

where [algorithm] is one of the implemented clustering algorithms.
At the present time, it can be dbscan, hierarchical,

### Customizing the parameters