"""
日本のコロナ感染者数を可視化するサンプルコード
https://docs.streamlit.io/en/stable/api.html#display-data の公式ドキュメント見ながらつくった
"""
import io
import datetime
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# streamlitの警告を非表示にする
st.set_option("deprecation.showfileUploaderEncoding", False)

# sns.set()
# plt.rcParams["font.family"] = "Yu Gothic"  # Yu Gothic指定すれば日本語出せるはずだができず
pd.options.plotting.backend = (
    "plotly"  # pandasのグラフをplotlyで表示（pandas>0.25以上、plotly>4.5以上）
)

st.title("Coronavirus Trends in Japan")
st.text(
    "data source: https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000068/resource/c2d997db-1450-43fa-8037-ebb11ec28d4c"
)


@st.cache
def load_data():
    # webから最新の情報取ってくる
    data = pd.read_csv(
        "https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv",
        parse_dates=["公表_年月日"],
        index_col="公表_年月日",
    )
    return data


class Cross:
    @staticmethod
    def age_cross_data(df):
        # 公表_年月日、患者_年代でクロス集計
        df_cross = pd.crosstab(df.index, df["患者_年代"])
        # 日本語表記除去
        df_cross = df_cross.rename(
            columns={
                "10歳未満": "under 10",
                "10代": "10",
                "20代": "20",
                "30代": "30",
                "40代": "40",
                "50代": "50",
                "60代": "60",
                "70代": "70",
                "80代": "80",
                "90代": "90",
                "100歳以上": "over 100",
                "'-": "-",
                "不明": "unknown",
            }
        )
        df_cross.index.names = ["Date"]
        df_cross.columns.name = "Generation"
        sort_cols = sorted(df_cross.columns.to_list())
        df_cross = df_cross[sort_cols]
        return df_cross.rolling(7).mean()

    @staticmethod
    def region_cross_data(df):
        # 公表_年月日、患者_居住地でクロス集計
        df_cross = pd.crosstab(data.index, data["患者_居住地"])
        # 日本語表記除去
        df_cross = df_cross.rename(
            columns={
                "湖北省武漢市": "Wuhan, Hubei Province",
                "都内": "Inside Tokyo",
                "湖南省長沙市": "Changsha City, Hunan Province",
                "都外": "Outside Tokyo",
                "調査中": "Under investigation",
                "―": "-",
            }
        )
        df_cross.index.names = ["Date"]
        df_cross.columns.name = "Region"
        sort_cols = sorted(df_cross.columns.to_list())
        df_cross = df_cross[sort_cols]
        return df_cross.rolling(7).mean()

    @staticmethod
    def dayofweek_cross_data(df):
        # 公表_年月日、患者_居住地でクロス集計
        df_cross = pd.crosstab(data.index, data["曜日"])
        # 日本語表記除去
        df_cross = df_cross.rename(
            columns={
                "日": "Sun",
                "月": "Mon",
                "火": "Tue",
                "水": "Wed",
                "木": "Thu",
                "金": "Fri",
                "土": "Sat",
            }
        )
        df_cross.index.names = ["Date"]
        df_cross.columns.name = "dayofweek"
        sort_cols = sorted(df_cross.columns.to_list())
        df_cross = df_cross[sort_cols]
        return df_cross.rolling(7).mean()

    @staticmethod
    def gender_cross_data(df):
        # 公表_年月日、患者_居住地でクロス集計
        df_cross = pd.crosstab(data.index, data["患者_性別"])
        # 日本語表記除去
        df_cross = df_cross.rename(
            columns={
                "男性": "Male",
                "女性": "Female",
                "不明": "Unknown",
                "女": "Woman",
                "調査中": "Under investigation",
                "―": "-",
            }
        )
        df_cross.index.names = ["Date"]
        df_cross.columns.name = "gender"
        sort_cols = sorted(df_cross.columns.to_list())
        df_cross = df_cross[sort_cols]
        return df_cross.rolling(7).mean()


def sidebar():
    """
    サイドバーの項目
    - ボタンとかのウィジェットはst.sidebar でサイドバーに追加できる
    """
    # セレクトボックス（可視化する項目選ぶ）
    selectbox_item = st.sidebar.selectbox(
        "Select item", ("Age", "Region", "Gender", "Dayofweek"),
    )

    # レンジスライダー（可視化する期間指定）
    slider_date = st.sidebar.slider(
        "Select date",
        value=(datetime.date(2020, 2, 1), datetime.date.today()),
        format="MM/DD/YY - hh:mm",
    )

    # 複数行テキスト入力ウィジェット
    text_area_titile = st.sidebar.text_area("Input title", "")

    # csvファイルアップロード（csvをただ表示するだけ）
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.subheader("uploaded csv")
        st.write(data)  # テーブルはmain部分に表示される

    # ボタン
    if st.sidebar.button("Show balloons!!!"):
        st.balloons()  # 風船表示しとく（ムダ機能）

    return selectbox_item, slider_date, text_area_titile


def main(data, selectbox_item, text_area_titile):
    """メイン部分の項目"""
    st.subheader(f"{text_area_titile}")

    st.subheader("Number of people infected by day")

    if selectbox_item == "Age":
        # 患者_年代
        df_cross = Cross().age_cross_data(data)
        if st.checkbox("Show age cross-tabulation"):
            st.subheader("Age cross-tabulation")
            st.write(df_cross)
        fig = df_cross.plot()
        st.write(fig)  # plotlyで書くためにfigを渡している
        # matplotlibのグラフで可視化したい場合は以下の記法
        # df_cross.plot(figsize=(10, 8))
        # st.pyplot()

    elif selectbox_item == "Region":
        # 患者_居住地
        df_cross = Cross().region_cross_data(data)
        if st.checkbox("Show region cross-tabulation"):
            st.subheader("Region cross-tabulation")
            st.write(df_cross)
        fig = df_cross.plot()
        st.write(fig)

    elif selectbox_item == "Dayofweek":
        # 曜日
        df_cross = Cross().dayofweek_cross_data(data)
        if st.checkbox("Show dayofweek cross-tabulation"):
            st.subheader("Dayofweek cross-tabulation")
            st.write(df_cross)
        fig = df_cross.plot()
        st.write(fig)

    elif selectbox_item == "Gender":
        # 患者_性別
        df_cross = Cross().gender_cross_data(data)
        df_cross.index.names = ["Date"]
        if st.checkbox("Show gender cross-tabulation"):
            st.subheader("Gender cross-tabulation")
            st.write(df_cross)
        fig = df_cross.plot()
        st.write(fig)


if __name__ == "__main__":
    # 生データロードして表示
    data_load_state = st.text("Loading data...")
    data = load_data()
    data_load_state.text("Loading data...done!")
    if st.checkbox("Show raw data"):
        st.subheader("Raw data")
        st.write(data)
        # st.dataframe(data.style.highlight_max(axis=0))  # 列の最大値色付ける。数値列じゃない列あるからエラー？
    # サイドバー関連
    selectbox_item, slider_date, text_area_titile = sidebar()
    # 期間指定
    data = data.query(f'"{slider_date[0]}" <= index <= "{slider_date[1]}"')
    # メイン領域関連
    main(data, selectbox_item, text_area_titile)
