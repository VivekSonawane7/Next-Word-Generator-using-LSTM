# 📝 Next Word Generator using LSTM

This project implements a **Next Word Prediction system** using an **LSTM (Long Short-Term Memory)** neural network.  
Given a sequence of words, the model predicts the most likely next word based on learned patterns from text data.

⚠️ This project is built **for learning and understanding NLP and sequence modeling**, not for production use.

---

## 📌 Features

- Predicts the next word for a given sentence
- Supports generating multiple words sequentially
- Uses LSTM for sequence learning
- Text preprocessing (tokenization & padding)
- Embedding layer for word representation
- Simple and readable code structure
- Optional Streamlit UI

---

## 🛠️ Tech Stack

- Python  
- TensorFlow / Keras  
- NumPy  
- Streamlit  
- NLP (Tokenization, Sequence Modeling)

---

## 🧠 How It Works

1. Text data is tokenized into integer sequences  
2. Fixed-length input sequences are created using padding  
3. Words are converted into dense vectors using an Embedding layer  
4. LSTM learns sequential word patterns  
5. Softmax layer predicts the probability of the next word  
6. The most probable word is selected as output  

---

## 🧪 Example

**Input:**
