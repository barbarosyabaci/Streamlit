"""Runtime configuration for the independently deployed RAN application."""
import hmac
import os
import streamlit as st
from pymongo import MongoClient
from pymongo.errors import PyMongoError


def setting(name, default=""):
    value = os.environ.get(name)
    if value is not None:
        return value
    try:
        return st.secrets.get(name, default)
    except FileNotFoundError:
        return default


def get_mongo_uri():
    uri = setting("MONGODB_URI")
    if not uri:
        st.info("Online database is not configured yet. CSV upload remains available. "
                "The app owner can add MONGODB_URI in Streamlit Cloud Secrets.")
        st.stop()
    return uri


@st.cache_resource(show_spinner=False)
def mongo_client(uri, **kwargs):
    client = MongoClient(uri, serverSelectionTimeoutMS=10000,
                         connectTimeoutMS=10000, **kwargs)
    try:
        client.admin.command("ping")
    except PyMongoError:
        client.close()
        st.error("The online database could not be reached. Check database connection "
                 "and network access settings, or upload CSV files.")
        st.stop()
    return client


def require_admin():
    expected = setting("ADMIN_PASSWORD")
    if not expected:
        st.info("Database administration requires an ADMIN_PASSWORD in the app's Secrets.")
        st.stop()
    supplied = st.text_input("Administrator password", type="password")
    if not hmac.compare_digest(supplied.encode(), str(expected).encode()):
        if supplied:
            st.error("Incorrect administrator password.")
        st.stop()
