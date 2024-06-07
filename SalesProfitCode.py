import pandas as pd
import numpy as np
import scipy as sp
import statsmodels as stats
from matplotlib import pyplot as plt
import seaborn as sb


def double_bar_chart(grouped_df, target_col, value_col1, value_col2):
    # Extract the necessary columns
    subcategories = grouped_df[target_col]
    values1 = grouped_df[value_col1]
    values2 = grouped_df[value_col2]

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))

    # Define bar width and positions
    bar_width = 0.35
    index = np.arange(len(subcategories))

    # Plot the bars for the first value column
    bars1 = ax.bar(index - bar_width / 2, values1, bar_width, label=value_col1, color='b', edgecolor='black')

    # Plot the bars for the second value column
    bars2 = ax.bar(index + bar_width / 2, values2, bar_width, label=value_col2, color='r', edgecolor='black')

    ax.set_xlabel(target_col)
    ax.set_ylabel('Values')
    ax.set_title(f'Double Bar Chart of {value_col1} and {value_col2} by {target_col}')
    ax.set_xticks(index)
    ax.set_xticklabels(subcategories, rotation=45)
    ax.legend()

    plt.tight_layout()
    plt.show()


def first_question(df):
    grouped_df_cat = df.groupby("Category").agg({"Sales": "max", "Profit": "max"})
    grouped_df_subcat = df.groupby(["Category", "Sub-Category"]).agg({"Sales": "max", "Profit": "max"})

    return grouped_df_cat.columns
    # double_bar_chart(grouped_df_cat, "Category", "Sales", "Profit")


orders_df = pd.read_excel("/content/drive/MyDrive/Current_Working_Datasets/PEAK_AI_Dataset/Superstore_Dataset.xlsx",
                          sheet_name="Orders")
people_df = pd.read_excel("/content/drive/MyDrive/Current_Working_Datasets/PEAK_AI_Dataset/Superstore_Dataset.xlsx",
                          sheet_name="People")

peak_dfs = [orders_df, people_df]

df = peak_dfs[0]

first_question(df)