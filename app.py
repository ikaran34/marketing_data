import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
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

# Show revenue distribution with a histogram
st.subheader("Revenue Distribution")
fig, ax = plt.subplots()
ax.hist(df['Revenue'], bins=10, color='blue', edgecolor='black')
ax.set_title('Distribution of Revenue')
ax.set_xlabel('Revenue')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Show a line chart for trend analysis (if relevant data exists)
st.subheader("Revenue Trend Over Time")
fig, ax = plt.subplots()
df['Date'] = pd.to_datetime(df['Date'])
df_sorted = df.sort_values(by='Date')
ax.plot(df_sorted['Date'], df_sorted['Revenue'], marker='o', color='green')
ax.set_title('Revenue Trend Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Revenue')
st.pyplot(fig)

# Option to filter data (example: filter by channel)
st.subheader("Filter Data by Marketing Channel")
channel = st.selectbox("Select Marketing Channel", df['Channel'].unique())
filtered_data = df[df['Channel'] == channel]
st.write(f"Showing data for {channel} marketing channel")
st.write(filtered_data)

# Additional plots or analysis can be added below
