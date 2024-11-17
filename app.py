import streamlit as st
import pandas as pd
from utils.data_handler import load_data, authenticate_google_sheets
from utils.search_api import SearchAPI
from utils.llm_processing import process_with_llm

st.title("AI Agent for Data Extraction")

# File upload
uploaded_file = st.file_uploader("Upload CSV or connect Google Sheet", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Data preview:", data.head())
    primary_column = st.selectbox("Select the main entity column", data.columns)

    # User prompt input
    prompt_template = st.text_input("Enter query (e.g., 'Get me the email address of {company}')")

    if st.button("Start Extraction"):
        results = []
        for entity in data[primary_column].unique():
            # Web search
            query = prompt_template.replace("{company}", entity)
            search_results = SearchAPI().search(query)

            # LLM processing
            parsed_data = process_with_llm(search_results, entity)
            results.append(parsed_data)

        results_df = pd.DataFrame(results)
        st.write("Extracted Data", results_df)

        # Download option
        st.download_button("Download CSV", results_df.to_csv(index=False), "extracted_data.csv")
