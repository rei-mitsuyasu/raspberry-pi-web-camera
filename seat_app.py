import numpy as np
import pandas as pd
import streamlit as st
import datetime
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from datetime import datetime, timedelta
import plotly.graph_objects as go

def main():
    st.set_page_config(page_title="席決めアプリ", page_icon="⚡")
    st.title("席決め")
    st.write("NULL")
    num_people = st.text_input("名簿に追加する人数を入力してください(半角数字) (例: 5)")

    if num_people.isdigit():
        num_people = int(num_people)  # 数字として処理
        if num_people > 0:  # 1人以上の場合に処理を続ける
            # テキストボックスを人数分表示
            names = []
            for i in range(num_people):
                name = st.text_input(f"名前 {i+1}")
                names.append(name)

            # 「名簿作成」ボタン
            if st.button("名簿を作成"):
                # 名前リストを2列に分けて表示
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**列 1**")
                    for i in range(0, len(names), 2):  # 2列ごとに分ける
                        if i < len(names):
                            st.write(names[i])

                with col2:
                    st.write("**列 2**")
                    for i in range(1, len(names), 2):  # 2列目
                        if i < len(names):
                            st.write(names[i])
        else:
            st.error("人数は1以上の数字で入力してください。")
    else:
        st.error("正しい人数（整数）を入力してください。")

if __name__ == "__main__":
    main()