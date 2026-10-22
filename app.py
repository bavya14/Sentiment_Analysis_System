import streamlit as st
from textblob import TextBlob
import re
from collections import Counter

st.set_page_config(
    page_title="SentimentScope | Text Sentiment Analyzer",
    page_icon="💬",
    layout="wide",
)

st.markdown("""
<style>
    .main-title {font-size: 2.35rem; font-weight: 750; margin-bottom: 0.15rem;}
    .subtitle {color: #6b7280; margin-bottom: 1.4rem;}
    .result-card {padding: 1.15rem; border: 1px solid rgba(128,128,128,.25);
                  border-radius: 14px; min-height: 120px;}
    .result-label {font-size: .9rem; color: #6b7280; margin-bottom: .25rem;}
    .result-value {font-size: 1.65rem; font-weight: 700;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💬 SentimentScope</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">A simple NLP application that identifies the sentiment '
    'expressed in text.</div>',
    unsafe_allow_html=True,
)

st.info(
    "This demo uses TextBlob's English sentiment analyzer. It is useful for learning "
    "and experimentation, but it may misread sarcasm, slang, mixed opinions, and context."
)

EXAMPLES = {
    "Positive": "I absolutely love this product. It is easy to use and works wonderfully!",
    "Negative": "I am disappointed with the service. The delivery was late and the support was unhelpful.",
    "Neutral": "The package arrived on Tuesday and contains three items.",
    "Mixed": "The camera takes beautiful photos, but the battery life is terrible.",
}

with st.sidebar:
    st.header("Try an example")
    choice = st.selectbox("Choose sample text", ["Write my own"] + list(EXAMPLES.keys()))
    st.caption("Choose a sample to fill the text area.")
    st.divider()
    st.markdown("### How scoring works")
    st.markdown(
        "- **Polarity:** ranges from −1 (negative) to +1 (positive).\n"
        "- **Subjectivity:** ranges from 0 (objective) to 1 (subjective).\n"
        "- **Label:** assigned using the polarity score."
    )
    st.markdown("### Project details")
    st.caption("Python · Streamlit · TextBlob · NLP")

default_text = EXAMPLES.get(choice, "")
if choice == "Write my own":
    default_text = ""

text = st.text_area(
    "Enter text to analyze",
    value=default_text,
    height=180,
    placeholder="Type a review, comment, message, or paragraph here...",
    help="For the most meaningful results, enter English text.",
)

col_a, col_b = st.columns([1, 4])
with col_a:
    analyze = st.button("Analyze sentiment", type="primary", use_container_width=True)
with col_b:
    st.caption(f"Characters: {len(text):,} · Words: {len(re.findall(r'\\b\\w+\\b', text)):,}")

def classify_sentiment(polarity: float) -> str:
    """Map polarity to a simple sentiment label."""
    if polarity > 0.05:
        return "Positive"
    if polarity < -0.05:
        return "Negative"
    return "Neutral"

def get_metrics(value: str):
    blob = TextBlob(value)
    sentiment = blob.sentiment
    return {
        "polarity": float(sentiment.polarity),
        "subjectivity": float(sentiment.subjectivity),
        "label": classify_sentiment(float(sentiment.polarity)),
    }

if analyze:
    if not text.strip():
        st.warning("Please enter some text before analyzing.")
    else:
        metrics = get_metrics(text.strip())
        st.divider()
        st.subheader("Analysis results")

        label = metrics["label"]
        emoji = {"Positive": "😊", "Negative": "☹️", "Neutral": "😐"}[label]
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(
                f'<div class="result-card"><div class="result-label">Sentiment</div>'
                f'<div class="result-value">{emoji} {label}</div></div>',
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f'<div class="result-card"><div class="result-label">Polarity</div>'
                f'<div class="result-value">{metrics["polarity"]:.3f}</div></div>',
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                f'<div class="result-card"><div class="result-label">Subjectivity</div>'
                f'<div class="result-value">{metrics["subjectivity"]:.3f}</div></div>',
                unsafe_allow_html=True,
            )

        st.markdown("#### Polarity scale")
        st.caption("Negative ← 0 → Positive")
        st.progress((metrics["polarity"] + 1) / 2)

        st.markdown("#### Text statistics")
        words = re.findall(r"\b[\w']+\b", text)
        sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
        stats1, stats2, stats3, stats4 = st.columns(4)
        stats1.metric("Words", len(words))
        stats2.metric("Characters", len(text))
        stats3.metric("Sentences", len(sentences))
        stats4.metric("Unique words", len(set(w.lower() for w in words)))

        with st.expander("View most common words"):
            normalized = [w.lower() for w in words if len(w) > 2]
            common = Counter(normalized).most_common(8)
            if common:
                st.write(", ".join(f"**{word}** ({count})" for word, count in common))
            else:
                st.write("No words long enough to display.")

        st.caption(
            "Note: Sentiment predictions are approximate and should not be treated as "
            "a definitive measure of a person's feelings."
        )

st.divider()
st.markdown(
    "<div style='text-align:center;color:#6b7280;font-size:.85rem;'>"
    "Built with Python, Streamlit, and TextBlob · Educational NLP project</div>",
    unsafe_allow_html=True,
)
