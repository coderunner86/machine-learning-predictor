
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

df_allusers = pd.read_table('./data/allusers_pipe.txt', delimiter = '|')
df_sales= pd.read_table('./data/sales_tab.txt',names=['sales_id','list_id','seller_id','buyer_id','event_id','date_id','qty_sold','price_paid','commision','datetime']).dropna()
df_events = pd.read_table('./data/allevents_pipe.txt', delimiter = '|', names=['event_id','venue_id','category_id','date_id','event_name','start_time']).dropna()
df_category = pd.read_table('./data/category_pipe.txt', delimiter = '|', names=['category_id','category_group','category_name','category_description']).dropna()
df_venue = pd.read_table('./data/venue_pipe.txt', delimiter = '|', names=['venue_id','venue_name','venue_city','venue_state','venue_seats']).dropna()
df_date = pd.read_table('./data/date2008_pipe.txt', delimiter = '|', names=['datetime','day','day_id','month','month_id','year', 'holiday']).dropna()

#OBTENIENDO LAS COLUMNAS REQUERIDAS
df_sales['datetime'] = pd.to_datetime(df_sales['datetime']).dt.strftime('%Y-%m-%d')
df_sales['year'] = pd.to_datetime(df_sales['datetime']).dt.strftime('%Y')
df_sales['month'] = pd.to_datetime(df_sales['datetime']).dt.strftime('%m')
df_sales['day_of_week'] = pd.to_datetime(df_sales['datetime']).dt.strftime('%d')
sale_value = df_sales[['qty_sold','price_paid', 'event_id', 'year', 'month', 'day_of_week']]


X = sale_value.loc[:, sale_value.columns != 'qty_sold']
y = df_sales['qty_sold']
def preprocessDataAndPredict():

    #Split data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25)

    #model creation
    lr = LinearRegression()

    #Training
    lr.fit(X_train, y_train)

    #Predict
    predictions = lr.predict(X_test)
    
    return predictions[:7]
    pass


#errors = abs(predictions - test_labels)

#print('Media del error absoluto:', round(np.mean(errors), 2), 'Boletos vendidos.')


#X = df[['venue_id', 'category', 'eventname', 'priceperticket', 'cant_sold', 'sale_date']].values
#y = df['pricepaid'].values

#y_pred = model.predict(X)


  
