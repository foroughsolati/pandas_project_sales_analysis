"""
Sales Data Analysis Project

Author: Forough Solati

Tools:
- Python
- Pandas

Tasks:
1. Calculate total sales
2. Analyze categories
3. Analyze customers
4. Answer business questions
"""

import pandas as pd
#خواندن دیتا
df=pd.read_csv('sales_data.csv')
df['total_price']=df['price'] * df['quantity']

#مجموع کل قروش
total_sales =df['total_price'].sum()
#میانگین کل فروش
average_sales =df['total_price'].mean()
#سقارشی که بیشترین total_price را داشته
max_order =df['total_price'].max()

# category مجموع فروش،میانگین فروش و تعداد فروش در هر 
category_sales =df.groupby('category')['total_price'].sum()
category_mean = df.groupby('category')['total_price'].mean()
category_count = df.groupby('category')['total_price'].count()

#مجموع خرید،تعداد سفارش و میانگین خرید برای هر مشتری   
customer_sales =df.groupby('customer')['total_price'].sum()
customer_count =df.groupby('customer')['total_price'].count()
customer_mean = df.groupby('customer')['total_price'].mean()

#کدام مشتری بیشترین خرید را داشته؟
top_customer =df.groupby('customer')['total_price'].sum().idxmax()

#کدام category  بیشترین فروش را داشته؟
top_category =df.groupby('category')['total_price'].sum().idxmax()

#میانگین فروش Laptop یا Phone بیشتر است؟
means=df.groupby('category')['total_price'].mean()
laptop_vs_phone = means['Laptop'] > means['Phone']

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Max Order:", max_order)

print("Top Customer:", top_customer)
print("Top Category:", top_category)

print("Laptop Average > Phone Average ?")
print(laptop_vs_phone)
