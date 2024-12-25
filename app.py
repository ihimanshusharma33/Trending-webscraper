from flask import Flask, render_template
import subprocess
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("______MONOGO_URI______")  
db = client['twitter_trends']
collection = db['trending_topics']

@app.route("/")
def home():
    return '''
    <html>
        <body>
            <h1>Twitter Trending Topics</h1>
            <button onclick="window.location.href='/run-script'">Click here to run the script</button>
        </body>
    </html>
    '''

@app.route("/run-script")
def run_script():
    # Run the Selenium script
    subprocess.run(["python", "selenium_script.py"])

    # Fetch the latest record from MongoDB
    record = collection.find_one(sort=[('_id', -1)])

    if not record:
        return "No data found."

    # Return the trending topics to the webpage
    return f'''
    <html>
        <body>
            <h1>Twitter Trending Topics</h1>
            <p>These are the most happening topics as on {record['end_time']}</p>
            <ul>
                {"".join([f"<li>{trend}</li>" for trend in record['trends']])}
            </ul>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
