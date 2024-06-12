console.log("IiI")
document.addEventListener("DOMContentLoaded", function() {
    const iconContainer = document.getElementById("icon-container");
  
    // Function to create a random position for an icon
    function getRandomPosition() {
      const pageHeight = document.body.clientHeight;
      const pageWidth = document.body.clientWidth;
  
      const topPosition = Math.random() * 10;
      const leftPosition = Math.random() * 10;
  
      return { top: topPosition, left: leftPosition };
    }
  
    // Function to create an icon element
    function createIcon() {
      const icon = document.createElement("div");
      icon.className = "icon bg-blue-500 rounded-full";
  
      const { top, left } = getRandomPosition();
      icon.style.top = `${top}px`;
      icon.style.left = `${left}px`;
  
      iconContainer.appendChild(icon);
  
      // Remove the icon after the animation duration
      setTimeout(() => {
        icon.remove();
      }, 5000); // 5000 milliseconds (5 seconds) matches the animation duration
    }
  
    // Create icons at intervals (adjust as needed)
    setInterval(createIcon, 1000); // Create an icon every second
  });
  