# LLM — Lesson 1: Tokenization, Vocabulary, Encoding & Decoding

**Author**        | [Karthik Arjun](https://www.linkedin.com/in/karthik-arjun-a5b4a258/)  
------------------|-------------------------------------------------------------  
**Book Reference**| *Build a Large Language Model* by Sebastian Raschka  
**Lesson**        | L1 - Tokenization, Vocabulary, Encoding & Decoding  
**Next Lesson**   | L2 - Tensors & Embeddings (Coming Soon)

---

## 📘 About

This repository contains the first lesson in a learning series for building a simple Large Language Model from scratch. Lesson 1 (L1) covers the fundamentals of working with raw text: tokenization, building a vocabulary, encoding text to token IDs, and decoding token IDs back to human-readable text. The materials follow concepts from Sebastian Raschka's book and are designed for hands-on learning using only Python's standard library.

---

## ✅ What This Lesson Covers

| Step | Task               | Description |
|------|--------------------|-------------|
| 1    | Download Text File | Download `the-verdict.txt` (example dataset) |
| 2    | Tokenize Text      | Use regex to split text into words & punctuation |
| 3    | Build Vocabulary   | Create unique token → ID mapping |
| 4    | Encode Input       | Convert text (e.g., "I love Jack") into token IDs |
| 5    | Decode             | Convert token IDs back to readable text |

---

## 🧰 Requirements

- Python 3.8+  
- Only uses built-in modules: `os`, `re`, `urllib` (no external dependencies)

---

## ⚙️ Setup & Usage

1. Clone the repository:
   git clone https://github.com/nexageapps/LLM.git

2. Run the lesson script (example):
   python lesson1_tokenization.py

3. The script will:
   - download `the-verdict.txt` if missing,
   - tokenize the text,
   - build a vocabulary mapping tokens to integer IDs,
   - demonstrate encoding and decoding.

(Adjust filenames or commands according to the repository scripts.)

---

## 📂 Files of Interest

- README.md — this file  
- lesson1_tokenization.py — tokenization, vocab, encode/decode examples  
- the-verdict.txt — example text (downloaded by scripts)

---

## 🔭 Next Steps

Lesson 2 will introduce tensors and embeddings and show how token IDs map to numeric vectors for model input.

---

## 🤝 Contributing

Contributions, issues, and suggestions are welcome. Please open an issue for discussion before submitting large changes.

---

## 📄 License & Contact

This repository is provided for educational purposes. For questions or collaboration, reach out to the author on LinkedIn.