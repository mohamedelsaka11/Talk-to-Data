import os
import json
import re
import sqlite3
from sqlalchemy import create_engine, inspect
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq  
from dotenv import load_dotenv
from langchain.chains import LLMChain  


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = api_key

db_url = "sqlite:///amazon.db"

def extract_schema(db_url):
    engine = create_engine(db_url)
    inspector = inspect(engine)
    schema = {}
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema[table_name] = [col['name'] for col in columns]
    return json.dumps(schema)

def text_to_sql(schema, prompt):
    SYSTEM_PROMPT = """
    You are an expert SQL generator. Given a database schema and a user prompt, generate a valid SQL query that answers the prompt. 
    Only use the tables and columns provided in the schema. ALWAYS ensure the SQL syntax is correct and avoid using any unsupported features. 
    Output only the SQL as your response will be directly used to query data from the database. No preamble please. Do not use <think> tags.
    """

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "Schema:\n{schema}\n\nQuestion: {user_prompt}\n\nSQL Query:")
    ])

    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, api_key=api_key)

    chain = LLMChain(prompt=prompt_template, llm=model)
    raw_response = chain.run({"schema": schema, "user_prompt": prompt})
    cleaned_response = re.sub(r"<think>.*?</think>", "", raw_response, flags=re.DOTALL)
    return cleaned_response.strip()

def get_data_from_database(prompt):
    schema = extract_schema(db_url)
    sql_query = text_to_sql(schema, prompt)
    conn = sqlite3.connect("amazon.db")
    cursor = conn.cursor()
    try:
        res = cursor.execute(sql_query)
        results = res.fetchall()
    except sqlite3.Error as e:
        print("SQL Error:", e)
        results = []
    conn.close()
    return results

