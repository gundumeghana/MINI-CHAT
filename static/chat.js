
const socket = io.connect(window.location.origin);
const input = document.getElementById("message");
const sendBtn = document.getElementById("send");
const messages = document.getElementById("messages");

sendBtn.onclick = function() {
  const msg = input.value.trim();
  if (msg) {
    socket.send(msg);
    input.value = "";
  }
};

socket.on("message", (msg) => {
  const li = document.createElement("li");
  li.textContent = msg;
  messages.appendChild(li);
  messages.scrollTop = messages.scrollHeight;
});
