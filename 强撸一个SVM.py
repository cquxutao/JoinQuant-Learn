import talib
from jqdata import *
from sklearn import svm

test_stock = '399300.XSHE'
start_date = datetime.date(2007,1,4)
end_date = datetime.date(2016,6,3)


trading_days = list(get_all_trade_days())
start_date_index = trading_days.index(start_date)
end_date_index = trading_days.index(end_date)


x_all = []
y_all = []

for index in range(start_date_index,end_date_index):
<<<<<<< HEAD
	start_day = trading_days[index - 30]
	end_day = trading_days[index]
	stock_data = get_price(test_stock,start_date=start_day,end_date=end_day,frequency='daily',fields=['close'])
	close_prices = stock_data['close'].values

	#
	sma_data = talib.SMA(close_prices)[-2]
	wma_data = talib.WMA(close_prices)[-2]
	mom_data = talib.MOM(close_prices)[-2]

	features = []

	features.append(sma_data)
	features.append(wma_data)
	features.append(mom_data)

	label = False
	if close_prices[-1] > close_prices[-2]:
		label = True
	x_all.append(features)
	y_all.append(label)
=======
  start_day = trading_days[index - 30]
  end_day = trading_days[index]
  stock_data = get_price(test_stock,start_date=start_day,end_date=end_day,frequency='daily',fields=['close'])
  close_prices = stock_data['close'].values
  
  #
  sma_data = talib.SMA(close_prices)[-2]
  wma_data = talib.WMA(close_prices)[-2]
  mom_data = talib.MOM(close_prices)[-2]
  
  features = []
  
  features.append(sma_data)
  features.append(wma_data)
  features.append(mom_data)
  
  label = False
  if close_prices[-1] > close_prices[-2]:
    label = True
  x_all.append(features)
  y_all.append(label)
>>>>>>> 强撸一个SVM:joy:

#准备算法需要用到的数据
x_train = x_all[:-1]
y_train = y_all[:-1]
x_test = x_all[-1]
y_test = y_all[-1]
print('data done!')


clf = svm.SVC()

clf.fit(x_train,y_train)

prediction = clf.predict(x_test)

print(prediction == y_test)
print('all done')

