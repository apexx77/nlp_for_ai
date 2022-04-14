# Basics of Natural Language Processing
### Table of Contents
1. [Installations](#installations)
2. [CoNLL Shared Tasks](#conll)
3. [Training the model](#model)
4. [Word Embeddings](#embeddings)

## <a name="installations"></a> Installations

You can install various resources that are used in the repository in this section.

- [CRF++ Tool](https://taku910.github.io/crfpp/#download)
    - To test whether the CRF++ tool is installed properly, try to run the command `crf_learn.exe` in the command line.
- Datasets
    - Chunking
        - [Training](https://www.clips.uantwerpen.be/conll2000/chunking/train.txt.gz)
        - [Testing](https://www.clips.uantwerpen.be/conll2000/chunking/test.txt.gz)
    - Named Entity Recognition
        - [Spanish and Dutch](https://www.clips.uantwerpen.be/conll2002/ner/data/)
        - [English and German](https://www.clips.uantwerpen.be/conll2003/ner.tgz)
    - POS Tagging
        - This dataset can be obtained from the dataset that was used for Chunking.
        - We have to write a simple program that removes the last column of the dataset to extract the dataset for POS Tagging.



## <a name="conll"></a> CoNLL Shared Tasks
You can find all the shared tasks of CoNLL [here](https://www.conll.org/previous-tasks)

## <a name="model"></a> Training the model

- We can train the CRF++ model for POS Tagging, Chunking and Named Entity Recognition by the below commands.
- This training certainly depends on the training data, the template and the testing data.
- Firstly, prepare a template that can train the model efficiently.
- Next, to train the model, navigate to the folder in which Training, Testing datasets are present and also template.
- Execute the Command ``` crf_learn <template_name> <training_data> <model_name> ```
- This creates a model with name `model_name`. 
- Our model is created. Now we should test the model with the testing datset and output the results to a new file.
- Execute the Command ``` crf_test -m <model_name> <testing_data> > <output_file> ```
- This creates a file named `output_file`
- To check the efficiency of the output, we can write a Python/Perl script that does the task.
- To use the standard Perl Script of CONLL, execute the command ``` perl conlleval -d "\t" < <output_file> ```
- This gives us the efficiency of the output.


## <a name="embeddings"></a> Word Embeddings

Embeddings translate large sparse vectors into a lower-dimensional space that preserves semantic relationships.
Word embeddings is a technique where individual words of a domain or language are represented as real-valued vectors in a lower dimensional space.
Sparse Matrix problem with BOW is solved by mapping high-dimensional data into a lower-dimensional space. Word embeddings are considered to be one of the successful applications of unsupervised learning at present. They do not require any annotated corpora. Embeddings use a lower-dimensional space while preserving semantic relationships.

There are 3 Models known for Word Embeddings :
 - Word2Vec-Skipgram Model
    - Word2vec is an algorithm invented at Google for training word embeddings. word2vec relies on the distributional hypothesis. The distributional hypothesis states that words which, often have the same neighboring words tend to be semantically similar. This helps to map semantically similar words to geometrically close embedding vectors.
    - Skip gram does not predict the current word based on the context instead it uses each current word as an input to a log-linear classifier with continuous projection layer, and predict words within a certain range before and after the current word.
 - Word2Vec-CBOW Model(Continuous Bag of Words)
    - Word2Vec models are shallow neural network with an input layer, a projection layer and an output layer. It is trained to reconstruct linguistic contexts of words. 
    - Input layer for Word2vec neural network takes a larger corpus of text to produce a vector space, typically of several hundred dimensions. 
    - Every unique word in the text corpus is assigned a corresponding vector in the space. This architecture is called continuous bag of words CBOW as it uses continuous distributed representation of the context. 
    -  It considers both the order of words in the history as well as future. This helps common context word vectors in the corpus to be located close to one another in the vector space.
 - GloVe Model(Global Vectors)
    - GloVe was developed by Pennington, et al. at Stanford. It is called Global Vectors as the global corpus statistics are captured directly by the model.
    - It leverages both Global matrix factorization methods like latent semantic analysis (LSA) for generating low-dimensional word representations and Local context window methods such as the skip-gram model of Mikolov et al


