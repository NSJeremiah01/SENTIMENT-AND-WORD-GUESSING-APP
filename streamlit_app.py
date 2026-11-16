import streamlit as st
from transformers import pipeline


st.set_page_config(page_title="My AI App")
st.title("SENTIMENT AND WORD GUESSING APP")

st.write("The Streamlit app is running.")
st.success("Testing the app interface.")

# Load each model only once, then keep it in memory(this saves time and memory )
@st.cache_resource
def load_sentiment_model():
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
  )
  
@st.cache_resource
def load_fill_mask_model():
    return pipeline("fill-mask", model="distilbert-base-uncased")
  
  # The special symbol that hides a word (it is [MASK] for this model) 
  
tab1, tab2 = st.tabs(["Sentiment", "Missing word"])
  
  # Tab 1: is the sentence positive or negative?
with tab1:
    st.write("Type  sentence. The model will say if it is POSITIVE or NEGATIVE.")
    text = st.text_area("Your sentence", "I love learning about artificial intelligence")
    
    if st.button("Check sentiment"):
      if not text.strip():
        st.warning("please type a sentence first.")
      else:
        with st.spinner("Thinking..."):
          result = load_sentiment_model()(text, truncation=True)[0]
        message = f"{result['label']} (score: {round(result['score'], 3)})" 
        if result["label"] == "POSITIVE":
          st.success(message)
        else:
          st.error(message)
          
# Tab 2: guess the hidden word
with tab2:
  st.write("Enter a sentence and replace one word with [MASK].")

masked_text = st.text_input(
    "Your sentence",
    "The sun rises in the [MASK]."
)

if st.button("Guess missing word"):
    if "[MASK]" not in masked_text:
        st.warning("Please include [MASK] in your sentence.")
    else:
        with st.spinner("Guessing..."):
            result = load_fill_mask_model()(masked_text)

        st.write("Possible words:")
        for prediction in result:
          word = prediction["token_str"]
          score = prediction["score"]

          st.write(f"**{word}**")
          st.progress(score)
          st.caption(f"Score: {score:.2%}")
          

    