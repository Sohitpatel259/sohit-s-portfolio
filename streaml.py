import streamlit as st
import streamlit.components.v1 as components

# ------------------------
chatbot_html = """
<link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet" />

<div id="n8n-chat"></div>

<script type="module">
  import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';

  createChat({
    webhookUrl: "https://sohitpatel.app.n8n.cloud/webhook/1c0d08f0-abd0-4bdc-beef-370c27aae1a0/chat",
    target: "#n8n-chat",
    mode: "overlay",
    chatTitle: "💬 fraud detection Assistant",
    theme: "light",
    showWelcomeMessage: true
  });
</script>
"""

# Display chatbot widget inside Streamlit
components.html(chatbot_html, height=600, width=800)
