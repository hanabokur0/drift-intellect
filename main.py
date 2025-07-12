import streamlit as st
import random
import json

st.set_page_config(page_title="知的ドリフティング", layout="centered")
st.title("🌊 知的ドリフティング - Drift Intellect")

# 言語選択
lang = st.radio("言語を選んでください / Choose language", ["日本語", "English"])
wordlist_file = "wordlist_ja.json" if lang == "日本語" else "wordlist_en.json"

# 単語読み込み
try:
    with open(wordlist_file, "r", encoding="utf-8") as f:
        words = json.load(f)
except FileNotFoundError:
    st.error(f"{wordlist_file} が見つかりません。")
    words = []

# ランダムに5単語表示
if words:
    selected = random.sample(words, 5)
    st.subheader("漂流中の単語 / Floating Words")
    for word in selected:
        if st.button(word):
            st.markdown(f"**{word}** に関する解釈や知識（AI連携予定）")
