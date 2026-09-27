// Custom JavaScript file

let currentImageIndex = 0;

// Function to cycle through available images
function changeImage() {
    if (typeof imageList !== 'undefined' && imageList.length > 0) {
        currentImageIndex = (currentImageIndex + 1) % imageList.length;
        const imgElement = document.getElementById("displayImage");
        if (imgElement) {
            imgElement.src = imageList[currentImageIndex];
        }
    }
}

// Function to change text message
function changeMessage() {
    var msg = document.getElementById("message");
    if (msg) {
        msg.innerText = "meow javascript is working hehe";
        msg.style.color = "#198754"; // Bootstrap success green
    }
}
