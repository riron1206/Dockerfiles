"""
streamlit でステーションのmapとかする表示
Usage:
    $ poetry run streamlit run ./app_map.py
"""
import datetime
import gc

from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium import plugins
from folium.plugins import HeatMap
import lightgbm as lgb
from sklearn.model_selection import KFold
from matplotlib import rcParams
import streamlit as st
from streamlit_folium import folium_static
import pydeck as pdk

dark_colors = [
    "#99D699",
    "#B2B2B2",
    (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
    (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
    (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
    (0.4, 0.6509803921568628, 0.11764705882352941),
    (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
    (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
    (0.4, 0.4, 0.4),
]
rcParams["figure.figsize"] = (12, 9)
rcParams["figure.dpi"] = 150
rcParams["lines.linewidth"] = 2
rcParams["axes.facecolor"] = "white"
rcParams["axes.titlesize"] = 20
rcParams["axes.labelsize"] = 17.5
rcParams["xtick.labelsize"] = 15
rcParams["ytick.labelsize"] = 15
rcParams["legend.fontsize"] = 17.5
rcParams["patch.edgecolor"] = "none"
rcParams["grid.color"] = "white"
rcParams["grid.linestyle"] = "-"
rcParams["grid.linewidth"] = 1
rcParams["grid.alpha"] = 1
rcParams["text.color"] = "444444"
rcParams["axes.labelcolor"] = "444444"
rcParams["ytick.color"] = "444444"
rcParams["xtick.color"] = "444444"

pd.options.plotting.backend = (
    "plotly"  # pandasのグラフをplotlyで表示（pandas>0.25以上、plotly>4.5以上）
)

# streamlitの警告を非表示にする
st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("San Francisco Bay Area Bike Share")
st.text("data source: https://www.kaggle.com/benhamner/sf-bay-area-bike-share/")


def reduce_mem_usage(df, verbose=False):
    """メモリ使用量を減らすためにデータ型を変更"""
    numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
    start_mem = df.memory_usage().sum() / 1024 ** 2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                c_prec = df[col].apply(lambda x: np.finfo(x).precision).max()
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                    and c_prec == np.finfo(np.float16).precision
                ):
                    df[col] = df[col].astype(np.float16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                    and c_prec == np.finfo(np.float64).precision
                ):
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    end_mem = df.memory_usage().sum() / 1024 ** 2
    if verbose:
        print(
            "Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)".format(
                end_mem, 100 * (start_mem - end_mem) / start_mem
            )
        )
    return df


@st.cache
def load_data(
    DATADIR=r"C:\Users\yokoi.shingo\my_task\アイデアソン\data\57_793589_bundle_archive",
):
    # trips
    trips_df = reduce_mem_usage(pd.read_csv(f"{DATADIR}/trip.csv"))
    trips_df["start_date"] = pd.to_datetime(trips_df["start_date"])
    trips_df["end_date"] = pd.to_datetime(trips_df["end_date"])

    # station
    stations_df = reduce_mem_usage(pd.read_csv(f"{DATADIR}/station.csv"))
    stations_df["lat"] = stations_df["lat"].apply(lambda x: str(x))
    stations_df["long"] = stations_df["long"].apply(lambda x: str(x))

    start_station_info = stations_df[["id", "lat", "long"]]
    start_station_info.columns = ["start_station_id", "start_lat", "start_long"]
    end_station_info = stations_df[["id", "lat", "long"]]
    end_station_info.columns = ["end_station_id", "end_lat", "end_long"]

    trips_df = trips_df.merge(start_station_info, on="start_station_id")
    trips_df = trips_df.merge(end_station_info, on="end_station_id")

    # status
    status_df = reduce_mem_usage(pd.read_csv(f"{DATADIR}/status.csv"))
    status_df.time = pd.to_datetime(status_df.time)
    status_df = status_df[status_df.time.dt.minute % 5 == 0]

    stations_df.rename(columns={"id": "station_id"}, inplace=True)
    stations_df.installation_date = pd.to_datetime(stations_df.installation_date)
    status_df = status_df.merge(stations_df, on="station_id", how="left")
    status_df.reset_index(inplace=True)
    status_df.drop(columns=["index"], inplace=True)
    status_df["date"] = status_df.time.dt.date

    # weather
    weather_df = reduce_mem_usage(pd.read_csv(f"{DATADIR}/weather.csv"))
    weather_df.date = pd.to_datetime(weather_df.date)
    zipcode_city_dict = dict()
    zipcode_city_dict[95113] = "San Jose"
    zipcode_city_dict[94301] = "Palo Alto"
    zipcode_city_dict[94107] = "San Francisco"
    zipcode_city_dict[94063] = "Redwood City"
    zipcode_city_dict[94041] = "Mountain View"
    weather_df["city"] = weather_df.zip_code.apply(lambda x: zipcode_city_dict[x])

    status_df.date = pd.to_datetime(status_df.date)
    status_df = status_df.merge(weather_df, how="left", on=["date", "city"])
    # status_df.dropna(inplace=True)

    # foliumのデータはキャッシュできないのでデータフレームのみ
    return (stations_df, trips_df, status_df, weather_df, get_nb_trips_df(trips_df))


def get_nb_trips_df(trips_df):
    """どのステーション間の移動が多いかのデータベース準備"""
    # レンタルバイクの出発点と終着点の回数
    station_ids_dict = dict()
    plot_dict = dict()
    for index, row in trips_df.iterrows():
        start_lat = row["start_lat"]
        start_long = row["start_long"]
        end_lat = row["end_lat"]
        end_long = row["end_long"]
        key = (
            str(start_lat)
            + "_"
            + str(start_long)
            + "_"
            + str(end_lat)
            + "_"
            + str(end_long)
        )
        if key in plot_dict:
            plot_dict[key] += 1
        else:
            plot_dict[key] = 1

        station_ids_dict[key] = (
            str(row["start_station_id"])
            + "_"
            + str(row["start_station_name"])
            + "_"
            + str(row["end_station_id"])
            + "_"
            + str(row["end_station_name"])
        )

    start_lat = []
    start_long = []
    end_lat = []
    end_long = []
    nb_trips = []
    for key, value in plot_dict.items():
        start_lat.append(float(key.split("_")[0]))
        start_long.append(float(key.split("_")[1]))
        end_lat.append(float(key.split("_")[2]))
        end_long.append(float(key.split("_")[3]))
        nb_trips.append(int(value))

    start_station_id = []
    start_station_name = []
    end_station_id = []
    end_station_name = []
    for key, value in station_ids_dict.items():
        start_station_id.append(int(value.split("_")[0]))
        start_station_name.append(str(value.split("_")[1]))
        end_station_id.append(int(value.split("_")[2]))
        end_station_name.append(str(value.split("_")[3]))

    nb_trips_df = pd.DataFrame(
        {
            "start_station_id": start_station_id,
            "start_station_name": start_station_name,
            "start_lat": start_lat,
            "start_long": start_long,
            "end_station_id": end_station_id,
            "end_station_name": end_station_name,
            "end_lat": end_lat,
            "end_long": end_long,
            "nb_trips": nb_trips,
        }
    )
    return nb_trips_df


class MapFolium:
    """folium関連"""

    @staticmethod
    def get_station_map(stations_df):
        """各ステーションの場所を地図に追加"""
        heatmap = folium.Map(
            [stations_df["lat"].median(), stations_df["long"].median()],  # 地図の中心点
            zoom_start=10,  # zoom_start 引数で最初のズームレベルを指定できます。こちらは指定しないと、「いい感じ」にしてくれるようです。ズームレベルは、1~20の整数値で指定し、1が最もズームアウトした状態、20が最もズームインした状態
            # tiles='Stamen Toner'  # tiles: 地図のスタイル。Stamen Tonerだとモノクロになる
        )
        stations_loc = [
            [float(stations_df.lat.values[i]), float(stations_df.long.values[i])]
            for i in range(len(stations_df))
        ]
        heatmap.add_child(HeatMap(stations_loc, radius=10))

        for index, row in stations_df.iterrows():
            folium.Marker(
                [float(row["lat"]), float(row["long"])],
                popup="id:" + str(row["station_id"]) + "\nname:" + row["name"],
            ).add_to(heatmap)

        return heatmap

    @staticmethod
    def get_trip_map(stations_df, nb_trips_df):
        """どのステーション間の移動が多いかの地図描画"""
        # 地図の中心点出すために緯度経度の中央値計算
        ave_lat = (nb_trips_df.start_lat.median() + nb_trips_df.end_lat.median()) / 2
        ave_lon = (nb_trips_df.start_long.median() + nb_trips_df.end_long.median()) / 2
        directions_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=15)

        for index, row in nb_trips_df.iterrows():
            points = []
            points.append(tuple([row["start_lat"], row["start_long"]]))
            points.append(tuple([row["end_lat"], row["end_long"]]))
            folium.PolyLine(points, color="red", weight=row["nb_trips"] / 1000).add_to(
                directions_map
            )

        for index, row in stations_df.iterrows():
            folium.Marker(
                [float(row["lat"]), float(row["long"])],
                popup="id:" + str(row["station_id"]) + "\nname:" + row["name"],
            ).add_to(directions_map)

        return directions_map


class MapPydeck:
    """pydeck関連
    緯度経度の列のデータフレームでしかplotできないのでレコード数増えると描画おそすぎるので使わない"""

    @staticmethod
    def plot_trip_start_end_map(nb_trips_df, t_type="start"):
        """どのステーションでレンタル開始終了が多いかの地図をpydeckで描画"""

        if t_type == "start":
            # df = nb_trips_df[["start_lat", "start_long", "nb_trips"]].rename(
            df = nb_trips_df[["start_lat", "start_long"]].rename(
                columns={"start_lat": "lat", "start_long": "lon"}
            )
        else:
            # df = nb_trips_df[["end_lat", "end_long", "nb_trips"]].rename(
            df = nb_trips_df[["end_lat", "end_long"]].rename(
                columns={"end_lat": "lat", "end_long": "lon"}
            )

        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state=pdk.ViewState(
                    latitude=37.76, longitude=-122.4, zoom=11, pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        "HexagonLayer",
                        reduce_mem_usage(df),
                        get_position=["lng", "lat"],
                        auto_highlight=True,
                        elevation_scale=50,
                        pickable=True,
                        elevation_range=[0, 3000],
                        extruded=True,
                        coverage=1,
                    ),
                ],
            )
        )


class ModelTs:
    """fbprophetで時系列モデル作ろうとしたが、
    依存ライブラリのpystanはcondaでしかインストールできないのでできず。。。"""

    @staticmethod
    def time_cols(df, date_col):
        df[date_col] = pd.to_datetime(df[date_col])  # dtype を datetime64 に変換
        df["year"] = df[date_col].dt.year
        df["month"] = df[date_col].dt.month
        df["day"] = df[date_col].dt.day
        df["dayofyear"] = df[date_col].dt.dayofyear
        df["dayofweek"] = df[date_col].dt.dayofweek
        df["weekend"] = (df[date_col].dt.dayofweek.values >= 5).astype(int)
        df["hour"] = df[date_col].dt.hour
        df["minute"] = df[date_col].dt.minute
        return df


def sidebar():
    """
    サイドバーの項目
    - ボタンとかのウィジェットはst.sidebar でサイドバーに追加できる
    """
    # セレクトボックス（可視化する項目選ぶ）
    maps = st.sidebar.radio("Select map", ("station", "trip"),)

    # データフレームが期間指定に対応してないのでやめとく
    ## レンジスライダー（可視化する期間指定）
    # slider_date = st.sidebar.slider(
    #    "Select date",
    #    value=(datetime.date(2013, 8, 1), datetime.date(2015, 8, 31)),
    #    format="MM/DD/YY",
    # )

    availables = st.sidebar.radio(
        "Select available", ("bikes_available", "docks_available")
    )

    return maps, availables  # , slider_date


def main(stations_df, trips_df, status_df, weather_df, nb_trips_df):
    """メイン部分の項目"""

    # ------------------------ ステーションのmap表示 ------------------------
    st.header(f"Map")
    if selectbox_item == "station":
        # ステーションのmap
        st.subheader(f"Station Map")
        folium_static(MapFolium.get_station_map(stations_df))
        # 地域ごとのステーション数、ドック数plot
        st.subheader(f"Station/Dock Count")
        _df = (
            stations_df.groupby("city")
            .agg({"name": "count"})
            .sort_values(by="name", ascending=False)
            .rename(columns={"name": "station_count"})
        )
        _df_dock = (
            stations_df.groupby("city")
            .agg({"dock_count": "sum"})
            .sort_values(by="dock_count", ascending=False)
        )
        fig = _df.join(_df_dock).plot.bar()
        st.write(fig)

    elif selectbox_item == "trip":
        # どのステーション間の移動が多いか
        st.subheader(f"Trip Map")
        folium_static(MapFolium.get_trip_map(stations_df, nb_trips_df))
        # データフレームも出しとく
        st.dataframe(
            nb_trips_df[
                [
                    "start_station_id",
                    "start_station_name",
                    "end_station_id",
                    "end_station_name",
                    "nb_trips",
                ]
            ]
            .sort_values(by="nb_trips", ascending=False)
            .head(100)
        )

        # 開始と終着駅のカウント数を一気にplot
        st.subheader(f"Trip Start End Station Count")
        start_station_name = pd.DataFrame(
            trips_df["start_station_name"].value_counts()
        ).rename(columns={"start_station_name": "start_station_count"})
        _df = trips_df[["start_station_id", "start_station_name"]].set_index(
            "start_station_name"
        )
        start_station_name = start_station_name.join(_df).drop_duplicates()

        end_station_name = pd.DataFrame(
            trips_df["end_station_name"].value_counts()
        ).rename(columns={"end_station_name": "end_station_count"})
        _df = trips_df[["end_station_id", "end_station_name"]].set_index(
            "end_station_name"
        )
        end_station_name = end_station_name.join(_df).drop_duplicates()

        start_end = start_station_name.join(end_station_name)
        start_end = start_end.reset_index()
        start_end = start_end[
            ["start_station_id", "index", "start_station_count", "end_station_count"]
        ]
        start_end = start_end.rename(
            columns={"index": "name", "start_station_id": "station_id"}
        ).sort_values(["start_station_count", "end_station_count"])
        start_end = start_end.set_index("name")
        fig = (
            start_end[["start_station_count", "end_station_count"]].tail(15).plot.barh()
        )
        st.write(fig)
        st.dataframe(
            start_end.sort_values(
                ["start_station_count", "end_station_count"], ascending=False
            )
        )

        ##MapPydeck.plot_trip_start_end_map(trips_df, "start")
        ##MapPydeck.plot_trip_start_end_map(trips_df, "end")

    # --------------------------------------------------------------------

    # -------------------- ステーションごとの利用可能なバイク数・ドック数 --------------------
    if ava_radio == "bikes_available":
        st.header(f"Bikes_Available")
        ### バイク数の分布
        ##st.subheader(f"Bikes_Available Distribution")
        ##fig = status_df["bikes_available"].plot.hist(
        ##    bins=27, title="Bikes Available (All Stations)"
        ##)
        ##st.write(fig)

        # 利用可能な数が0になったの駅回数
        st.subheader(f"Bikes_Available=0 count station status")
        _df = status_df[status_df["bikes_available"] == 0]
        _series = _df.groupby(["station_id", "name"]).size()
        _df = (
            pd.DataFrame(_series)
            .sort_values(0, ascending=False)
            .rename(columns={0: "bikes_available=0 count"})
            .head(10)
        )
        st.dataframe(_df)
        print()

        # ステーションごとのバイク数の推移
        st.subheader(f"Bikes_Available per station")
        b_s_id = st.text_input(
            "Input station_id", _df.iloc[0].name[0]
        )  # 利用可能な数が0になったの駅回数が一番多いstation_idを初期値とする
        _df = status_df[status_df["station_id"] == int(b_s_id)]
        _df = _df[["time", "bikes_available"]].sort_values(by="time").set_index("time")
        fig = _df.plot(title=f"status.csv station_id={b_s_id}", y="bikes_available")
        st.write(fig)  # plotlyで書くためにfigを渡している

        # ステーションごとのバイク数の分布(box plot) box plotデータサイズ大きすぎて表示できないので画像あらかじめ作って表示
        st.subheader(f"Bikes_Available per station")
        st.image(Image.open("./bikes_available_box.png"), use_column_width=True)

        # ステーションごとのバイク数のshapで計算した相関関係
        st.subheader(f"Bikes_Available Shap Correlation(LightGBM)")
        st.image(
            Image.open("./shap_summary_plot_corr_bikes_available.png"),
            use_column_width=True,
        )
        st.text(
            "This result depends on the model.\nThe results can vary significantly with feature engineering."
        )

    elif ava_radio == "docks_available":
        st.header(f"Docks_Available")
        ### ドック数の分布
        ##st.subheader(f"Docks_Available Distribution")
        ##fig = status_df["docks_available"].plot.hist(
        ##    bins=27, title="Docks Available (All Stations)"
        ##)
        ##st.write(fig)

        # 利用可能な数が0になったの駅回数
        st.subheader(f"Docks_Available=0 count station status")
        _df = status_df[status_df["docks_available"] == 0]
        _series = _df.groupby(["station_id", "name"]).size()
        _df = (
            pd.DataFrame(_series)
            .sort_values(0, ascending=False)
            .rename(columns={0: "docks_available=0 count"})
            .head(10)
        )
        st.dataframe(_df)

        # ステーションごとのドック数の推移
        st.subheader(f"Docks_Available per station")
        b_s_id = st.text_input(
            "Input station_id", _df.iloc[0].name[0]
        )  # 利用可能な数が0になったの駅回数が一番多いstation_idを初期値とする
        _df = status_df[status_df["station_id"] == int(b_s_id)]
        _df = _df[["time", "docks_available"]].sort_values(by="time").set_index("time")
        fig = _df.plot(title=f"status.csv station_id={b_s_id}", y="docks_available")
        st.write(fig)  # plotlyで書くためにfigを渡している

        # ステーションごとのドック数の分布(box plot) box plotデータサイズ大きすぎて表示できないので画像あらかじめ作って表示
        st.subheader(f"Docks_Available per station")
        st.image(Image.open("./docks_available_box.png"), use_column_width=True)

        # ステーションごとのドック数のshapで計算した相関関係
        st.subheader(f"Docks_Available Shap Correlation(LightGBM)")
        st.image(
            Image.open("./shap_summary_plot_corr_docks_available.png"),
            use_column_width=True,
        )
        st.text(
            "This result depends on the model.\nThe results can vary significantly with feature engineering."
        )
    # ------------------------------------------------------------------------------------

    # -------------------------------- csvのデータ表示 --------------------------------
    st.header(f"Other")
    st.subheader(f"Csv Data (only first 100 rows)")
    csv_radio = st.radio("select csv", ("station", "status", "trip", "weather"))
    if csv_radio == "station":
        st.dataframe(stations_df.head(100))
    elif csv_radio == "status":
        st.dataframe(status_df.head(100))
    elif csv_radio == "trip":
        st.dataframe(trips_df.head(100))
    elif csv_radio == "weather_df":
        st.dataframe(weather_df.head(100))
    # --------------------------------------------------------------------------------


if __name__ == "__main__":
    stations_df, trips_df, status_df, weather_df, nb_trips_df = load_data()
    # del status_df, weather_df
    # gc.collect()

    # サイドバー関連
    # selectbox_item, slider_date = sidebar()
    selectbox_item, ava_radio = sidebar()

    ## 期間指定
    # stations_df = stations_df.query(
    #    f'"{slider_date[0]}" <= installation_date <= "{slider_date[1]}"'
    # )
    # trips_df = trips_df.query(f'"{slider_date[0]}" <= start_date <= "{slider_date[1]}"')

    # メイン領域関連
    main(stations_df, trips_df, status_df, weather_df, nb_trips_df)
