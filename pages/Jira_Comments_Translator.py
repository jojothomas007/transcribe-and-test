import streamlit as st

from src.transcribe_test.dto.jira_issue_dto import Issue
from src.transcribe_test.service.jira_service import JiraService
from src.transcribe_test.service.translator import Translator
from src.transcribe_test.config import Config

def fetch_issue():
    issue:Issue = None
    st.session_state.issue = JiraService().get_issue(issue_key)
    st.session_state.description = st.session_state.issue.fields.description
    st.session_state.step = 1  # Move to the "fetch" step
    
st.set_page_config(
    page_title="Jira Comments Translator",
    page_icon="📚"
)

st.header('📚 Jira Comments Translator')
st.subheader('Translates text from Jira Issue comments.')

issue_key = st.text_input("Jira Issue key for Translation:", disabled=(st.session_state.step >= 1))
Config.load_config()
# Fetch Jira issue details
st.button("Fetch", disabled=(st.session_state.step >= 1), on_click=fetch_issue)
 