# 📄 Legal Docs RAG Chatbot

A Generative AI-powered chatbot that allows users to upload legal documents and ask natural language questions. It uses **LangChain**, **FAISS**, and **OpenAI** to retrieve relevant context and generate accurate answers in real-time.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)

---

## 🔍 Features

- Upload `.txt` legal documents
- Automatically chunk, embed & store docs in FAISS
- Ask questions using natural language
- Retrieves accurate, context-aware answers from OpenAI
- Built with **LangChain**, **FAISS**, **Streamlit**, and **OpenAI API**

---

## 🚀 Tech Stack

- **LLM:** OpenAI GPT-3.5 / GPT-4 (via `ChatOpenAI`)
- **Embeddings:** OpenAIEmbeddings (`langchain_community`)
- **Vector Store:** FAISS
- **Frontend:** Streamlit
- **Framework:** LangChain RAG Pipeline
- **Cloud Ready:** Deployable on Streamlit Cloud

---

## 🧪 Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rohitpote-15/legal-docs-rag-chatbot.git
cd legal-docs-rag-chatbot
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file by copying the template:

```bash
cp .env.template .env
```

Then open `.env` and paste your OpenAI key like this:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. Run the Streamlit App

```bash
streamlit run src/app.py
```

---

## 🖼️ Screenshot

<img width="1919" height="1028" alt="image" src="https://github.com/user-attachments/assets/4d0ffda9-99a5-4df7-8c14-f9e6264d3300" />

<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/9f815046-b594-4803-96ea-c3d964bad91d" />

---

## ☁️ Optional Deployment (Streamlit Cloud)

Want to deploy this for public use?
Follow these steps:

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Connect your GitHub repo
3. Deploy using `src/app.py` as the main file
4. Set `OPENAI_API_KEY` under “Secrets”

Your live app will be at:

```
https://<your-project-name>.streamlit.app
```

---

## 🧑‍💻 Author

**Rohit Pote**

* 💼 AI/ML Engineer | LLM Architect | Prompt Engineer
* 🌐 [LinkedIn](https://www.linkedin.com/in/rohitrajupote/)
* 📬 [rohitrajupote97@gmail.com](mailto:rohitrajupote97@gmail.com)
* https://legal-docs-rag-chatbot.streamlit.app/
---

## ⭐️ Star This Repo

If you found this project helpful, please consider giving it a star — it helps others find and learn from it!

```

---

### ✅ What To Do Next:
- Paste this into your GitHub `README.md` file.
- Replace the `![Screenshot](...)` link with a screenshot or GIF of your app.
- Add your Streamlit Cloud link once you deploy it.

Need help with screenshot, deployment, or demo link setup? Just let me know — we’ll finish this strong 💼🚀
```
