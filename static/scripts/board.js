const messageForm = document.getElementById("messageForm");
messageForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const formData = new FormData(this);
  try {
    const response = await fetch("/submit-message", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();

    if (response.ok) {
      const messagesDiv = document.getElementById("messages");
      const messageDiv = document.createElement("div");

      const messageParagraph = document.createElement("p");
      messageParagraph.textContent = result.message;

      const messageImage = document.createElement("img");
      messageImage.src = result.file_url;
      messageImage.alt = "Uploaded Image";
      messageImage.style.maxWidth = "200px";

      messageDiv.appendChild(messageParagraph);
      messageDiv.appendChild(messageImage);

      messagesDiv.appendChild(messageDiv);
    } else {
      alert("Failed to submit message");
    }
  } catch (error) {
    console.error("Error", error);
  }
});
