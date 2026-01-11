# Next Word Generator using LSTM

A beginner-friendly NLP project that predicts the **next word in a sentence** using an LSTM (Long Short-Term Memory) neural network.  
This project is built mainly for **learning purposes** to understand sequence modeling and text generation, not for production use.

---

## 📖 Project Description
The goal of this project is to explore how recurrent neural networks, specifically LSTMs, can be applied to natural language processing tasks.  
By training on text data, the model learns word sequences and attempts to predict the next word given a partial sentence.

---

## ✨ Features
- Text preprocessing: tokenization and padding
- Neural network with:
  - Embedding layer
  - LSTM layer
  - Dense + Softmax output layer
- Streamlit app for simple user interaction
- Example-driven workflow for beginners in NLP

---

## 🛠 Tech Stack
- **Python**
- **TensorFlow / Keras**
- **NumPy**
- **Streamlit**

---

## ⚙️ How the Model Works
1. **Preprocessing**  
   - Input text is tokenized into sequences of integers.  
   - Sequences are padded to ensure uniform length.

2. **Model Architecture**  
   - **Embedding Layer**: Converts words into dense vector representations.  
   - **LSTM Layer**: Learns sequential dependencies between words.  
   - **Dense + Softmax Layer**: Outputs probability distribution over the vocabulary for the next word.

3. **Prediction**  
   - Given an input sequence, the model predicts the most likely next word.  
   - Example:  
     - Input: `"Hello, You are "`  
     - Output: `"Hello, You are right it about the difference"`

---

## ⏱ Training Time
Training an LSTM is **computationally expensive** due to its sequential nature.  
- On a CPU, training can take **60–70 minutes** depending on dataset size.  
- This is expected behavior and highlights why LSTMs are less efficient compared to newer architectures.

---

## ⚠️ Limitations
- **Slow training** on large datasets (especially on CPU).  
- **Limited generalization**: predictions may not always be meaningful without extensive training data.  
- **No pretrained model or large datasets** included in this repository (to keep it lightweight).  

---

## 🎯 Purpose
This project is designed for **learning and experimentation**:  
- Understanding sequence modeling with LSTMs.  
- Practicing text preprocessing techniques.  
- Building a simple end-to-end NLP pipeline.  

It is **not intended for production deployment**.

---

## 🚀 Future Improvements
- Replace LSTM with **Transformer-based models** (e.g., GPT, BERT) for faster training and better performance.  
- Add support for pretrained embeddings (e.g., GloVe, Word2Vec).  
- Improve the Streamlit interface with visualization of predictions.  

---

## 📌 Example Usage
Run the Streamlit app:
```bash
streamlit run app.py
