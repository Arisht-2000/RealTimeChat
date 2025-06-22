import React, { useState, useRef, useEffect } from "react";

const ChatArea = () => {
  const [messages, setMessages] = useState([
    { text: "Welcome to the chatroom!", user: "other" }
  ]);
  const [input, setInput] = useState("");
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      setMessages([...messages, { text: input, user: "user" }]);
      setInput("");
    }
  };

  return (
    <div style={{display: "flex", flexDirection: "column", height: "100%"}}>
      <div className="chat-messages" style={{flex: 1, overflowY: "auto", padding: 20, background: "#f7f9fa"}}>
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`message ${msg.user}`}
            style={{
              alignSelf: msg.user === "user" ? "flex-end" : "flex-start",
              background: msg.user === "user" ? "#007bff" : "#e9ecef",
              color: msg.user === "user" ? "#fff" : "#333",
              borderRadius: 18,
              padding: "12px 16px",
              marginBottom: 8,
              maxWidth: "70%",
              boxShadow: "0 2px 8px rgba(0,0,0,0.04)"
            }}
          >
            {msg.text}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <form className="chat-input" onSubmit={handleSubmit} style={{display: "flex", padding: 16, background: "#f1f3f6", borderTop: "1px solid #e0e0e0"}}>
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Type your message..."
          required
          style={{flex: 1, padding: "10px 14px", border: "1px solid #ccc", borderRadius: 20, fontSize: "1rem"}}
        />
        <button type="submit" style={{background: "#007bff", color: "#fff", border: "none", borderRadius: "50%", width: 40, height: 40, marginLeft: 10, fontSize: "1.2rem", cursor: "pointer"}}>
          <i className="fas fa-paper-plane"></i>
        </button>
      </form>
    </div>
  );
};

export default ChatArea;
