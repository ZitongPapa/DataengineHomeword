import pandas as pd
from fbprophet import Prophet

# DataFrame处理为Prophet模型需要的数据
def data_manage(df):
	# 转化时间格式，去掉多余列
	df['Datetime']=pd.to_datetime(df.Datetime,format='%d-%m-%Y %H:%M')
	df.index=df.Datetime
	df.drop(['ID','Datetime'],axis=1,inplace=True)
	# 按天采集
	df_daily=df.resample('D').sum()
	df_daily['ds']=df_daily.index
	df_daily['y']=df_daily.Count
	df_daily.drop(['Count'],axis=1,inplace=True)
	return df_daily


def prophet_predic(df_daliy):
	# 拟合prophet模型
	m= Prophet(yearly_seasonality=True,seasonality_prior_scale=0.1)
	m.fit(df_daily)
	# 预测未来7个月 213天
	future=m.make_future_dataframe(periods=213)
	forecast= m.predict(future)
	m.plot(forecast)
	m.plot_components(forecast)

if __name__ == '__main__':
	df=pd.read_csv('train.csv')
	df_daily= data_manage(df)
	prophet_predic(df_daily)