# Level 1: Basic - Foundations of LLMs

## Level Overview

Welcome to the foundational level of LLM mastery! This level introduces you to the core concepts of Natural Language Processing and Large Language Models. You'll learn how text is processed, how transformers work, and how to use pre-trained models effectively.

### Learning Objectives
- Understand text tokenization and vocabulary building
- Master transformer architecture basics
- Learn attention mechanisms and positional encoding
- Use pre-trained models for various NLP tasks
- Develop prompt engineering skills
- Build your first LLM-powered application

---

## Lessons Overview

### **L1: Text Processing & Tokenization**
**Duration:** 2-3 hours  
**Concepts:** Characters vs tokens, regex splitting, vocabulary creation, encoding/decoding

**What You'll Learn:**
- How LLMs process raw text
- Creating custom tokenizers
- Building vocabulary from text corpus
- Encoding text to IDs and decoding back

**Key Code:**
```python
# Tokenization example
preprocessed = re.split(r'([,.:;?_!"()\']|--|\\s)', raw_text)
vocab = {token: integer for integer, token in enumerate(all_words)}
```

---

### **L2: Transformer Pipelines**
**Duration:** 2-3 hours  
**Concepts:** HuggingFace pipelines, pre-trained models, zero-shot classification, sentiment analysis

**What You'll Learn:**
- Using HuggingFace transformers library
- Different pipeline types (classification, generation, NER, Q&A)
- Model selection and loading
- Practical applications of pre-trained models

**Key Code:**
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love this course!")
```

---

### **L3: Word Embeddings**
**Duration:** 3-4 hours  
**Concepts:** Word2Vec, GloVe, embedding spaces, semantic similarity

**What You'll Learn:**
- Vector representations of words
- Training Word2Vec models
- Using pre-trained embeddings
- Measuring semantic similarity
- Visualizing embedding spaces

**Applications:**
- Finding similar words
- Analogy tasks (king - man + woman = queen)
- Document similarity

---

### **L4: Attention Mechanisms**
**Duration:** 3-4 hours  
**Concepts:** Self-attention, query-key-value, multi-head attention, attention scores

**What You'll Learn:**
- Why attention is crucial for transformers
- Computing attention scores
- Multi-head attention benefits
- Visualizing attention patterns

**Key Formula:**
```
Attention(Q, K, V) = softmax(QK^T / √d_k)V
```

---

### **L5: Positional Encoding**
**Duration:** 2 hours  
**Concepts:** Absolute vs relative position, sinusoidal encoding, learned positions

**What You'll Learn:**
- Why transformers need positional information
- Sinusoidal positional encoding
- Learned positional embeddings
- Impact on model performance

---

### **L6: Transformer Architecture**
**Duration:** 4 hours  
**Concepts:** Encoder-decoder, layer normalization, residual connections, feed-forward networks

**What You'll Learn:**
- Complete transformer architecture
- Encoder vs decoder differences
- Layer normalization and residual connections
- Building blocks of transformers

**Architecture Components:**
1. Input Embedding + Positional Encoding
2. Multi-Head Attention
3. Feed-Forward Network
4. Layer Normalization
5. Residual Connections

---

### **L7: Pre-training Concepts**
**Duration:** 3 hours  
**Concepts:** MLM (Masked Language Modeling), CLM (Causal Language Modeling), training objectives

**What You'll Learn:**
- Different pre-training strategies
- BERT-style masked language modeling
- GPT-style causal language modeling
- Next sentence prediction

---

### **L8: Tokenizers Deep Dive**
**Duration:** 3 hours  
**Concepts:** BPE, WordPiece, SentencePiece, subword tokenization

**What You'll Learn:**
- Byte Pair Encoding (BPE) algorithm
- WordPiece tokenization (BERT)
- SentencePiece (language-agnostic)
- Handling unknown words and rare tokens

**Comparison:**
| Tokenizer | Used By | Strengths |
|-----------|---------|-----------|
| BPE | GPT-2, GPT-3 | Efficient, handles rare words |
| WordPiece | BERT | Good for morphology |
| SentencePiece | T5, XLNet | Language-agnostic |

---

### **L9: Model Loading & Inference**
**Duration:** 2 hours  
**Concepts:** HuggingFace Hub, model selection, inference optimization

**What You'll Learn:**
- Browsing HuggingFace model hub
- Loading models and tokenizers
- Running inference efficiently
- Model cards and documentation

---

### **L10: Text Generation Basics**
**Duration:** 3 hours  
**Concepts:** Greedy search, beam search, sampling, temperature, top-k, top-p

**What You'll Learn:**
- Different decoding strategies
- Temperature and randomness control
- Top-k and nucleus (top-p) sampling
- Controlling generation quality

**Generation Parameters:**
```python
output = model.generate(
    input_ids,
    max_length=50,
    temperature=0.7,
    top_k=50,
    top_p=0.9,
    num_beams=5
)
```

---

### **L11: Prompt Engineering 101**
**Duration:** 3 hours  
**Concepts:** Prompt design, instruction following, context setting

**What You'll Learn:**
- Crafting effective prompts
- Zero-shot prompting techniques
- Role-playing and persona setting
- Prompt templates

**Best Practices:**
- Be specific and clear
- Provide examples when needed
- Set the context properly
- Iterate and refine

---

### **L12: Zero-shot Learning**
**Duration:** 2 hours  
**Concepts:** Classification without training, label understanding

**What You'll Learn:**
- Zero-shot classification
- How models understand labels
- Practical applications
- Limitations and strengths

---

### **L13: Few-shot Learning**
**Duration:** 3 hours  
**Concepts:** In-context learning, example selection, prompt formatting

**What You'll Learn:**
- Providing examples in prompts
- Example selection strategies
- Few-shot vs fine-tuning
- Optimal number of examples

---

### **L14: Model Evaluation Metrics**
**Duration:** 3 hours  
**Concepts:** Perplexity, BLEU, ROUGE, F1, accuracy

**What You'll Learn:**
- Perplexity for language models
- BLEU for translation
- ROUGE for summarization
- Classification metrics
- Choosing appropriate metrics

**Metrics Summary:**
- **Perplexity:** Lower is better (measures uncertainty)
- **BLEU:** 0-1, higher is better (n-gram overlap)
- **ROUGE:** 0-1, higher is better (recall-oriented)
- **F1:** Harmonic mean of precision and recall

---

### **L15: Basic Project - Simple Chatbot**
**Duration:** 4-6 hours  
**Project:** Build a conversational chatbot using pre-trained models

**Requirements:**
1. Use a pre-trained conversational model
2. Implement conversation history
3. Add personality through prompts
4. Handle multi-turn conversations
5. Create a simple UI (optional)

**Skills Applied:**
- Model loading and inference
- Prompt engineering
- Text generation
- Context management

---

## Setup Instructions

### Install Required Libraries
```bash
pip install transformers torch numpy pandas matplotlib seaborn
pip install datasets tokenizers sentencepiece
pip install jupyter ipywidgets
```

### Verify Installation
```python
import transformers
import torch
print(f"Transformers version: {transformers.__version__}")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
```

---

## Progress Tracking

Track your progress through the level:

- [ ] L1: Text Processing & Tokenization
- [ ] L2: Transformer Pipelines
- [ ] L3: Word Embeddings
- [ ] L4: Attention Mechanisms
- [ ] L5: Positional Encoding
- [ ] L6: Transformer Architecture
- [ ] L7: Pre-training Concepts
- [ ] L8: Tokenizers Deep Dive
- [ ] L9: Model Loading & Inference
- [ ] L10: Text Generation Basics
- [ ] L11: Prompt Engineering 101
- [ ] L12: Zero-shot Learning
- [ ] L13: Few-shot Learning
- [ ] L14: Model Evaluation Metrics
- [ ] L15: Basic Project

---

## Assessment

After completing this level, you should be able to:

- Explain how transformers process text  
- Build custom tokenizers  
- Use pre-trained models for various tasks  
- Understand attention mechanisms  
- Generate text with different strategies  
- Engineer effective prompts  
- Evaluate model performance  
- Build a simple LLM application  

---

## Additional Resources

### Books
- "Build a Large Language Model (From Scratch)" - Sebastian Raschka
- "Natural Language Processing with Transformers" - Lewis Tunstall et al.

### Papers
- "Attention Is All You Need" (Vaswani et al., 2017)
- "BERT: Pre-training of Deep Bidirectional Transformers" (Devlin et al., 2018)
- "Language Models are Few-Shot Learners" (Brown et al., 2020)

### Online Resources
- HuggingFace Course: https://huggingface.co/course
- Jay Alammar's Blog: https://jalammar.github.io/
- Andrej Karpathy's YouTube: Neural Networks Zero to Hero

---

## Next Steps

Once you complete Level 1, proceed to:
**Level 2: Intermediate** - Fine-tuning, advanced architectures, and specialized models

---

**Good luck with your learning journey!**
