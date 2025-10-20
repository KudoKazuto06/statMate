# Streamlit app (chat + file upload + computation)

import streamlit as st
import pandas as pd
from stats_engine import independent_ttest, paired_ttest, correlation, anova, describe
from llm_utils import decide_test, ask_llm

st.set_page_config(page_title="StatMate 🧮", layout="wide")
st.title("🧮 StatMate – Statistics Chatbot + Computation")

# Upload CSV/Excel (optional)
uploaded = st.file_uploader("📂 Upload CSV/Excel (optional)", type=["csv","xlsx"])
df = None
if uploaded:
    df = pd.read_csv(uploaded) if uploaded.name.endswith(".csv") else pd.read_excel(uploaded)
    st.success(f"Loaded file: {uploaded.name}")
    st.dataframe(df.head())

# Chat input
user_input = st.text_area("💬 Ask me anything about statistics or your data:")
if st.button("Send") and user_input:
    if df:
        # Try computation first
        test_type = decide_test(user_input)
        st.write(f"🧠 LLM suggests: `{test_type}`")
        try:
            if test_type in ["independent_ttest", "paired_ttest", "correlation", "anova"]:
                cols = st.multiselect("Select columns for computation", df.columns)
                if len(cols) >= 2:
                    if test_type == "independent_ttest":
                        st.write(independent_ttest(df, cols[0], cols[1]))
                    elif test_type == "paired_ttest":
                        st.write(paired_ttest(df, cols[0], cols[1]))
                    elif test_type == "correlation":
                        st.write(correlation(df, cols[0], cols[1]))
                    elif test_type == "anova":
                        st.write(anova(df, *cols))
                else:
                    st.warning("Please select at least two columns for computation.")
            elif test_type == "describe":
                st.write(describe(df))
            else:
                # Not a computation question → treat as theory
                answer = ask_llm(user_input)
                st.write(answer)
        except Exception as e:
            st.error(f"⚠️ Error during computation: {e}")
    else:
        # No file → pure theory chat
        answer = ask_llm(user_input)
        st.write(answer)
        
        