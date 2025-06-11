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
def home():
    return render_template("form.html")  # Only shows the form

@app.route('/add', methods=['POST'])
def add_animal():
    data = load_data()
    new_animal = {
        "name": request.form['name'],
        "species": request.form['species'],
        "age": request.form['age'],
        "caretaker": request.form['caretaker'],
        "feeding_schedule": request.form['feeding_schedule'],
        "vet_checkups": request.form['vet_checkups'],
        "tickets": request.form['tickets'],
        "visitors": request.form['visitors'],
    }
    data.append(new_animal)
    save_data(data)
    return redirect("/records")  # Redirect to new page

@app.route('/records')
def show_records():
    animals = load_data()
    return render_template("records.html", animals=animals)

@app.route('/delete/<int:index>')
def delete_animal(index):
    data = load_data()
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
    return redirect("/records")
