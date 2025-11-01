import streamlit as st
from pipeline.pipeline import AnimeRecommenderPipeline
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Anime Recommender", layout="wide")

@st.cache_resource
def init_pipeline():
    return AnimeRecommenderPipeline()

pipeline = init_pipeline()
st.title("Anime Recommender System")

query = st.text_input("Enter an anime description or title:")

if query:
    with st.spinner("Finding recommendations..."):
        response = pipeline.get_recommendations(query)
        st.markdown("### Recommendations based on your input:")
        st.write(response)
