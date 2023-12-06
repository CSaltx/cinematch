import React from "react";
import ReactMarkdown from "react-markdown";
import "./CustomMessage.css"; // Make sure this is uncommented

const CustomMessage = ({ text, position, dateString, isUserMessage }) => {
  const messageClass = isUserMessage ? "user-message" : "bot-message";
  return (
    <div className={`message ${position} ${messageClass}`}>
      <div className="message-content">
        {isUserMessage ? (
          text // Render plain text for user messages
        ) : (
          <ReactMarkdown>{text}</ReactMarkdown> // Render markdown for bot messages
        )}
      </div>
      <div className="message-date">{dateString}</div>
    </div>
  );
};

export default CustomMessage;
