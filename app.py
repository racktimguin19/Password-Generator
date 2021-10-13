from flask import Flask, render_template, request
from password_generator import generate_password
import pyperclip


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Password length given by the user
        password_length = int(request.form.get('pw-length'))

        # Generating Password
        password = generate_password(password_length)

        # Copy password to clipboard
        pyperclip.copy(password)

        return render_template("index.html", password=password, password_length=password_length)

    # Setting the minimum password length to 4
    password_length = 4

    return render_template("index.html", password_length=password_length)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')