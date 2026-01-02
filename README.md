# 🗣️ Talk-to-Data: AI SQL Analyst

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-green?style=flat&logo=langchain)
![Groq](https://img.shields.io/badge/Groq-Llama3-orange?style=flat)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?style=flat&logo=streamlit)

### 🚀 Overview

**Talk-to-Data** is an intelligent AI agent designed to bridge the gap between non-technical users and relational databases. By leveraging **Large Language Models (LLMs)** and **LangChain**, this tool translates natural language questions into executable **SQL queries**, executes them against the database, and automatically **visualizes** the results.

Instead of writing complex SQL joins, users can simply ask:

> _"What is the total revenue per customer?"_

---

### 📸 Demo & Screenshots

**1. Data Visualization (Automatic Charts)**

![Visualization Demo](screenshots/chart_demo.png)

**2. Data Retrieval (Tabular View)**

![Table Demo](screenshots/table_demo.png)

---

### ✨ Key Features

- **🗣️ Natural Language to SQL:** Powered by **Groq (Llama-3.3-70b)** for ultra-fast and accurate SQL generation.
- **📊 Automatic Visualization:** Dynamically generates bar charts when the query results allow (e.g., Category vs. Count).
- **🔄 Dynamic Schema Extraction:** Uses **SQLAlchemy** to inspect the database structure on the fly, making the tool adaptable to any schema changes without code modification.
- **⚡ Zero-Setup Database:** Comes with a built-in script to generate a dummy E-commerce database (Customers, Orders, Products).

### 🛠️ Tech Stack

- **LLM Engine:** Groq API (Llama 3).
- **Orchestration:** LangChain (Prompt Templates & Chains).
- **Database:** SQLite & SQLAlchemy.
- **Frontend:** Streamlit.
- **Data Handling:** Pandas.

---

### 🏗️ How It Works

1.  **User Input:** The user asks a question via the Streamlit UI.
2.  **Schema Inspection:** The system scans the database tables and columns.
3.  **Prompt Engineering:** The Schema + User Question are sent to the LLM with a strict system prompt to generate valid SQL.
4.  **Execution:** The generated SQL is executed against the SQLite database.
5.  **Visualization:** If the result contains categorical and numerical data, a chart is rendered automatically.

---

### 💻 Installation & Usage

**1. Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/talk-to-data.git
cd talk-to-data
```
