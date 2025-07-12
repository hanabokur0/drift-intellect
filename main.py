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

import streamlit as st
import random
import json

# 言語選択
lang = st.sidebar.selectbox("言語 / Language", ["日本語", "English"])

# 単語リストをロード
filename = "wordlist_ja.json" if lang == "日本語" else "wordlist_en.json"
with open(filename, "r", encoding="utf-8") as f:
    wordlist = json.load(f)

# セッション状態で単語保持
if "words" not in st.session_state:
    st.session_state.words = random.sample(wordlist, 5)
if "selected_word" not in st.session_state:
    st.session_state.selected_word = None

# 単語の再生成
if st.button("🌊 単語を流す / Refresh words"):
    st.session_state.words = random.sample(wordlist, 5)
    st.session_state.selected_word = None
# 単語ボタン表示
st.markdown("### 浮かび上がる単語たち / Floating Words")
for i, word in enumerate(st.session_state.words):
    if st.button(word, key=f"word_btn_{i}"):
        st.session_state.selected_word = word

# 選んだ単語の意味を表示（プレーンテキスト例）
if st.session_state.selected_word:
    st.markdown("----")
    st.markdown(f"### 🧭 選んだ単語: `{st.session_state.selected_word}`")
    st.markdown("🔍 意味を表示中...")

    # 辞書ファイルを読み込み（日本語 or 英語）
    dict_filename = "dict_ja.json" if lang == "日本語" else "dict_en.json"
    with open(dict_filename, "r", encoding="utf-8") as f:
        dictionary = json.load(f)

    # 意味を取得＆表示
    meaning = dictionary.get(st.session_state.selected_word, "（まだ意味が登録されていません）")
    st.markdown(f"**{meaning}**")
