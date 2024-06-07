import pandas as pd
import numpy as np
import scipy as sp
import statsmodels as stats
from matplotlib import pyplot as plt
import seaborn as sb


order_df = pd.read_excel(r'C://Users//Administrator//Downloads//SuperstoreDataset.xlsx', 'Orders')
def second_q(order_df):
    no_disc = 0
    discounts = order_df["Discount"]
    #grouped_df_no_disc = order_df.groupby("Discount")
    for item in discounts:
        if item == 0:
            no_disc += 1

    return no_disc

def search_data(order_df):
    zero_discount_array = []
    for item in order_df:
        print(item)
        if item == "Discount":
            print(item)
            zero_discount_array.append(item)

    return zero_discount_array

no_disc_array = search_data(order_df)
filtered_rows = order_df[order_df["Discount"] == 0]["Product_ID"]
# print(f"{no_disc_array}")
print(filtered_rows)




#     grouped_df_no_disc = order_df.groupby("Discount")
#    # grouped_df_subcat = df.groupby(["Category", "Sub-Category"]).agg({"Sales": "max", "Profit": "max"})
#     return grouped_df_no_disc
#    # return grouped_df_cat.columns


#
zero_disc = second_q(order_df)
print(zero_disc)