# AI Agent for Data Extraction
AI Agent for Web Search and Information Extraction
Overview
This project is a Streamlit-based AI application that allows users to:

Upload a CSV file or connect to a Google Sheet.
Use a custom prompt to search and retrieve information for each entity (e.g., companies).
Process search results with OpenAI GPT (e.g., extract emails or other data).
View and download structured results.
Features
Upload CSV files or connect to Google Sheets.
Perform automated web searches for entities using a custom prompt.
Extract information using OpenAI GPT-3.5/4.
View and download the results in CSV format.
Setup Instructions
Prerequisites
Python 3.8 or above.
API keys for:
OpenAI: Sign up.
SerpAPI (or another search API): Sign up.
Google Sheets API: Guide to create credentials.
Steps to Set Up
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/AI_Agent_Project.git
cd AI_Agent_Project
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the project root and add your credentials:

plaintext
Copy code
OPENAI_API_KEY=your_openai_api_key
SEARCH_API_KEY=your_search_api_key
GOOGLE_CREDENTIALS_FILE=path_to_your_google_service_account.json
Run the app:

bash
Copy code
streamlit run app.py
Usage
Open the app in your browser (e.g., http://localhost:8501).
Upload a CSV file with entities (e.g., company names).
Enter a custom prompt (e.g., "Get me the email address of {entity}").
Click "Run Search and Extraction."
View the extracted data and download it as a CSV file.
File Descriptions
File/Folder	Description
app.py	Main application file for Streamlit.
config.py	Loads API keys and configuration from .env.
requirements.txt	Lists all Python dependencies required for the project.
.env	Stores sensitive API keys (ignored in .gitignore).
utils/data_handler.py	Functions to handle CSV uploads and Google Sheets integration.
utils/search_api.py	Handles integration with SerpAPI or another web search API.
utils/llm_processing.py	Uses OpenAI GPT to process search results and extract relevant information.
utils/utils.py	Contains helper functions for error handling or formatting.
Dependencies
Python Libraries:
streamlit: For building the dashboard interface.
pandas: For handling CSV and structured data.
openai: For interacting with OpenAI GPT.
google-auth, google-auth-oauthlib, google-api-python-client: For Google Sheets integration.
requests: For working with web APIs.
python-dotenv: For managing environment variables.
Acknowledgments
OpenAI for GPT-3.5/4.
SerpAPI for search engine result extraction.
Google Sheets API for data integration.
3. .gitignore File
Ensure your sensitive files (like .env) and unnecessary files (e.g., __pycache__) are not pushed to GitHub.

Example .gitignore:

plaintext
Copy code
.env
__pycache__/
*.pyc
*.pyo
*.log
*.json
4. Upload to GitHub
Initialize Git:

bash
Copy code
git init
Add Files and Commit:

bash
Copy code
git add .
git commit -m "Initial commit for AI Agent Project"
Push to GitHub: Create a new repository on GitHub (e.g., AI_Agent_Project) and push the code:

bash
Copy code
git remote add origin https://github.com/your_username/AI_Agent_Project.git
git branch -M main
git push -u origin main
5. Verify and Share
Confirm the repository is accessible on GitHub.
Share the link to your repository for others to test or evaluate.
Let me know if you have further questions!






You've reached your limit for using GPTs.

## Project Description
This application allows users to upload a CSV or connect a Google Sheet and run web searches to extract information based on a user-defined prompt.

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
