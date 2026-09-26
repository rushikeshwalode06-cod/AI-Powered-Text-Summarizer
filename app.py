import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

/* =========================
   GLOBAL
========================= */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(124, 58, 237, 0.22),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(236, 72, 153, 0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(59, 130, 246, 0.10),
            transparent 30%
        ),
        #070711;
    color: #ffffff;
}

/* Main width */

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0b0a18 0%,
            #10091c 50%,
            #090812 100%
        );
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #ffffff !important;
}

/* =========================
   HERO
========================= */

.hero-box {
    position: relative;
    overflow: hidden;

    padding: 42px;
    border-radius: 28px;

    background:
        linear-gradient(
            135deg,
            rgba(124, 58, 237, 0.30),
            rgba(168, 85, 247, 0.12),
            rgba(236, 72, 153, 0.18)
        );

    border: 1px solid rgba(168, 85, 247, 0.35);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.45),
        inset 0 1px 0 rgba(255,255,255,0.08);

    margin-bottom: 32px;
}

.hero-box:before {
    content: "";
    position: absolute;

    width: 250px;
    height: 250px;

    background: rgba(168,85,247,0.18);

    filter: blur(80px);

    right: -80px;
    top: -100px;
}

.hero-badge {
    display: inline-block;

    padding: 8px 16px;

    border-radius: 30px;

    background: rgba(255,255,255,0.08);

    border: 1px solid rgba(255,255,255,0.16);

    color: #e9d5ff;

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 1.4px;

    margin-bottom: 18px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;

    line-height: 1.1;

    margin: 0;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #ddd6fe,
            #f9a8d4
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    color: #cbd5e1;

    font-size: 17px;

    max-width: 850px;

    line-height: 1.7;

    margin-top: 15px;
}

/* =========================
   SECTION HEADERS
========================= */

.section-title {
    font-size: 25px;

    font-weight: 800;

    color: #ffffff;

    margin-top: 28px;
    margin-bottom: 14px;
}

.section-subtitle {
    color: #94a3b8;

    font-size: 14px;

    margin-bottom: 14px;
}

/* =========================
   TEXT AREA
========================= */

textarea {
    background:
        linear-gradient(
            145deg,
            rgba(17,16,31,0.98),
            rgba(12,11,24,0.98)
        ) !important;

    color: #f8fafc !important;

    border: 1px solid rgba(139,92,246,0.30) !important;

    border-radius: 18px !important;

    padding: 18px !important;

    font-size: 15px !important;

    line-height: 1.7 !important;

    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.03),
        0 10px 35px rgba(0,0,0,0.18) !important;
}

textarea:focus {
    border: 1px solid rgba(168,85,247,0.75) !important;

    box-shadow:
        0 0 0 2px rgba(168,85,247,0.10),
        0 15px 40px rgba(0,0,0,0.25) !important;
}

/* =========================
   GENERATE BUTTON
========================= */

.stButton > button {
    min-height: 52px;

    border-radius: 15px;

    border: 1px solid rgba(255,255,255,0.15);

    background:
        linear-gradient(
            135deg,
            #7c3aed,
            #9333ea,
            #db2777
        );

    color: white;

    font-size: 16px;

    font-weight: 800;

    box-shadow:
        0 12px 30px rgba(124,58,237,0.30);

    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);

    box-shadow:
        0 18px 40px rgba(168,85,247,0.40);
}

/* =========================
   METRIC CARDS
========================= */

div[data-testid="stMetric"] {
    min-height: 135px;

    padding: 22px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(23,21,42,0.96),
            rgba(13,12,26,0.96)
        );

    border: 1px solid rgba(139,92,246,0.25);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.28);

    transition: all 0.25s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-4px);

    border-color:
        rgba(168,85,247,0.55);

    box-shadow:
        0 20px 45px rgba(0,0,0,0.35);
}

div[data-testid="stMetricLabel"] {
    color: #a78bfa !important;

    font-weight: 700 !important;
}

div[data-testid="stMetricValue"] {
    color: #ffffff !important;

    font-size: 28px !important;

    font-weight: 800 !important;
}

/* =========================
   CODE / COPY BOX
========================= */

div[data-testid="stCode"] {
    border-radius: 18px !important;

    border: 1px solid rgba(139,92,246,0.30) !important;

    box-shadow:
        0 15px 40px rgba(0,0,0,0.25) !important;
}

/* =========================
   DOWNLOAD BUTTON
========================= */

.stDownloadButton > button {
    width: 100%;

    min-height: 52px;

    border-radius: 15px;

    border: 1px solid rgba(255,255,255,0.10);

    background:
        linear-gradient(
            135deg,
            #ec4899,
            #8b5cf6
        );

    color: white;

    font-weight: 800;

    box-shadow:
        0 12px 30px rgba(236,72,153,0.20);

    transition: all 0.25s ease;
}

.stDownloadButton > button:hover {
    transform: translateY(-3px);

    box-shadow:
        0 18px 40px rgba(236,72,153,0.30);
}

/* =========================
   INFO CARDS
========================= */

.info-card {
    padding: 24px;

    min-height: 145px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(24,22,43,0.95),
            rgba(13,12,27,0.95)
        );

    border: 1px solid rgba(139,92,246,0.22);

    box-shadow:
        0 12px 35px rgba(0,0,0,0.25);
}

.info-icon {
    font-size: 26px;

    margin-bottom: 10px;
}

.info-title {
    color: #ffffff;

    font-size: 16px;

    font-weight: 800;
}

.info-text {
    color: #94a3b8;

    font-size: 13px;

    margin-top: 7px;
}

/* =========================
   DIVIDER
========================= */

.gradient-line {
    height: 1px;

    margin: 35px 0;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(168,85,247,0.55),
            rgba(236,72,153,0.55),
            transparent
        );
}

/* =========================
   STATUS CARD
========================= */

.status-card {
    padding: 15px 18px;

    border-radius: 15px;

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    margin-bottom: 10px;
}

.status-green {
    color: #86efac;
    font-weight: 700;
}

.status-purple {
    color: #c4b5fd;
    font-weight: 700;
}

/* =========================
   FOOTER
========================= */

.footer {
    text-align: center;

    margin-top: 45px;

    padding: 25px;

    color: #64748b;

    font-size: 13px;

    border-top: 1px solid rgba(255,255,255,0.06);
}

/* =========================
   ALERTS
========================= */

div[data-testid="stAlert"] {
    border-radius: 15px !important;
}

/* =========================
   MOBILE
========================= */

@media (max-width: 768px) {

    .hero-box {
        padding: 28px;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-description {
        font-size: 14px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# MODEL CONFIG
# =========================================================

MODEL_NAME = "rushikeshwalode/summarization_model"


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_NAME
    )

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    model.to(device)

    model.eval()

    return tokenizer, model, device


# =========================================================
# LOAD
# =========================================================

with st.spinner("✨ Loading AI model..."):

    tokenizer, model, device = load_model()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ✨ AI Summarizer")

    st.caption(
        "Intelligent Text Summarization Dashboard"
    )

    st.markdown("---")

    st.markdown("### 🤖 Model")

    st.markdown(
        '<div class="status-card">'
        '<span class="status-purple">T5-Small</span>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("### ⚡ Device")

    if torch.cuda.is_available():

        st.markdown(
            '<div class="status-card">'
            '<span class="status-green">🚀 GPU Enabled</span>'
            '</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<div class="status-card">'
            '<span class="status-purple">💻 CPU Mode</span>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown("### 📌 Features")

    st.write("✨ AI Text Summarization")
    st.write("📄 Original Text Preview")
    st.write("📊 Summary Statistics")
    st.write("📋 One-Click Copy")
    st.write("⬇️ Download Summary")
    st.write("⚡ GPU / CPU Support")

    st.markdown("---")

    st.caption(
        "Powered by Hugging Face Transformers"
    )


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero-box">

<div class="hero-badge">
✨ AI POWERED • TEXT SUMMARIZATION
</div>

<div class="hero-title">
Transform Long Text Into Smart Summaries
</div>

<div class="hero-description">
Turn lengthy articles, reports and documents into concise,
meaningful and easy-to-read summaries using your trained
T5 Transformer model.
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">📝 Enter Your Text</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Paste your article, report, document or any long text below.'
    '</div>',
    unsafe_allow_html=True
)

input_text = st.text_area(
    "Input Text",
    height=280,
    placeholder=(
        "Start typing or paste your long text here..."
    ),
    label_visibility="collapsed"
)


# =========================================================
# GENERATE BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

button_col1, button_col2, button_col3 = st.columns(
    [1, 2, 1]
)

with button_col2:

    summarize_clicked = st.button(
        "✨  GENERATE AI SUMMARY",
        use_container_width=True
    )


# =========================================================
# SUMMARY FUNCTION
# =========================================================

def generate_summary(text):

    inputs = tokenizer(
        "summarize: " + text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():

        output_ids = model.generate(
            **inputs,
            max_new_tokens=128,
            min_new_tokens=20,
            num_beams=4,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

    summary = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True
    )

    return summary


# =========================================================
# GENERATE SUMMARY
# =========================================================

if summarize_clicked:

    if not input_text.strip():

        st.warning(
            "⚠️ Please enter some text before generating a summary."
        )

    else:

        with st.spinner(
            "🤖 AI is analyzing your text and generating a summary..."
        ):

            try:

                summary = generate_summary(
                    input_text
                )

                st.session_state["summary"] = summary

                st.session_state[
                    "original_text"
                ] = input_text

            except Exception as e:

                st.error(
                    f"❌ Error while generating summary: {e}"
                )


# =========================================================
# RESULTS
# =========================================================

if "summary" in st.session_state:

    summary = st.session_state["summary"]

    original_text = st.session_state[
        "original_text"
    ]

    # -----------------------------------------------------
    # DIVIDER
    # -----------------------------------------------------

    st.markdown(
        '<div class="gradient-line"></div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # ORIGINAL TEXT
    # =====================================================

    st.markdown(
        '<div class="section-title">📄 Original Text</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Your original input is preserved below.'
        '</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "Original",
        value=original_text,
        height=230,
        disabled=True,
        label_visibility="collapsed"
    )


    # =====================================================
    # GENERATED SUMMARY
    # =====================================================

    st.markdown(
        '<div class="section-title">✨ AI Generated Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Your concise AI-generated summary is ready.'
        '</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "Summary",
        value=summary,
        height=220,
        key="summary_output",
        label_visibility="collapsed"
    )


    # =====================================================
    # COPY & DOWNLOAD
    # =====================================================

    st.markdown(
        '<div class="section-title">📋 Copy & Save</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Copy the generated summary instantly or save it as a text file.'
        '</div>',
        unsafe_allow_html=True
    )

    copy_col, download_col = st.columns(
        [1.4, 1]
    )

    # -----------------------------------------------------
    # COPY
    # -----------------------------------------------------

    with copy_col:

        st.markdown(
            "#### 📋 Copy Summary"
        )

        st.caption(
            "Use the copy icon in the top-right corner."
        )

        # Native Streamlit copy functionality
        st.code(
            summary,
            language=None
        )

    # -----------------------------------------------------
    # DOWNLOAD
    # -----------------------------------------------------

    with download_col:

        st.markdown(
            "#### ⬇️ Save Summary"
        )

        st.caption(
            "Download your generated summary."
        )

        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )

        st.download_button(
            label="⬇️  DOWNLOAD SUMMARY",
            data=summary,
            file_name="AI_Summary.txt",
            mime="text/plain",
            use_container_width=True
        )


    # =====================================================
    # STATISTICS
    # =====================================================

    st.markdown(
        '<div class="gradient-line"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">📊 Summary Analytics</div>',
        unsafe_allow_html=True
    )

    original_words = len(
        original_text.split()
    )

    summary_words = len(
        summary.split()
    )

    if original_words > 0:

        reduction = (
            (
                original_words -
                summary_words
            )
            / original_words
        ) * 100

    else:

        reduction = 0

    reduction = max(
        0,
        reduction
    )

    # -----------------------------------------------------
    # METRICS
    # -----------------------------------------------------

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:

        st.metric(
            label="📄 Original Words",
            value=original_words
        )

    with metric2:

        st.metric(
            label="✨ Summary Words",
            value=summary_words
        )

    with metric3:

        st.metric(
            label="📉 Text Reduction",
            value=f"{reduction:.1f}%"
        )

    with metric4:

        st.metric(
            label="🤖 Model",
            value="T5-Small"
        )


    # =====================================================
    # PROJECT INFORMATION
    # =====================================================

st.markdown(
    '<div class="gradient-line"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🚀 AI Dashboard Information</div>',
    unsafe_allow_html=True
)

info1, info2, info3 = st.columns(3)

# -----------------------------------------------------
# CARD 1
# -----------------------------------------------------

with info1:

    with st.container(border=True):

        st.markdown("### 🧠 Transformer Model")

        st.caption(
            "Fine-tuned T5-Small model "
            "for abstractive text summarization."
        )


# -----------------------------------------------------
# CARD 2
# -----------------------------------------------------

with info2:

    with st.container(border=True):

        st.markdown("### ⚡ Fast Inference")

        st.caption(
            "Automatically uses GPU when "
            "CUDA is available."
        )


# -----------------------------------------------------
# CARD 3
# -----------------------------------------------------

with info3:

    with st.container(border=True):

        st.markdown("### ✨ Smart Summaries")

        st.caption(
            "Converts long text into "
            "concise and meaningful content."
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

✨ <b>AI Text Summarizer</b>

<br><br>

Built with Streamlit • PyTorch • Hugging Face Transformers • T5

<br><br>

AI Summarization Project • 2026

</div>
""", unsafe_allow_html=True)