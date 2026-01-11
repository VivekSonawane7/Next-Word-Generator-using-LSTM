import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# -----------------------------
# Load model and tokenizer
# -----------------------------
@st.cache_resource
def load_resources():
    model = load_model("lstm_model.h5")
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

model, tokenizer = load_resources()

# IMPORTANT: same value used while training
MAX_SEQ_LEN = 10   # change if different

# -----------------------------
# Next word prediction function
# -----------------------------
def predict_next_word(text, model, tokenizer, max_len):
    sequence = tokenizer.texts_to_sequences([text])[0]
    sequence = pad_sequences([sequence], maxlen=max_len, padding="pre")

    preds = model.predict(sequence, verbose=0)
    predicted_index = np.argmax(preds)

    for word, index in tokenizer.word_index.items():
        if index == predicted_index:
            return word
    return ""

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📝 Next Word Generator")
st.write("Type a sentence and predict the next word")

input_text = st.text_input("Enter text")

if st.button("Predict Next Word"):
    if input_text.strip() == "":
        st.warning("Please enter some text")
    else:
        next_word = predict_next_word(
            input_text, model, tokenizer, MAX_SEQ_LEN
        )
        st.success(f"Next word: **{next_word}**")

# -----------------------------
# Optional: Generate multiple words
# -----------------------------
st.subheader("Generate Multiple Words")

num_words = st.slider("Number of words", 1, 20, 5)

if st.button("Generate Sentence"):
    result = input_text
    for _ in range(num_words):
        next_word = predict_next_word(
            result, model, tokenizer, MAX_SEQ_LEN
        )
        result += " " + next_word
    st.info(result)
