# ## Learning Unit 3

## Learning Unit 3: Natural Language Processing and Word Embeddings
- Objectives:
  * Understand the basics of natural language processing (NLP)
  * Grasp the concept of word embeddings
- Topics:
  * Introduction to NLP
  * Word embeddings and Word2Vec
  * Applications of NLP in Tetum and Portuguese languages
- Activities:
  * Experiment with word embeddings using a pre-trained model
  * Discussion on potential NLP applications for preserving Timorese languages and culture

## Unit Resources

Here are detailed resources for Learning Unit 3: Natural Language Processing and Word Embeddings, formatted in Markdown:

# Resources for Learning Unit 3: Natural Language Processing and Word Embeddings

## 1. Lecture Notes

### Introduction to NLP

Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and human language. It involves developing algorithms and models that enable computers to understand, interpret, and generate human language in a valuable way.

Key components of NLP:
1. Tokenization: Breaking text into individual words or subwords
2. Part-of-speech tagging: Assigning grammatical categories to words
3. Named Entity Recognition: Identifying and classifying named entities in text
4. Syntactic parsing: Analyzing the grammatical structure of sentences
5. Semantic analysis: Extracting meaning from text

Challenges in NLP:
- Ambiguity in language
- Contextual understanding
- Handling multiple languages and dialects
- Dealing with informal language and slang

### Word Embeddings and Word2Vec

Word embeddings are learned representations of text where words with similar meanings have similar representations. They are typically represented as dense vectors in a high-dimensional space.

Advantages of word embeddings:
- Capture semantic relationships between words
- Enable mathematical operations on words
- Improve performance in various NLP tasks

Word2Vec:
- Popular algorithm for generating word embeddings
- Two main architectures: Continuous Bag of Words (CBOW) and Skip-gram
- Learns to predict a word given its context or vice versa

How Word2Vec works:
1. Initialize random vectors for each word in the vocabulary
2. Slide a window over the text corpus
3. For each window, predict the target word from context words (CBOW) or context words from the target word (Skip-gram)
4. Update word vectors based on prediction errors
5. Repeat until convergence

### Applications of NLP in Tetum and Portuguese Languages

Challenges:
- Limited digital resources and datasets
- Lack of standardized orthography (especially for Tetum)
- Morphological complexity (particularly in Portuguese)

Potential applications:
1. Machine translation between Tetum, Portuguese, and other languages
2. Text-to-speech and speech-to-text systems for accessibility
3. Sentiment analysis for social media monitoring
4. Automated content summarization for news and government documents
5. Language learning tools and applications

Case study: NLP for low-resource languages in Indonesia
- Discuss similarities with Timor-Leste's linguistic situation
- Highlight successful projects and methodologies

## 2. Discussion Questions

1. How might NLP technologies impact the preservation and promotion of Tetum and other indigenous languages in Timor-Leste?
2. What are the potential benefits and risks of implementing machine translation systems between Tetum, Portuguese, and other languages in government and education sectors?
3. How can word embeddings be used to explore and visualize relationships between concepts in Timorese culture and language?
4. What ethical considerations should be taken into account when developing NLP applications for Timor-Leste's languages and cultures?
5. How might NLP technologies assist in the standardization of Tetum orthography and the development of digital resources for the language?

## 3. Writing Exercise Instructions

Title: "Exploring Word Relationships in Timorese Languages"

Instructions:
1. Choose 10 culturally significant words in Tetum or another Timorese language.
2. For each word, list 3-5 related words or concepts.
3. Draw a simple diagram showing the relationships between these words.
4. Write a short paragraph (100-150 words) explaining how these word relationships reflect aspects of Timorese culture or daily life.
5. Discuss how capturing these relationships in a word embedding model could be valuable for NLP applications in Timor-Leste.

## 4. Assignment Details

Title: "Proposal for an NLP Application in Timor-Leste"

Instructions:
1. Identify a specific challenge or opportunity in Timor-Leste that could be addressed using NLP technologies.
2. Research existing NLP applications in similar contexts or for similar languages.
3. Write a 1000-word proposal outlining:
   a. The problem or opportunity you've identified
   b. The specific NLP techniques or technologies you propose to use
   c. The potential impact of your proposed application
   d. Challenges in implementation and how they might be addressed
   e. A basic implementation plan, including data collection and model development
4. Include a bibliography with at least 5 relevant academic or industry sources.

Submission deadline: End of week 4

## 5. Additional Materials and Examples

### Sample Word Embedding Visualization

[Include an image or link to an interactive visualization showing word embeddings for common Tetum or Portuguese words]

### Code Snippet: Using Word2Vec with Gensim

```python
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# Assuming you have a text file 'tetum_corpus.txt' with one sentence per line
sentences = LineSentence('tetum_corpus.txt')

# Train the Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Find similar words
similar_words = model.wv.most_similar('paz', topn=10)
print(similar_words)

# Perform word analogy
result = model.wv.most_similar(positive=['feto', 'liurai'], negative=['mane'], topn=1)
print(result)
```

### Resource List for Tetum NLP

1. CPLP Corpus: A parallel corpus of Portuguese and other CPLP languages, including Tetum
   [Link to CPLP Corpus]

2. Tetun Dictionary: Online dictionary for Tetum language
   [Link to Tetun Dictionary]

3. Global Voices in Tetum: News articles in Tetum, potential source for corpus building
   [Link to Global Voices in Tetum]

4. Low-Resource NLP Toolkit: Open-source tools for NLP in low-resource languages
   [Link to Low-Resource NLP Toolkit]

5. Crúbadán Project: Web-crawled text data for Tetum and other low-resource languages
   [Link to Crúbadán Project]