async function sendMessage() {
  const inputField = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const userMessage = inputField.value.trim();
  if (!userMessage) return;

  appendMessage(userMessage, "user");
  inputField.value = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage }),
    });

    const data = await response.json();

    if (data.reply) {
      appendMessage(data.reply, "bot");
    } else {
      appendMessage("⚠️ Sorry, something went wrong.", "bot");
    }
  } catch (error) {
    appendMessage("⚠️ Network error. Please try again.", "bot");
  }
}

function appendMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");
  const messageDiv = document.createElement("div");
  messageDiv.className = `message ${sender}`;
  messageDiv.innerText = text;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
