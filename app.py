from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
DATA_FILE = "zoo_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    animals = load_data()
    return render_template("index.html", animals=animals)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    species = request.form['species']
    age = request.form['age']
    data = load_data()
    data.append({"name": name, "species": species, "age": age})
    save_data(data)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    data = load_data()
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
