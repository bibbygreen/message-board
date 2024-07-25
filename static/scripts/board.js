document.getElementById("upload").addEventListener("change", function (event) {
  const fileName = event.target.files[0]
    ? event.target.files[0].name
    : "No file chosen";
  document.getElementById("file-name").textContent = fileName;
});

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
    console.log(result);

    if (response.ok) {
      const messagesContainerDiv = document.querySelector(
        ".messages-container"
      );
      const messageDiv = document.createElement("div");
      messageDiv.className = "message-box";

      const messageImage = document.createElement("img");
      messageImage.src = result.file_url;
      messageImage.alt = "Uploaded Image";
      messageDiv.appendChild(messageImage);

      const usernameDiv = document.createElement("div");
      usernameDiv.className = "div-username";
      usernameDiv.textContent = result.username;
      messageDiv.appendChild(usernameDiv);

      const messageParagraph = document.createElement("p");
      messageParagraph.className = "p-message-text";
      messageParagraph.textContent = result.message;
      messageDiv.appendChild(messageParagraph);

      messagesContainerDiv.appendChild(messageDiv);
    } else {
      alert("Failed to submit message");
    }
  } catch (error) {
    console.error("Error", error);
  }
});
