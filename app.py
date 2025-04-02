import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("marketing_data.csv")

# Group data by Region and sum the revenue
region_revenue = df.groupby('Region')['Revenue'].sum()

# Display bar chart for revenue by Region
st.title("Revenue by Region")
st.bar_chart(region_revenue)

# You can also display additional stats if needed
st.write(f"Total Revenue: ${region_revenue.sum():,}")

# Optionally, you can also show the data in a table format
st.subheader("Revenue Data by Region")
st.write(region_revenue)

# You can add any other visualizations or analysis as needed.
