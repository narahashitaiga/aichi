# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('楢橋のアプリケーション')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('あなたの名前を入力してください')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'🌟 元気ですか、{user_input}さん! 🌟')  # メッセージをハイライト
    else:
        st.error('名前を入力してください。')  # エラーメッセージを表示
st.slider("体重を入力してください")
def caluculate_bmi(weight,height):
    return weight / [height ** 2]
def interpret_bmi:
    if bmi < 18.5:
    return "低体重"
elif 18.5 <= bmi < 25:
    return "普通体重"
elif 25 <= bmi < 30:
    return "肥満（１度）"
elif 30 <= bmi < 35:
    return "肥満（２度）"
elif 35 <= bmi < 40:
     return "肥満（３度）"

