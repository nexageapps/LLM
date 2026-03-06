<div align="center">

# LLM Mastery: Zero to Production

### Master Large Language Models through 60 hands-on lessons

**From tokenization to transformers. From fine-tuning to deployment. Build real AI that works.**

60 hands-on lessons. 4 progressive levels. Real-world projects.

[Quick Start](#getting-started) • [Course Structure](#course-structure) • [Contributing](./CONTRIBUTING.md) • [LinkedIn](https://www.linkedin.com/in/karthik-arjun-a5b4a258/)

[![Python](https://img.shields.io/badge/Python-3.8+-orange.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Lessons](https://img.shields.io/badge/Lessons-60+-brightgreen.svg)](./01_Basic/)
[![Sponsored by nexageapps](https://img.shields.io/badge/Sponsored%20by-nexageapps-blue.svg)](https://nexageapps.com)

</div>

---

## 📚 Course Overview

This repository contains a structured learning path for Large Language Models (LLMs), designed specifically for Master's in AI students. The curriculum progresses from foundational concepts to expert-level implementations, with hands-on Jupyter notebooks for each lesson.

### 🎯 Learning Philosophy
- **Theory + Practice**: Each lesson combines conceptual understanding with executable code
- **Progressive Complexity**: Build knowledge incrementally across 60 lessons
- **Real-world Applications**: Learn through practical examples and use cases
- **Self-paced Learning**: Complete lessons at your own speed with clear explanations

---

## 📖 Course Structure

The course is divided into **4 levels** with **15 lessons each** (60 total lessons):

### 🟢 Level 1: Basic (Lessons 1-15)
**Focus:** Foundations of NLP, tokenization, embeddings, and transformer basics

| Lesson | Topic | Description |
|--------|-------|-------------|
| L1 | Text Processing & Tokenization | Understanding text data, creating tokens, vocabulary building |
| L2 | Transformer Pipelines | Using pre-trained models, classification, sentiment analysis |
| L3 | Word Embeddings | Word2Vec, GloVe, embedding spaces |
| L4 | Attention Mechanisms | Self-attention, multi-head attention basics |
| L5 | Positional Encoding | Understanding position in sequences |
| L6 | Transformer Architecture | Encoder-decoder structure, layer normalization |
| L7 | Pre-training Concepts | MLM, CLM, and training objectives |
| L8 | Tokenizers Deep Dive | BPE, WordPiece, SentencePiece |
| L9 | Model Loading & Inference | HuggingFace basics, model selection |
| L10 | Text Generation Basics | Greedy search, beam search, sampling |
| L11 | Prompt Engineering 101 | Crafting effective prompts |
| L12 | Zero-shot Learning | Classification without training data |
| L13 | Few-shot Learning | Learning from examples |
| L14 | Model Evaluation Metrics | Perplexity, BLEU, ROUGE |
| L15 | Basic Project | Build a simple chatbot |

### 🔵 Level 2: Intermediate (Lessons 16-30)
**Focus:** Fine-tuning, advanced architectures, and specialized models

| Lesson | Topic | Description |
|--------|-------|-------------|
| L16 | Transfer Learning | Adapting pre-trained models |
| L17 | Fine-tuning Techniques | Full fine-tuning vs parameter-efficient |
| L18 | LoRA & Adapters | Low-rank adaptation methods |
| L19 | BERT Family | BERT, RoBERTa, ALBERT, DistilBERT |
| L20 | GPT Family | GPT-2, GPT-3, GPT-4 architecture |
| L21 | T5 & Seq2Seq Models | Text-to-text frameworks |
| L22 | Domain Adaptation | Adapting models to specific domains |
| L23 | Multi-task Learning | Training on multiple objectives |
| L24 | Instruction Tuning | Teaching models to follow instructions |
| L25 | RLHF Basics | Reinforcement learning from human feedback |
| L26 | Model Compression | Distillation, pruning, quantization |
| L27 | Efficient Inference | Optimization techniques for deployment |
| L28 | RAG Systems | Retrieval-augmented generation |
| L29 | Vector Databases | Storing and retrieving embeddings |
| L30 | Intermediate Project | Build a document Q&A system |

### 🟠 Level 3: Advanced (Lessons 31-45)
**Focus:** Custom architectures, training from scratch, and advanced techniques

| Lesson | Topic | Description |
|--------|-------|-------------|
| L31 | Training from Scratch | Building LLMs from ground up |
| L32 | Custom Architectures | Designing novel transformer variants |
| L33 | Distributed Training | Multi-GPU and multi-node training |
| L34 | Mixed Precision Training | FP16, BF16 optimization |
| L35 | Gradient Accumulation | Training large models with limited memory |
| L36 | Advanced Optimization | AdamW, Lion, learning rate schedules |
| L37 | Data Preparation | Curating and cleaning training data |
| L38 | Tokenizer Training | Building custom tokenizers |
| L39 | Model Parallelism | Pipeline and tensor parallelism |
| L40 | Flash Attention | Efficient attention implementations |
| L41 | Long Context Models | Handling extended sequences |
| L42 | Multimodal LLMs | Vision-language models (CLIP, LLaVA) |
| L43 | Code Generation Models | Codex, CodeLlama, StarCoder |
| L44 | Model Alignment | Safety, bias mitigation, ethical AI |
| L45 | Advanced Project | Train a specialized domain model |

### � Level 4: Expert (Lessons 46-60)
**Focus:** Research frontiers, production systems, and cutting-edge techniques

| Lesson | Topic | Description |
|--------|-------|-------------|
| L46 | Constitutional AI | Advanced alignment techniques |
| L47 | Mixture of Experts | MoE architectures (Mixtral, GPT-4) |
| L48 | State Space Models | Mamba and alternatives to attention |
| L49 | Retrieval Systems | Advanced RAG, HyDE, query expansion |
| L50 | Agent Systems | LLM-powered autonomous agents |
| L51 | Tool Use & Function Calling | Integrating external tools |
| L52 | Production Deployment | Serving, scaling, monitoring |
| L53 | Cost Optimization | Reducing inference costs |
| L54 | Evaluation Frameworks | LLM-as-judge, benchmarking |
| L55 | Prompt Injection & Security | Adversarial attacks and defenses |
| L56 | Continual Learning | Updating models with new data |
| L57 | Model Merging | Combining multiple models |
| L58 | Research Paper Implementation | Reproducing SOTA results |
| L59 | Custom Training Frameworks | Building training pipelines |
| L60 | Capstone Project | End-to-end LLM application |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Basic understanding of machine learning
- Familiarity with PyTorch or TensorFlow
- Jupyter Notebook or Google Colab

### Installation
```bash
# Clone the repository
git clone https://github.com/nexageapps/LLM.git
cd LLM

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Recommended Learning Path
1. Start with **Basic/L1** and progress sequentially
2. Complete all code exercises in each notebook
3. Attempt the project at the end of each level
4. Review and experiment with variations
5. Join discussions and share your implementations

---

## 📂 Repository Structure

```
LLM/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── 01_Basic/                         # Level 1: Basic (L1-L15)
│   ├── README.md                     # Level overview
│   ├── L1_Text_Processing.ipynb
│   ├── L2_Transformer_Pipelines.ipynb
│   └── ...
├── 02_Intermediate/                  # Level 2: Intermediate (L16-L30)
│   ├── README.md
│   ├── L16_Transfer_Learning.ipynb
│   └── ...
├── 03_Advanced/                      # Level 3: Advanced (L31-L45)
│   ├── README.md
│   ├── L31_Training_From_Scratch.ipynb
│   └── ...
├── 04_Expert/                        # Level 4: Expert (L46-L60)
│   ├── README.md
│   ├── L46_Constitutional_AI.ipynb
│   └── ...
├── datasets/                         # Sample datasets
├── models/                           # Saved models
└── utils/                            # Helper functions
```

---

## 🎓 Learning Outcomes

By completing this course, you will:

✅ Understand transformer architecture from first principles  
✅ Build and train custom LLMs  
✅ Fine-tune models for specific tasks  
✅ Implement advanced techniques (LoRA, RLHF, RAG)  
✅ Deploy production-ready LLM applications  
✅ Stay current with latest research and techniques  
✅ Develop expertise in prompt engineering and model evaluation  
✅ Create multimodal and agent-based systems  

---

## 📚 Key References

- **Build a Large Language Model (From Scratch)** - Sebastian Raschka
- **Attention Is All You Need** - Vaswani et al. (2017)
- **HuggingFace Transformers Documentation**
- **OpenAI Research Papers**
- **Anthropic Research**
- **Google AI Blog**

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

---

## 📧 Contact & Support

- **Author:** Karthik Arjun
- **LinkedIn:** [Connect with me](https://www.linkedin.com/in/karthik-arjun-a5b4a258/)
- **Issues:** Open an issue on GitHub
- **Discussions:** Join our community discussions

---

## 📜 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 🌟 Acknowledgments

Special thanks to:
- Sebastian Raschka for "Build a Large Language Model"
- HuggingFace team for transformers library
- OpenAI, Anthropic, and Google for advancing LLM research
- The open-source AI community

---

**Happy Learning! 🚀**

*Last Updated: March 2026*
