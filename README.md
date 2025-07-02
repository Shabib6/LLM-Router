# 🧠 LLM Router

> A Smart, Multi-Model Query Router Built by Shabib 

LLM Router intelligently routes user queries to the most suitable Large Language Model (LLM) from a pool of models like GPT-4, DeepSeek Coder, Gemini, Mistral, and LLaMA 3 — based on the query’s nature. It ensures maximum performance, efficiency, and cost-effectiveness by selecting the right model for the right task.

---

## 🚀 Features

- 🔁 Dynamic LLM selection (GPT-4, Gemini, DeepSeek, Mistral, LLaMA 3)
- 🧠 Smart system prompt logic powered by GPT-4o
- 💻 Offline support using Ollama for Mistral & LLaMA 3
- 🔒 API key support for secure integration
- ⚙️ Customizable prompts per model
- 🧪 Terminal-based live query testing

---

## 🛠️ Tech Stack

- **Python 3.12+**
- `OpenAI` SDK
- `google-generativeai`
- `requests`
- `dotenv`
- `Ollama` for running open-source LLMs locally

---

## 🧩 Supported Models

| Model     | Provider       | Use Case                                                 |
|-----------|----------------|-----------------------------------------------------------|
| GPT-4     | OpenAI         | Creative writing, brainstorming, general reasoning        |
| Gemini    | Google         | Real-world knowledge, factual Q&A, current events         |
| DeepSeek  | DeepSeek Coder | Code generation, debugging, algorithms                    |
| Mistral   | Ollama         | Fast summarization, safe dialogue, lightweight queries     |
| LLaMA 3   | Ollama         | Offline reasoning, general-purpose private interactions   |

---

## 📦 Setup Instructions

```bash
# 1. Clone the Repo
git clone https://github.com/yourusername/llm-router.git
cd llm-router

# 2. Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate      # On Windows

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Create a `.env` file in the root folder and add your API keys:
## 🔐 .env File

Create a `.env` file in the root directory and add the following:

```env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
