import streamlit as st
import random
import json

st.set_page_config(page_title="知的ドリフティング", layout="centered")
st.title("🌊 知的ドリフティング - Drift Intellect")

# 言語選択
lang = st.sidebar.selectbox("言語 / Language", ["日本語", "English"])

# 単語リストをロード
filename = "wordlist_ja.json" if lang == "日本語" else "wordlist_en.json"
try:
    with open(filename, "r", encoding="utf-8") as f:
        wordlist = json.load(f)
except FileNotFoundError:
    st.error(f"{filename} が見つかりません。")
    wordlist = []

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
# 選んだ単語の意味を表示（辞書連携）
if st.session_state.selected_word:
    st.markdown("----")
    st.markdown(f"### 🧭 選んだ単語: `{st.session_state.selected_word}`")
    st.markdown("🔍 意味を表示中...")

    dict_filename = "dict_ja.json" if lang == "日本語" else "dict_en.json"
    try:
        with open(dict_filename, "r", encoding="utf-8") as f:
            dictionary = json.load(f)
        meaning = dictionary.get(st.session_state.selected_word, "（まだ意味が登録されていません）")
    except FileNotFoundError:
        meaning = "辞書ファイルが見つかりません。"

    st.markdown(f"**{meaning}**")

    # ログ保存（重複回避）
    if "log" not in st.session_state:
        st.session_state.log = []
    if not any(entry["word"] == st.session_state.selected_word for entry in st.session_state.log):
        st.session_state.log.append({
            "word": st.session_state.selected_word,
            "meaning": meaning
        })

# ログ表示
if "log" in st.session_state and st.session_state.log:
    st.markdown("----")
    st.markdown("### 📜 今日のドリフト記録 / Drift Log")
    for entry in st.session_state.log:
        st.markdown(f"- **{entry['word']}**: {entry['meaning']}")
