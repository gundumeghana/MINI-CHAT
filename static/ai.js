
const input = document.getElementById("message");
const sendBtn = document.getElementById("send");
const messages = document.getElementById("messages");

function addMessage(text, fromUser = true) {
  const li = document.createElement("li");
  li.textContent = (fromUser ? "You: " : "AI: ") + text;
  messages.appendChild(li);
  messages.scrollTop = messages.scrollHeight;
}

sendBtn.onclick = async function() {
  const msg = input.value.trim();
  if (!msg) return;
  addMessage(msg, true);
  input.value = "";

  const res = await fetch("/api/ai-reply", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg })
  });
  const data = await res.json();
  addMessage(data.reply, false);
};
