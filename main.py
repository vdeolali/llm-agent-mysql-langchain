from dotenv import load_dotenv
import streamlit as st

load_dotenv()

from langchain_community.utilities import SQLDatabase

def init_connection(u, p, h, d) -> SQLDatabase:
    uri = f"mysql+mysqlconnector://{u}:{p}@{h}:3306/{d}"
    return SQLDatabase.from_uri(uri, include_tables=['album', 'artist', 'customer', 'employee', 'genre', 'invoice', 'invoiceline', 'mediatype', 'playlist', 'playlisttrack', 'track'])



def connect_to_mysql(host, port, user, password, database):
    uri = f"mysql+mysqlconnector://root:kako1i12@localhost:3306/Chinook"
    db = SQLDatabase.from_uri(uri, include_tables=['album', 'artist', 'customer', 'employee', 'genre', 'Invoice', 'invoiceline','mediatype', 'playlist','playlisttrack', 'track'])
st.set_page_config(page_title="Chat with data in mysql", page_icon=":books:")
st.title("Talk to MySQL 💬")

with st.sidebar:
    st.subheader("Settings")
    st.write("Chat with your tables in MySQL")
    st.text_input("Host", value="localhost")   
    st.text_input("Port", value="3306")
    st.text_input("User", value="root")
    st.text_input("Password", value="kako1i12", type="password")
    st.text_input("Database", value="Chinook")
    
    if st.button("Connect to MySQL"):
        print ("Yep")
        with st.spinner("Connecting to MySQL..."):
            db = init_connection("root", "kako1i12", "localhost", "Chinook")
            st.session_state.db = db
            st.success("Connected to MySQL!")





st.chat_input("Enter your query here...")
