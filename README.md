# 🧮 StatMate – AI Statistics Assistant

**StatMate** is an intelligent statistics chatbot and computation tool built with **Streamlit**, **LangChain**, and **Ollama**.  
It allows users to upload data, chat about statistical concepts, and automatically perform the appropriate test — all locally, with **no API keys or cloud dependencies**.

---

## 🚀 Features

- 💬 **AI Chatbot** – Ask theoretical questions like *“What is random sampling?”* or *“When to use ANOVA?”*  
- 📊 **Automatic Test Selection** – Detects and performs statistical tests such as:
  - Independent t-test  
  - Paired t-test  
  - ANOVA  
  - Correlation  
  - Descriptive statistics  
- 📂 **Upload CSV/Excel** – Analyze your own datasets directly.  
- 🧠 **Local LLM Integration** – Powered by **Llama 3** running via **Ollama**.  
- 🔒 **Private & Offline** – No internet or external API calls required.

---

## 🧩 Tech Stack (Backbone)

| Layer | Technology |
|-------|-------------|
| **Frontend / UI** | [Streamlit](https://streamlit.io) |
| **AI Layer** | [LangChain](https://www.langchain.com) + [Ollama](https://ollama.com) |
| **Statistical Engine** | NumPy, SciPy, Pandas |
| **Model** | `llama3:8b` (customizable to smaller models like `llama3:latest`) |

---

## ⚙️ Installation & Run Locally

### 1️⃣ Prerequisites
- [Python 3.9+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com) installed on your machine
- Llama 3 model pulled locally:
  ```bash
  ollama pull llama3:8b
  ```

### 2️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/statmate.git
cd statmate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
streamlit run main.py
```

The app will automatically start the Ollama server if it’s not already running.

---

## 🧠 How It Works

1. StatMate ensures Ollama is active locally (`ollama serve`).  
2. When you enter a question:
   - If it’s theoretical → StatMate uses **Llama 3** to explain it.
   - If a dataset is uploaded → it decides which test to apply and runs the computation.
3. The result (statistics or explanation) is displayed instantly in Streamlit.

---

## 📁 Project Structure

```
├── app.py               # Auto-starts Ollama server
├── llm_utils.py         # AI model and logic (LLM wrappers)
├── main.py              # Streamlit interface (chat + computation)
├── stats_engine.py      # Statistical test implementations
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ⚡ Example Questions

- “What is random sampling?”  
- “Compare pre-test and post-test scores.”  
- “Is there a correlation between height and weight?”  
- “Show descriptive stats for my dataset.”

---

## 🧩 Customization

Change the model in `llm_utils.py`:
```python
llm = OllamaLLM(model="llama3:latest")  # or "llama3:1b" for faster performance
```

---

## 📜 License & Copyright

```
© 2025 Nguyễn Công Thịnh.  
All rights reserved.

This project is for educational and personal research use only.
You may fork or modify it with proper attribution.
```

---

## 💡 Acknowledgements

- [Streamlit](https://streamlit.io) for interactive UI.  
- [LangChain](https://www.langchain.com) for LLM orchestration.  
- [Ollama](https://ollama.com) for local LLM deployment.  
- [Llama 3](https://llama.meta.com/) by Meta for the underlying model.

---

**StatMate – Chat. Analyze. Understand.**
