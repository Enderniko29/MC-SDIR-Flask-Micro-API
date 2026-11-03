from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('cars.csv')

@app.route('/cars')
def cars():
    return jsonify(df.head(10).to_dict(orient='records'))

@app.route('/manufacturers')
def manufacturers():
    return jsonify(df['CarName'].str.split().str[0].unique().tolist())

@app.route('/cars/prices')
def cars_prices():
    return jsonify(df[['CarName', 'price']].to_dict(orient='records'))


@app.route('/')
def index():
    return jsonify({"message": "Welcome to my first api"})

if __name__ == '__main__':
    app.run(debug=True, port = 8080)