#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
モデル作成で使う移動平均線や大陽線データcsv(stock_rate_2008_2018.csv)作成
元notebook: C:/Users/shingo/jupyter_notebook/stock_work/work/tmp.ipynb
Usage:
    $ activate stock
    $ python make_stock_csv.py  # stock_rate_2008_2018.csv が作られる。csvは1GB以上ある。Dドライブのデータ使うからDockerでは実行できない
"""
import datetime
import glob
import sqlite3
import pathlib
import numpy as np
import pandas as pd
from tqdm import tqdm
# from tqdm.notebook import tqdm
import random
np.random.seed(7)
random.seed(7)


class SqlliteMgr():
    def __init__(self, db_file_name=r'D:\DB_Browser_for_SQLite\stock.db'):
        self.db_file_name = db_file_name

    def table_to_df(self, table_name=None, sql=None):
        """ sqlite3で指定テーブルのデータをDataFrameで返す """
        conn = sqlite3.connect(self.db_file_name)
        if table_name is not None:
            return pd.read_sql(f'SELECT * FROM {table_name}', conn)
        elif sql is not None:
            return pd.read_sql(sql, conn)
        else:
            return None

    def get_code_price(self, code, start_date, end_date):
        """ DBから指定銘柄の株価取得 """
        # 200MA計算するためにだいぶ前から取る
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date() - datetime.timedelta(days=500)
        sql = f"""
        SELECT
            p.code,
            p.date,
            p.open,
            p.high,
            p.low,
            p.close,
            p.volume
        FROM
            prices AS p
            INNER JOIN
                brands AS b
            ON
                p.code = b.code
        WHERE
            p.code = {code}
        AND
            p.date BETWEEN '{start_date}' AND '{end_date}'
        AND
            b.unit >= 100
        AND
            b.sector NOT IN ('REIT銘柄一覧', 'ETF銘柄一覧', 'ETN銘柄一覧')
        """
        return self.table_to_df(sql=sql)


def delete_outlier_3sigma_df_cols(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """
    データフレームの指定列について、外れ値(3σ以上のデータ)削除
    Usage:
        df = delete_outlier_3sigma_df_cols(df, ['value', 'value2'])
    """
    for col in cols:
        if df[col].dtype.name not in ['object', 'category', 'bool']:
            # 数値型の列なら実行
            df = df[(abs(df[col] - np.mean(df[col])) / np.std(df[col]) <= 3)].reset_index(drop=True)
    return df


def add_option_columns(df, start_date):
    """ 株価データフレームに列追加 """
    df['5MA'] = df['close'].rolling(window=5).mean()
    df['25MA'] = df['close'].rolling(window=25).mean()
    df['75MA'] = df['close'].rolling(window=75).mean()
    df['200MA'] = df['close'].rolling(window=200).mean()
    df['5MA_div_rate'] = (df['close'] - df['5MA']) / df['5MA']  # 当日終値と5MA乖離率
    df['25MA_div_rate'] = (df['close'] - df['25MA']) / df['25MA']  # 当日終値と25MA乖離率
    df['75MA_div_rate'] = (df['close'] - df['75MA']) / df['75MA']  # 当日終値と75MA乖離率
    df['200MA_div_rate'] = (df['close'] - df['200MA']) / df['200MA']  # 当日終値と200MA乖離率
    df['10MAX_div_rate'] = df['close'] / df['high'].shift(1).fillna(0).rolling(window=10, min_periods=0).max()  # 当日終値と前日からの直近10日間の中で最大高値との乖離率
    df['volume_1diff_rate'] = (df['volume'] - df['volume'].shift(1).fillna(0)) / df['volume']  # 前日比出来高
    df['candlestick'] = (df['close'] - df['open']) / (df['high'] - df['low'])  # ローソク足の大きさ

    # start_dateからのレコードだけにする（200MA出すためにstart_date より前のレコード保持しているため）
    df = df.dropna(subset=['200MA'])
    df['date'] = pd.to_datetime(df['date'])
    df = df.query(f'date >= "{start_date}"')
    df = df.reset_index(drop=True)

    # 目的変数 翌日の終値/始値
    df['next_close_oepn_rate'] = df['close'].shift(-1) / df['open'].shift(-1)

    # 列削除
    df = df.drop(['5MA', '25MA', '75MA', '200MA'], axis=1)
    df = df.drop(['code', 'date', 'open', 'high', 'low', 'close', 'volume'], axis=1)

    # 行削除  ローソク足無いレコードものぞく
    df = df.dropna(subset=['next_close_oepn_rate', 'candlestick'])

    # 上昇率が大きすぎるのは外れ値として除く
    return delete_outlier_3sigma_df_cols(df, ['next_close_oepn_rate'])


if __name__ == '__main__':
    codes = [pathlib.Path(p).stem for p in glob.glob(r'D:\DB_Browser_for_SQLite\csvs\kabuoji3\*csv')]

    start_date, end_date = '2008-01-01', '2018-12-31'
    mgr = SqlliteMgr()

    df_concat = None
    for code in tqdm(codes):
        df = mgr.get_code_price(code, start_date, end_date)
        if df is not None:
            df = add_option_columns(df, start_date)
            df_concat = df if df_concat is None else pd.concat([df_concat, df], ignore_index=True)

    df_concat.to_csv('stock_rate_2008_2018.csv', index=False)
