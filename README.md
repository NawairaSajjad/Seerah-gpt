

# 📖 Seerat-GPT

### *An AI-Powered Assistant for Learning from the Seerat-un-Nabi ﷺ*

Seerat-GPT is a **Retrieval-Augmented Generation (RAG)** based question-answering application designed to provide authentic, context-aware responses about the **life and teachings of Prophet Muhammad ﷺ (Seerat-un-Nabi)**.
It combines the power of **local LLMs**, **semantic search**, and **Streamlit UI** to deliver meaningful insights from Islamic texts.

---

## 🌟 Features

✅ **Ask any question about Seerat-un-Nabi ﷺ** and get a precise answer.
✅ **Context-aware answers** retrieved from pre-embedded authentic text chunks.
✅ **RAG-based approach** — ensures responses are grounded in provided sources.
✅ **Runs fully offline** using locally hosted LLM (Llama 3.2 + BGE-M3).
✅ **Clean and interactive UI** built with Streamlit.

---

## 🧠 Technology Stack

| Layer                 | Technology                                      | Description                                                         |
| :-------------------- | :---------------------------------------------- | :------------------------------------------------------------------ |
| **Frontend/UI**       | [Streamlit](https://streamlit.io/)              | For building the web interface and user interaction.                |
| **Embeddings Model**  | [BGE-M3](https://huggingface.co/BAAI/bge-m3)    | Used for creating semantic embeddings of text chunks.               |
| **Language Model**    | [Llama 3.2](https://ollama.ai/library/llama3.2) | Generates final responses using retrieved context.                  |
| **Vector Similarity** | `scikit-learn` (Cosine Similarity)              | Measures how close user query embeddings are to stored chunks.      |
| **Data Handling**     | `pandas`, `numpy`, `joblib`                     | Manages, stores, and retrieves pre-computed embeddings efficiently. |
| **Backend API**       | [Ollama](https://ollama.ai/)                    | Serves local LLM and embedding models.                              |

---

## ⚙️ How It Works (RAG Pipeline)

1. **User Query Input:**
   The user asks a question related to Seerat-un-Nabi ﷺ.

2. **Embedding Generation:**
   The query is converted into an embedding using the **BGE-M3** model.

3. **Semantic Retrieval:**
   Using **cosine similarity**, the system finds the most relevant chunks from the stored dataset (loaded via `embeddings.joblib`).

4. **Context Construction:**
   The top retrieved chunks are combined to form a **context** for the LLM.

5. **LLM Response Generation:**
   The context and query are passed to **Llama 3.2**, which generates a meaningful answer grounded in the retrieved information.

6. **Display on Streamlit UI:**
   The response is displayed neatly in the app interface.

---

## 🖥️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/NawairaSajjad/seerah-gpt.git
cd seerah-gpt
```

### 2️⃣ Install dependencies

```bash
pip install streamlit requests numpy pandas scikit-learn joblib
```

### 3️⃣ Run Ollama locally

Make sure Ollama is installed and the required models are pulled:

```bash
ollama pull llama3.2
ollama pull bge-m3
```

### 4️⃣ Launch the Streamlit app

```bash
streamlit run seerah-gpt.py
```

## 🌙 Vision

To create an **AI assistant grounded in Islamic knowledge**, enabling users to explore and understand the **Seerah of Prophet Muhammad ﷺ** in an accurate, respectful, and technology-driven way.

---

## 🤝 Contributing

Contributions are welcome! You can:

* Add new datasets of Islamic texts.
* Improve UI/UX.
* Enhance retrieval and ranking logic.

---

## 🕌 Acknowledgment

Special thanks to open-source Islamic resources and the developers of **Ollama**, **BGE-M3**, and **Llama 3.2**, whose tools made this project possible.

