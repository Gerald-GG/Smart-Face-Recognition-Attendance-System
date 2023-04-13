// Define function to execute the Check Camera script
function checkCamera() {
    fetch("/check_camera")
        .then(response => response.json())
        .then(data => console.log(data.output))
        .catch(error => console.log(error));
}

// Define function to execute the Capture Image script
function captureImage() {
    fetch("/capture_image")
        .then(response => response.json())
        .then(data => console.log(data.output))
        .catch(error => console.log(error));
}

// Define function to execute the Train Images script
function trainImages() {
    fetch("/train_images")
        .then(response => response.json())
        .then(data => console.log(data.output))
        .catch(error => console.log(error));
}

// Define function to execute the Recognize script
function recognize() {
    fetch("/recognize")
        .then(response => response.json())
        .then(data => console.log(data.output))
        .catch(error => console.log(error));
}

// Define function to execute the Semester Report script
function semReport() {
    fetch("/sem_report")
        .then(response => response.json())
        .then(data => console.log(data.output))
        .catch(error => console.log(error));
}

// Define function to execute the Automail script
function automail() {
    fetch("/automail")
        .then(response => response.json())
        .then(data => console.log(data.output))
        .catch(error => console.log(error));
}

// Add event listeners to the buttons
document.getElementById("checkCamera").addEventListener("click", checkCamera);
document.getElementById("captureImage").addEventListener("click", captureImage);
document.getElementById("trainImages").addEventListener("click", trainImages);
document.getElementById("recognize").addEventListener("click", recognize);
document.getElementById("generateSemReport").addEventListener("click", semReport);
document.getElementById("automail").addEventListener("click", automail);