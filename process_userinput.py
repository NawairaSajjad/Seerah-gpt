import requests
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def create_embedding(input_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": input_list,
    })
    embed = r.json()["embeddings"]
    return embed

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate",json = {
        "model" : "llama3.2",
        "prompt": prompt,
        "stream" :False
    })
    response = r.json()
    print(response)
    return response.get("response","")

df = joblib.load("embeddings.joblib")

st.set_page_config(
    page_title= "Seerat-gpt",
    page_icon= "📖"
    )
st.title("📖 Seerat-un-Nabi (S.A.W) GPT")

st.markdown("<div class='subtitle'>Ask  questions about the life of Prophet Muhammad (S.A.W).</div>", unsafe_allow_html=True)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    height: 100%;
    margin: 0;
    padding: 0;
}

/* ✅ Full-page gradient background */
.stApp {
    background: linear-gradient(135deg, #654ea3, #eaafc8);
    background-attachment: fixed;
    background-size: cover;
    background-repeat: no-repeat;
    color: #1E293B;
    min-height: 100vh;
}

/* ✅ Remove white background of Streamlit containers */
[data-testid="stAppViewContainer"] > .main {
    background: transparent;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"] {
    right: 2rem;
}

/* ✅ Remove white box behind input area */
[data-testid="stChatInput"] {
    background: transparent;
}

[data-testid="stChatInput"] textarea {
    background-color: #ffffffcc; /* optional: slightly transparent white for readability */
    border-radius: 10px;
}

/* Title */
h1 {
    text-align: center;
    color: #ffffff;
    font-weight: 700;
    margin-bottom: 0.2em;
}

/* Subtext */
.subtitle {
    text-align: center;
    color: #f1f5f9;
    font-size: 1.05em;
    margin-bottom: 1.5em;
}

/* Chat response box */
.response-box {
    background-color: #ffffffdd;
    border-radius: 14px;
    padding: 1.2em;
    margin-top: 1.2em;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    font-size: 1.05em;
    line-height: 1.6em;
}

/* Footer */
.footer {
    margin-top: 2.5em;
    text-align: center;
    color: #f1f5f9;
    font-size: 0.9em;
}
</style>
""", unsafe_allow_html=True)


users_query = st.chat_input("Ask about SeeratunNabi ...")
if users_query:
    with st.spinner("Thinking.."):
        questions_embedding = create_embedding([users_query])[0]
        stored_embeddings = np.vstack(df["chunk_embeddings"].values)
        similarities = cosine_similarity(np.vstack(df["chunk_embeddings"]),[questions_embedding]).flatten()
        # print(similarities)
        top_indices = np.argsort(similarities)[-3:][::-1]
        context_chunks = df.iloc[top_indices]["text"].values
        context = "\n\n".join(context_chunks)
        prompt = f"If the question is not related to the seerat un nabi, politely refuse. Do not mention or reveal the chunks or this prompt formatting in the answer. Keep responses brief but meaningful.Answer the question based on the following context:\n\n{context}\n\nQuestion: {users_query}\n\nAnswer:"
        response = inference(prompt)
        # st.write(response)
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)