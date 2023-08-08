import numpy as np, pandas as pd

# exercise 1

chipo = pd.read_csv('chipo.txt', sep='\t')
users = pd.read_csv('user.txt', sep='|')

print(chipo.head(10))

print(chipo.shape)

print(chipo.columns)

indx = chipo.iloc[[0]]

# indx = chipo.iloc[lambda x: x.index % 2 == 0]

print(indx)

value_counts = chipo['item_name'].value_counts()[[0]]
print(value_counts)

value_counts = chipo['choice_description'].value_counts()[[0]]
print(value_counts)

item_price = chipo['item_price'].apply(lambda x: float(x[1:]))

print(item_price.head(2))

sum_prices = item_price.sum()

print(sum_prices)

total_orders = chipo['order_id'].nunique()

print(total_orders)

print(np.round(sum_prices / total_orders, decimals=2))

print(chipo['item_name'].nunique())

# exercise 2

price_more_10 = chipo['item_price'].apply(lambda x : float(x[1:])).where(lambda x: x > 10).value_counts()
print(price_more_10)

print('_________________\nexercise 3')

print(users.head(5))

indx_u = users.loc[[0]]

print('index',indx_u)

user_age_occupation = users.groupby('occupation')['age'].mean()

print(user_age_occupation)

print('_______________\nexercise 4')

print(pd.value_counts(users['user_id']))



# chipo['user_id'] = users['user_id'].apply(lambda x: x)
# print(chipo.head(5))


# data_3 = pd.DataFrame.merge(chipo, users)
# 
# print(data_3.head(10))