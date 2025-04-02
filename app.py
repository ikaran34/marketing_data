import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("marketing_data.csv")

# Title of the app
st.title("Marketing Data Insights")

# Show the dataframe
st.subheader("Marketing Data")
st.write(df)

# Calculate and display average revenue
avg_revenue = df['Revenue'].mean()
st.write(f"Average Revenue: {avg_revenue}")

# Show some basic statistics of the data
st.subheader("Data Statistics")
st.write(df.describe())

# Group data by Region and sum the revenue
region_revenue = df.groupby('Region')['Revenue'].sum()

# Show revenue distribution with a histogram
st.subheader("Revenue Distribution")
fig, ax = plt.subplots()
ax.hist(df['Revenue'], bins=10, color='blue', edgecolor='black')
ax.set_title('Distribution of Revenue')
ax.set_xlabel('Revenue')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Display bar chart for revenue by Region
st.title("Revenue by Region")
st.bar_chart(region_revenue)

# You can also display additional stats if needed
st.write(f"Total Revenue: ${region_revenue.sum():,}")

# Optionally, you can also show the data in a table format
st.subheader("Revenue Data by Region")
st.write(region_revenue)

# You can add any other visualizations or analysis as needed.
