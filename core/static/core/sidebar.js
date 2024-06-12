// document.addEventListener("DOMContentLoaded", function() {

//     console.log("Sidebar")

//     var trackForm = document.getElementById("track_form");
//     var trackLink = document.getElementById("track_link");
//     var sidebar = document.getElementById("sidebar");
//     var destination = document.getElementById("destination");

//     console.log(sidebar)

//     if (trackLink && sidebar) {
//         trackLink.addEventListener("click", function(event) {
//             event.preventDefault();
//             sidebar.style.display = "block";
//         });
//     } else {
//         console.error("Track link or sidebar element not found");
//     }

// });
document.addEventListener("DOMContentLoaded", function() {

    console.log("Sidebar")

    var trackLink = document.getElementById("track_link");
    var sidebar = document.getElementById("sidebar");
    var trackForm = document.getElementById("track_form");
    var destination = document.getElementById("destination");

    console.log(sidebar)
    console.log(trackLink)
    console.log(trackForm)
    console.log(destination)


    if (trackLink && sidebar) {
        trackLink.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent default link behavior
            sidebar.style.display = "block"; // Show sidebar
        });
    } else {
        console.error("Track link or sidebar element not found");
    }

    if (trackForm) {
        trackForm.addEventListener("submit", function(event) {
            event.preventDefault();
            var formData = new FormData(trackForm);
            fetch(trackForm.action, {
                method: trackForm.method,
                body: formData,
            })
            .then(response => response.text())
            .then(data => {
                destination.textContent = data;
                sidebar.style.display = "block"; 
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    } else {
        console.error("Track form element not found");
    }
});
    