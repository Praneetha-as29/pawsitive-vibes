from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# File to store registration data
EXCEL_FILE = "user_data.xlsx"

# Ensure the Excel file exists
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=["Name", "Department", "Year", "Section", "Password"])
    df.to_excel(EXCEL_FILE, index=False)

@app.route("/")
def home():
    return redirect(url_for("register"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        department = request.form["department"]
        year = request.form["year"]
        section = request.form["section"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "❌ Passwords do not match! <a href='/register'>Try again</a>"

        # Read existing data
        df = pd.read_excel(EXCEL_FILE)

        # Append new user data
        new_user = pd.DataFrame([[name, department, year, section, password]],
                                columns=["Name", "Department", "Year", "Section", "Password"])
        df = pd.concat([df, new_user], ignore_index=True)

        # Save back to Excel
        df.to_excel(EXCEL_FILE, index=False)

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
