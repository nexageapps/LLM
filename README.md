<div align="center">

# LLM Mastery: Zero to Production

### Master Large Language Models through 60 hands-on lessons

**From tokenization to transformers. From fine-tuning to deployment. Build real AI that works.**

60 hands-on lessons · 4 progressive levels · Real-world projects

[Quick Start](#-getting-started) · [Learning Flow](#-learning-flow) · [Course Map](#-course-map) · [Contributing](./CONTRIBUTING.md) · [LinkedIn](https://www.linkedin.com/in/karthik-arjun-a5b4a258/)

[![Python](https://img.shields.io/badge/Python-3.8+-orange.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Lessons](https://img.shields.io/badge/Lessons-60+-brightgreen.svg)](./01_Basic/)
[![Sponsored by nexageapps](https://img.shields.io/badge/Sponsored%20by-nexageapps-blue.svg)](https://nexageapps.com)

---

**If you find this helpful, please star the repository!**

[![Buy me a book](https://img.shields.io/badge/Buy%20Me%20A%20Book-Support%20This%20Project-yellow?style=for-the-badge)](https://buymeacoffee.com/fcc4sbsx5f6)

*Made by a student, for students*

</div>

---

## Table of Contents

| Section | Description |
|--------|--------------|
| [Learning Flow](#-learning-flow) | Visual journey from Basic → Expert |
| [Course Map](#-course-map) | Level-by-level breakdown with Mermaid |
| [Getting Started](#-getting-started) | Prerequisites, install, first steps |
| [Repository Structure](#-repository-structure) | Folder layout and navigation |
| [Learning Outcomes](#-learning-outcomes) | What you'll achieve |
| [References & Support](#-references--support) | Resources and contact |

---

## Learning Flow

This course is designed as a **single path**: each level builds on the previous one. Use the diagrams below to see how concepts connect and where to go next.

### Journey: Basic → Expert

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#0f172a', 'primaryColor':'#dbeafe', 'primaryBorderColor':'#2563eb', 'secondaryTextColor':'#0f172a', 'secondaryColor':'#fef3c7', 'tertiaryTextColor':'#0f172a', 'tertiaryColor':'#dcfce7', 'background':'#ffffff', 'mainBkg':'#f8fafc', 'secondBkg':'#f1f5f9', 'textColor':'#1e293b', 'titleColor':'#0f172a', 'clusterBkg':'#eff6ff', 'clusterBorder':'#2563eb', 'nodeBorder':'#2563eb', 'edgeColor':'#475569', 'lineColor':'#475569'}}}%%
flowchart LR
    subgraph L1["Level 1: Basic"]
        direction TB
        A1[Text & Tokens]
        A2[Embeddings & Attention]
        A3[Transformers & Inference]
        A4[Prompts & Evaluation]
        A1 --> A2 --> A3 --> A4
    end

    subgraph L2["Level 2: Intermediate"]
        direction TB
        B1[Transfer & Fine-tuning]
        B2[Model Families]
        B3[RAG & Efficiency]
        B1 --> B2 --> B3
    end

    subgraph L3["Level 3: Advanced"]
        direction TB
        C1[Train from Scratch]
        C2[Distributed & Optimized]
        C3[Multimodal & Alignment]
        C1 --> C2 --> C3
    end

    subgraph L4["Level 4: Expert"]
        direction TB
        D1[Alignment & MoE]
        D2[Agents & Tools]
        D3[Production & Research]
        D1 --> D2 --> D3
    end

    L1 --> L2 --> L3 --> L4
```

### Concept Dependencies (What Leads to What)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#0f172a', 'primaryColor':'#dbeafe', 'primaryBorderColor':'#2563eb', 'secondaryTextColor':'#0f172a', 'secondaryColor':'#e0e7ff', 'tertiaryTextColor':'#0f172a', 'tertiaryColor':'#dcfce7', 'background':'#ffffff', 'mainBkg':'#f8fafc', 'textColor':'#1e293b', 'titleColor':'#0f172a', 'clusterBkg':'#f0f9ff', 'clusterBorder':'#0284c7', 'nodeBorder':'#0ea5e9', 'edgeColor':'#475569'}}}%%
flowchart TB
    subgraph Foundations
        T[Text & Tokenization]
        E[Embeddings]
        Att[Attention]
        PE[Positional Encoding]
        T --> E --> Att --> PE
    end

    subgraph Architecture
        Enc[Encoder-Decoder]
        PT[Pre-training]
        TG[Text Generation]
        PE --> Enc
        Att --> Enc
        Enc --> PT --> TG
    end

    subgraph Application
        Prompt[Prompt Engineering]
        Zero[Zero-shot]
        Few[Few-shot]
        Eval[Metrics]
        TG --> Prompt --> Zero --> Few
        TG --> Eval
    end

    subgraph Adaptation
        TL[Transfer Learning]
        FT[Fine-tuning]
        LoRA[LoRA & Adapters]
        Foundations --> TL
        Architecture --> TL
        TL --> FT --> LoRA
    end

    subgraph Systems
        RAG[RAG & Vectors]
        Deploy[Deployment]
        Agents[Agents]
        LoRA --> RAG
        RAG --> Deploy
        Deploy --> Agents
    end

    Application --> Adaptation
```

### Skill Progression at a Glance

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#0f172a', 'primaryColor':'#dbeafe', 'secondaryTextColor':'#0f172a', 'tertiaryTextColor':'#0f172a', 'textColor':'#e2e8f0', 'titleColor':'#f1f5f9', 'lineColor':'#94a3b8', 'quadrant1TextFill':'#0f172a', 'quadrant2TextFill':'#0f172a', 'quadrant3TextFill':'#0f172a', 'quadrant4TextFill':'#0f172a', 'quadrant1Fill':'#dbeafe', 'quadrant2Fill':'#dcfce7', 'quadrant3Fill':'#fef3c7', 'quadrant4Fill':'#e0e7ff', 'background':'#1e293b'}}}%%
quadrantChart
    title Skill level by course stage
    x-axis Beginner --> Expert
    y-axis Theory --> Production
    quadrant-1 Research & custom
    quadrant-2 Deploy & scale
    quadrant-3 Foundations
    quadrant-4 Fine-tune & adapt
    "Basic L1-L15": [0.2, 0.3]
    "Intermediate L16-L30": [0.45, 0.5]
    "Advanced L31-L45": [0.7, 0.6]
    "Expert L46-L60": [0.9, 0.85]
```

---

## Course Map

### Level 1: Basic (L1–L15) — Foundations

**Goal:** Understand text, tokens, embeddings, attention, and how to use pre-trained transformers.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#0f172a', 'primaryColor':'#dbeafe', 'secondaryColor':'#e0e7ff', 'tertiaryColor':'#dcfce7', 'background':'#ffffff', 'mainBkg':'#f8fafc', 'textColor':'#1e293b', 'titleColor':'#0f172a', 'nodeBorder':'#2563eb', 'clusterBorder':'#2563eb'}}}%%
mindmap
  root((Basic))
    Text
      Tokenization
      Vocabulary
      Pipelines
    Representations
      Word Embeddings
      Attention
      Positional Encoding
    Architecture
      Transformer
      Pre-training
      Tokenizers
    Usage
      Loading & Inference
      Text Generation
      Prompts
    Evaluation
      Zero-shot
      Few-shot
      Metrics
      Project: Chatbot
```

| # | Topic | One-line description |
|---|--------|----------------------|
| L1 | Text Processing & Tokenization | Text data, tokens, vocabulary |
| L2 | Transformer Pipelines | Pre-trained models, classification, sentiment |
| L3 | Word Embeddings | Word2Vec, GloVe, embedding spaces |
| L4 | Attention Mechanisms | Self-attention, multi-head attention |
| L5 | Positional Encoding | Position in sequences |
| L6 | Transformer Architecture | Encoder-decoder, layer norm |
| L7 | Pre-training Concepts | MLM, CLM, training objectives |
| L8 | Tokenizers Deep Dive | BPE, WordPiece, SentencePiece |
| L9 | Model Loading & Inference | HuggingFace, model selection |
| L10 | Text Generation Basics | Greedy, beam search, sampling |
| L11 | Prompt Engineering 101 | Effective prompts |
| L12 | Zero-shot Learning | Classification without training |
| L13 | Few-shot Learning | Learning from examples |
| L14 | Model Evaluation Metrics | Perplexity, BLEU, ROUGE |
| L15 | **Basic Project** | Simple chatbot |

---

### Level 2: Intermediate (L16–L30) — Adaptation & Systems

**Goal:** Fine-tune models, use major families (BERT/GPT/T5), and build RAG and efficient inference.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#0f172a', 'primaryColor':'#fef3c7', 'primaryBorderColor':'#d97706', 'secondaryColor':'#dcfce7', 'tertiaryColor':'#dbeafe', 'background':'#ffffff', 'mainBkg':'#fffbeb', 'textColor':'#1e293b', 'nodeBorder':'#b45309', 'edgeColor':'#e2e8f0', 'lineColor':'#e2e8f0', 'arrowheadColor':'#e2e8f0'}}}%%
flowchart LR
    L16[Transfer Learning] --> L17[Fine-tuning]
    L17 --> L18[LoRA]
    L18 --> L19[BERT] & L20[GPT] & L21[T5]
    L19 & L20 & L21 --> L22[Domain] & L23[Multi-task] & L24[Instruction]
    L24 --> L25[RLHF]
    L25 --> L26[Compression] --> L27[Efficient Inference]
    L27 --> L28[RAG] --> L29[Vectors] --> L30[Project: Doc QA]
```

| # | Topic | One-line description |
|---|--------|----------------------|
| L16 | Transfer Learning | Adapting pre-trained models |
| L17 | Fine-tuning Techniques | Full vs parameter-efficient |
| L18 | LoRA & Adapters | Low-rank adaptation |
| L19 | BERT Family | BERT, RoBERTa, ALBERT, DistilBERT |
| L20 | GPT Family | GPT-2/3/4 architecture |
| L21 | T5 & Seq2Seq | Text-to-text frameworks |
| L22 | Domain Adaptation | Domain-specific models |
| L23 | Multi-task Learning | Multiple objectives |
| L24 | Instruction Tuning | Following instructions |
| L25 | RLHF Basics | Human feedback |
| L26 | Model Compression | Distillation, pruning, quantization |
| L27 | Efficient Inference | Deployment optimizations |
| L28 | RAG Systems | Retrieval-augmented generation |
| L29 | Vector Databases | Storing/retrieving embeddings |
| L30 | **Intermediate Project** | Document Q&A system |

---

### Level 3: Advanced (L31–L45) — Training & Scale

**Goal:** Train from scratch, use custom architectures, distributed and mixed-precision training, and multimodal/alignment topics.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#0f172a', 'primaryColor':'#dcfce7', 'primaryBorderColor':'#15803d', 'secondaryTextColor':'#0f172a', 'secondaryColor':'#dbeafe', 'tertiaryTextColor':'#0f172a', 'tertiaryColor':'#e0e7ff', 'background':'#ffffff', 'mainBkg':'#f0fdf4', 'textColor':'#1e293b', 'titleColor':'#0f172a', 'clusterBkg':'#ecfdf5', 'clusterBorder':'#059669', 'nodeBorder':'#0d9488', 'edgeColor':'#e2e8f0', 'lineColor':'#e2e8f0', 'arrowheadColor':'#e2e8f0'}}}%%
flowchart TB
    subgraph Train
        L31[Train from Scratch]
        L32[Custom Architectures]
        L31 --> L32
    end

    subgraph Scale
        L33[Distributed]
        L34[Mixed Precision]
        L35[Gradient Accum]
        L39[Model Parallelism]
        L40[Flash Attention]
        L33 --> L34 --> L35
        L34 --> L39 --> L40
    end

    subgraph Data
        L37[Data Prep]
        L38[Tokenizer Training]
    end

    subgraph Beyond
        L41[Long Context]
        L42[Multimodal]
        L43[Code Models]
        L44[Alignment]
        L45[Project]
    end

    Train --> Scale
    Data --> Train
    Scale --> Beyond
```

| # | Topic | One-line description |
|---|--------|----------------------|
| L31 | Training from Scratch | Building LLMs from scratch |
| L32 | Custom Architectures | Novel transformer variants |
| L33 | Distributed Training | Multi-GPU, multi-node |
| L34 | Mixed Precision Training | FP16, BF16 |
| L35 | Gradient Accumulation | Large models, limited memory |
| L36 | Advanced Optimization | AdamW, Lion, LR schedules |
| L37 | Data Preparation | Curating and cleaning data |
| L38 | Tokenizer Training | Custom tokenizers |
| L39 | Model Parallelism | Pipeline and tensor parallelism |
| L40 | Flash Attention | Efficient attention |
| L41 | Long Context Models | Extended sequences |
| L42 | Multimodal LLMs | Vision-language (CLIP, LLaVA) |
| L43 | Code Generation Models | Codex, CodeLlama, StarCoder |
| L44 | Model Alignment | Safety, bias, ethics |
| L45 | **Advanced Project** | Specialized domain model |

---

### Level 4: Expert (L46–L60) — Research & Production

**Goal:** Alignment, MoE/SSMs, agents, tools, deployment, and capstone.

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#0f172a', 'primaryColor':'#ede9fe', 'primaryBorderColor':'#6d28d9', 'secondaryColor':'#fce7f3', 'tertiaryColor':'#dbeafe', 'background':'#ffffff', 'mainBkg':'#faf5ff', 'textColor':'#1e293b', 'nodeBorder':'#7c3aed', 'edgeColor':'#e2e8f0', 'lineColor':'#e2e8f0', 'arrowheadColor':'#e2e8f0'}}}%%
flowchart LR
    L46[Constitutional AI] --> L47[MoE]
    L47 --> L48[State Space]
    L48 --> L49[Retrieval]
    L49 --> L50[Agents] --> L51[Tools]
    L51 --> L52[Deploy] --> L53[Cost]
    L53 --> L54[Eval] & L55[Security] & L56[Continual] & L57[Merging]
    L54 & L55 & L56 & L57 --> L58[Research] --> L59[Frameworks] --> L60[Capstone]
```

| # | Topic | One-line description |
|---|--------|----------------------|
| L46 | Constitutional AI | Advanced alignment |
| L47 | Mixture of Experts | MoE (Mixtral, GPT-4) |
| L48 | State Space Models | Mamba, alternatives to attention |
| L49 | Retrieval Systems | Advanced RAG, HyDE |
| L50 | Agent Systems | LLM-powered agents |
| L51 | Tool Use & Function Calling | External tools |
| L52 | Production Deployment | Serving, scaling, monitoring |
| L53 | Cost Optimization | Reducing inference cost |
| L54 | Evaluation Frameworks | LLM-as-judge, benchmarks |
| L55 | Prompt Injection & Security | Attacks and defenses |
| L56 | Continual Learning | Updating with new data |
| L57 | Model Merging | Combining models |
| L58 | Research Paper Implementation | Reproducing SOTA |
| L59 | Custom Training Frameworks | Training pipelines |
| L60 | **Capstone Project** | End-to-end LLM application |

---

## Getting Started

### Prerequisites

| Requirement | Notes |
|-------------|--------|
| **Python** | 3.8+ |
| **ML basics** | Supervised learning, loss, gradients |
| **Framework** | PyTorch or TensorFlow |
| **Environment** | Jupyter Notebook or Google Colab |

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

### Recommended Path

1. **Start at Basic L1** and go in order.
2. **Run every notebook** and finish the exercises.
3. **Do each level project** (L15, L30, L45, L60) before moving on.
4. **Experiment** — change prompts, data, and hyperparameters.
5. **Use the Mermaid maps** above to see how lessons connect.

---

## Repository Structure

```
LLM/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── 01_Basic/                    # Level 1 (L1–L15)
│   ├── README.md
│   ├── L1_Text_Processing_Tokenization.ipynb
│   ├── L2_Transformer_Pipelines.ipynb
│   └── ...
├── 02_Intermediate/             # Level 2 (L16–L30)
│   ├── README.md
│   ├── L16_Transfer_Learning.ipynb
│   └── ...
├── 03_Advanced/                 # Level 3 (L31–L45)
│   ├── README.md
│   ├── L31_Training_From_Scratch.ipynb
│   └── ...
├── 04_Expert/                   # Level 4 (L46–L60)
│   ├── README.md
│   └── ...
├── datasets/                    # Sample datasets
├── models/                      # Saved models
└── utils/                       # Helper functions
```

---

## Learning Outcomes

By the end of the course you will be able to:

| Area | Outcome |
|------|--------|
| **Theory** | Explain transformers from first principles |
| **Training** | Train and fine-tune custom LLMs |
| **Efficiency** | Use LoRA, distillation, quantization |
| **Systems** | Implement RAG, RLHF, and evaluation |
| **Deployment** | Ship production-ready LLM apps |
| **Practice** | Apply prompt engineering and evaluation |
| **Frontiers** | Work with multimodal and agent systems |

---

## References & Support

### Key References

- **Build a Large Language Model (From Scratch)** — Sebastian Raschka  
- **Attention Is All You Need** — Vaswani et al. (2017)  
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)  
- OpenAI & Anthropic research  
- Google AI Blog  

### Contributing

1. Fork the repo  
2. Create a feature branch  
3. Add improvements  
4. Open a pull request  

### Contact

| | |
|---|---|
| **Author** | Karthik Arjun |
| **LinkedIn** | [Connect](https://www.linkedin.com/in/karthik-arjun-a5b4a258/) |
| **Issues** | Open an issue on GitHub |
| **Discussions** | Use repo discussions for questions |

---

## License

This project is licensed under the **MIT License** — see [LICENSE](./LICENSE).

---

## Acknowledgments

- Sebastian Raschka — *Build a Large Language Model*  
- HuggingFace — transformers and ecosystem  
- OpenAI, Anthropic, Google — LLM research  
- The open-source AI community  

---

**Happy learning!**

*Last updated: March 2026*
