from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("marketing_data.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filter', methods=['GET', 'POST'])
def filter_data():
    filtered_df = df  # Start with all data

    if request.method == 'POST':
        min_revenue = request.form.get('min_revenue')
        
        if min_revenue:
            min_revenue = float(min_revenue)
            filtered_df = df[df['Revenue'] >= min_revenue]  # Filter rows

    return render_template('filter.html', tables=[filtered_df.to_html(classes='data')], titles=filtered_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
