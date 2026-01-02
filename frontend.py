import streamlit as st
import pandas as pd
from main import get_data_from_database

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Data Analyst")
st.markdown("Ask questions about your data in natural language.")

user_query = st.text_area("💬 Enter your question:", placeholder="e.g., Total products sold per category")

def format_results(results):
    """Convert raw SQL results into a DataFrame."""
    if not results:
        return None
    try:
        df = pd.DataFrame(results)
        return df
    except Exception as e:
        return None

def visualize_data(df):
    """
    Automatic Visualization Logic:
    If the dataframe has at least 2 columns (one text, one number), plot a chart.
    """
    if df is None or df.empty:
        return
    if len(df.columns) >= 2 and len(df) > 1:
        x_col = df.columns[0] 
        y_col = df.columns[-1] 

        if pd.api.types.is_numeric_dtype(df[y_col]):
            st.markdown("### 📊 Data Visualization")
            chart_data = df.set_index(x_col)
            st.bar_chart(chart_data[y_col])
        else:
            numeric_cols = df.select_dtypes(include=['number']).columns
            if len(numeric_cols) > 0:
                st.markdown("### 📊 Data Visualization")
                st.bar_chart(df[numeric_cols[0]])

if st.button("Analyze"):
    if user_query.strip() == "":
        st.warning("Please enter a question to analyze.")
    else:
        with st.spinner("Analyzing your query..."):
            database_response = get_data_from_database(user_query)
            df_response = format_results(database_response)

        st.success("Analysis complete!")
        
        if df_response is not None:
            st.dataframe(df_response)
            visualize_data(df_response)
        else:
            st.warning("No results found or could not process data.")

st.markdown("""
    <style>
    textarea {
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)