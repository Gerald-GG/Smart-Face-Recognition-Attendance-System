from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Define route to display the index page
@app.route("/")
def index():
    return render_template("index.html")

# Define route to execute the Check_Camera.py script
@app.route("/check_camera")
def check_camera():
    # Execute the Check_Camera.py script and capture its output
    output = subprocess.check_output(["python", "Check_Camera.py"])
    
    # Convert the output to a JSON response
    response = {"output": output.decode("utf-8")}
    
    # Return the JSON response
    return jsonify(response)

# Define route to execute the capture_image.py script
@app.route("/capture_image")
def capture_image():
    # Execute the capture_image.py script and capture its output
    output = subprocess.check_output(["python", "capture_image.py"])
    
    # Convert the output to a JSON response
    response = {"output": output.decode("utf-8")}
    
    # Return the JSON response
    return jsonify(response)

# Define route to execute the Traing_Images.py script
@app.route("/train_images")
def train_images():
    # Execute the Traing_Images.py script and capture its output
    output = subprocess.check_output(["python", "Traing_Images.py"])
    
    # Convert the output to a JSON response
    response = {"output": output.decode("utf-8")}
    
    # Return the JSON response
    return jsonify(response)

# Define route to execute the Recognize.py script
@app.route("/recognize")
def recognize():
    # Execute the Recognize.py script and capture its output
    output = subprocess.check_output(["python", "Recognize.py"])
    
    # Convert the output to a JSON response
    response = {"output": output.decode("utf-8")}
    
    # Return the JSON response
    return jsonify(response)

# Define route to execute the Sem_Report.py script
@app.route("/sem_report")
def sem_report():
    # Execute the Sem_Report.py script and capture its output
    output = subprocess.check_output(["python", "Sem_Report.py"])
    
    # Convert the output to a JSON response
    response = {"output": output.decode("utf-8")}
    
    # Return the JSON response
    return jsonify(response)

# Define route to execute the Automail.py script
@app.route("/automail")
def automail():
    # Execute the Automail.py script and capture its output
    output = subprocess.check_output(["python", "Automail.py"])
    
    # Convert the output to a JSON response
    response = {"output": output.decode("utf-8")}
    
    # Return the JSON response
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
