# Quick Start Guide - LLM Mastery Course

Welcome! This guide will help you get started with the LLM Mastery course in under 10 minutes.

## Setup (5 minutes)

### Option 1: Local Setup (Recommended for GPU users)

1. **Clone the repository**
```bash
git clone https://github.com/nexageapps/LLM.git
cd LLM
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Launch Jupyter**
```bash
jupyter notebook
```

### Option 2: Google Colab (No setup required!)

1. Open any lesson notebook from GitHub
2. Click "Open in Colab" badge at the top
3. Run the first cell to install dependencies
4. Start learning immediately!

---

## Your First Lesson (5 minutes)

### Start with L1: Text Processing & Tokenization

1. Navigate to `01_Basic/L1_Text_Processing_Tokenization.ipynb`
2. Read the introduction and concepts
3. Run each code cell sequentially
4. Experiment with the code
5. Complete the exercises at the end

**What you'll learn:**
- How LLMs process text
- Creating tokens from raw text
- Building vocabularies
- Encoding and decoding

---

## Learning Path

### Week 1-2: Basic Level (L1-L15)
- **Time commitment:** 2-3 hours per lesson
- **Focus:** Foundations and pre-trained models
- **Project:** Build a simple chatbot

### Week 3-4: Intermediate Level (L16-L30)
- **Time commitment:** 3-4 hours per lesson
- **Focus:** Fine-tuning and RAG systems
- **Project:** Document Q&A system

### Week 5-6: Advanced Level (L31-L45)
- **Time commitment:** 4-5 hours per lesson
- **Focus:** Training from scratch
- **Project:** Domain-specific model

### Week 7-8: Expert Level (L46-L60)
- **Time commitment:** 5-6 hours per lesson
- **Focus:** Research and production
- **Project:** End-to-end LLM application

---

## Tips for Success

### 1. Learn by Doing
- Don't just read the code - run it!
- Modify parameters and observe changes
- Break things and fix them

### 2. Take Notes
- Keep a learning journal
- Document your experiments
- Save interesting findings

### 3. Build Projects
- Apply concepts immediately
- Start small, iterate
- Share your work

### 4. Join the Community
- Ask questions in discussions
- Help others learn
- Share your progress

### 5. Stay Consistent
- Set a regular schedule
- Complete one lesson at a time
- Don't skip the exercises

---

## Troubleshooting

### Issue: CUDA out of memory
**Solution:** 
- Use smaller batch sizes
- Enable gradient checkpointing
- Use Google Colab with GPU runtime

### Issue: Package installation fails
**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

### Issue: Slow training
**Solution:**
- Enable mixed precision training
- Use smaller models for learning
- Consider cloud GPU options

### Issue: Model download fails
**Solution:**
```python
# Set HuggingFace cache directory
import os
os.environ['HF_HOME'] = '/path/to/cache'
```

---

## Track Your Progress

Create a learning log:

```markdown
# My LLM Learning Journey

## Week 1
- [x] L1: Text Processing (Completed)
- [x] L2: Transformer Pipelines (Completed)
- [ ] L3: Word Embeddings (In Progress)

### Key Learnings
- Tokenization is crucial for LLMs
- Pre-trained models are powerful

### Questions
- How to handle multilingual text?
- Best practices for prompt engineering?

### Next Steps
- Complete L3-L5 this week
- Build a sentiment analyzer
```

---

## Learning Resources

### Official Documentation
- [HuggingFace Docs](https://huggingface.co/docs)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [OpenAI Cookbook](https://cookbook.openai.com/)

### Recommended Reading
- "Build a Large Language Model" - Sebastian Raschka
- "Natural Language Processing with Transformers" - Lewis Tunstall
- Research papers linked in each lesson

### Video Resources
- Andrej Karpathy's YouTube channel
- HuggingFace course videos
- Stanford CS224N lectures

### Communities
- HuggingFace Discord
- r/MachineLearning
- EleutherAI Discord
- Local AI meetups

---

## Your First Week Plan

### Day 1: Setup & L1
- [ ] Complete environment setup
- [ ] Read course README
- [ ] Complete L1: Text Processing

### Day 2: L2-L3
- [ ] L2: Transformer Pipelines
- [ ] L3: Word Embeddings
- [ ] Experiment with embeddings

### Day 3: L4-L5
- [ ] L4: Attention Mechanisms
- [ ] L5: Positional Encoding
- [ ] Visualize attention

### Day 4: L6-L7
- [ ] L6: Transformer Architecture
- [ ] L7: Pre-training Concepts
- [ ] Review and consolidate

### Day 5: L8-L9
- [ ] L8: Tokenizers Deep Dive
- [ ] L9: Model Loading
- [ ] Practice with different models

### Day 6: L10-L11
- [ ] L10: Text Generation
- [ ] L11: Prompt Engineering
- [ ] Build a text generator

### Day 7: Review & Practice
- [ ] Review week's concepts
- [ ] Complete exercises
- [ ] Start planning chatbot project

---

## Ready to Start?

1. Open `01_Basic/L1_Text_Processing_Tokenization.ipynb`
2. Read through the introduction
3. Run the first code cell
4. You're learning LLMs!

---

## Need Help?

- **Issues:** Open a GitHub issue
- **Questions:** Use GitHub Discussions
- **Contact:** [LinkedIn](https://www.linkedin.com/in/karthik-arjun-a5b4a258/)

---

**Happy Learning! Let's master LLMs together!**

*Remember: The journey of a thousand miles begins with a single step. Your first step is L1!*
