import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import warnings

from etna.datasets.tsdataset import TSDataset
from etna.transforms import LagTransform
from etna.transforms import LinearTrendTransform
from etna.transforms import LagTransform
from etna.transforms import MeanTransform
from etna.transforms import DateFlagsTransform
from etna.transforms import LogTransform
from etna.transforms import SegmentEncoderTransform
from etna.transforms import TrendTransform


from etna.pipeline import Pipeline
from etna.models import NaiveModel

from etna.core import load


warnings.filterwarnings("ignore")

def get_df(product_name, data, end_date='2024-04-20'):
    df = data[(data.Product_Name == product_name)]
    df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

# Функция для конвертации единиц измерения в килограммы
    def convert_to_kg(row):
        if row['Product_Measure'] == 'кг':
            return row['Product_Amount']
        elif row['Product_Measure'] == 'г':
            return row['Product_Amount'] * 0.001  # Конвертация грамм в килограммы
        else:
            return row['Product_Amount']  # Предположим, что другие единицы измерения уже в килограммах

    # Применение функции к каждой строке
    df['Product_Amount_Kg'] = df.apply(convert_to_kg, axis=1)
    df.sort_values(by='Sale_Date', inplace=True)
    # Задание начальной и конечной даты для промежутка
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    start_date = end_date - pd.Timedelta(days=30*12)
    # Отфильтруйте данные по заданному промежутку даты
    df["Sale_Date"] = df["Sale_Date"].dt.tz_localize(None)

    filtered_data = df[(df['Sale_Date'] >= start_date) & (df['Sale_Date'] <= end_date)]
    # Группировка продаж по неделям и вычисление суммы проданных килограмм
    weekly_sales_kg = filtered_data.resample('W-Mon', on='Sale_Date')['Product_Amount_Kg'].sum().rename('Weekly_Sales_Kg')
    df_ts = pd.DataFrame({"timestamp":weekly_sales_kg.index,
                  "target":weekly_sales_kg,
                  "segment":product_name}).reset_index(drop=True)
    return df_ts


def collect_data(data, end_date, product_name):
    df_ts = pd.DataFrame({"timestamp":[],
                  "target":[],
                  "segment":[]})
    data['Manufacture_Date'] = pd.to_datetime(data['Manufacture_Date']) + pd.Timedelta(days=365)
    data['Expiry_Date'] = pd.to_datetime(data['Expiry_Date']) + pd.Timedelta(days=365)
    data['Sale_Date'] = pd.to_datetime(data['Sale_Date']) + pd.Timedelta(days=365)

    for name in [product_name]:
        df_new = get_df(name, data, end_date)
        df_ts = pd.concat([df_ts, df_new], ignore_index=True)

    ts = TSDataset(
        df=TSDataset.to_dataset(df_ts),
        freq="W-Mon"
    )
    return ts


def make_predict_df(ts):
    HORIZON = 12
    lags = LagTransform(in_column="target", lags=list(range(HORIZON, 40)), out_column="lag")
    mean = MeanTransform(in_column=f"lag_{HORIZON}", window=15)

    date_flags = DateFlagsTransform(
        day_number_in_week=True,
        day_number_in_month=True,
        week_number_in_month=False,
        month_number_in_year=True,
        season_number=True,
        is_weekend=True,
        out_column="date_flag",
    )
    log = LogTransform(in_column="target", inplace=True)
    trend = LinearTrendTransform(in_column="target", poly_degree=2)
    seg = SegmentEncoderTransform()
    transforms = [lags, mean, date_flags, log, seg, trend]

    pipeline = load("Naive_pipeline.zip", ts=ts)
    model = load("Naive_model.zip")

    current_date = ts.df.index[-1]

    # Определите диапазон дат для использования
    start_date = current_date - pd.DateOffset(days=HORIZON*7)

    # Получите временной ряд на заданном диапазоне
    target_values = ts.df[start_date:current_date]

    # Получите значения таргета на заданном горизонт

    return pipeline.forecast().to_pandas(), target_values   #['Капуста']['target'])

def get_trend(ts, product_name):
    trend_tr = TrendTransform('target')
    ans = trend_tr.fit_transform(ts).to_pandas()[product_name].iloc[:, 0]
    return ans

def get_remaining(data, start_date, end_date):
    data['Manufacture_Date'] = pd.to_datetime(data['Manufacture_Date'])
    data['Sale_Date'] = pd.to_datetime(data['Sale_Date'])

    # Создаем столбец с количеством произведенных продуктов для каждой даты
    manufactured_counts = data.groupby('Manufacture_Date').size().rename('Manufactured_Count')

    # Создаем столбец с количеством проданных продуктов для каждой даты
    sold_counts = data.groupby('Sale_Date').size().rename('Sold_Count')

    # Объединяем данные по датам
    result = pd.concat([manufactured_counts, sold_counts], axis=1).fillna(0)

    # Вычисляем количество продуктов на складе для каждой даты
    result['Remaining_Count'] = result['Manufactured_Count'].cumsum() - result['Sold_Count'].cumsum()

    # Задаем диапазон дат, которые вы хотите отобразить
    start_date = start_date
    end_date = end_date

    # Выбираем подмножество данных для заданного диапазона дат
    subset = result.loc[start_date:end_date]

    # Строим график для этого подмножества данных
    return subset.Remaining_Count

def predict(product_name, end_date, data):
    ts = collect_data(data, end_date, product_name)
    ans_trend = get_trend(ts, product_name)
    ans_df, back_df = make_predict_df(ts)    # функция меняет экземпляр ts, аккуратнее, хз как пофиксить
    ans_df = ans_df[product_name]['target']
    back_df = back_df[product_name]['target']
    forecast_pred = pd.concat([back_df, ans_df], axis=0)

    ans_remain = get_remaining(data, '2024-04-01', '2024-04-20').iloc[-50:]


    forecast_pred = list(zip(forecast_pred.index, forecast_pred.values))
    ans_trend = list(zip(ans_trend.index, ans_trend.values))
    ans_remain = list(zip(ans_remain.index, ans_remain.values))

    return forecast_pred, ans_trend, ans_remain
