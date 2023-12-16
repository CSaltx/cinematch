import React, { useState, useEffect } from "react";
import "react-chat-elements/dist/main.css";
import { MessageBox, Input, Button } from "react-chat-elements";
import CustomMessage from "./CustomMessage"; // Import your custom message component
import "./ChatComponent.css";
import ApiNotFound from "./ApiNotFound.js";
import TypingInd from "./TypingIndicator.js";
import "./ChatComponent.css";
import LoadingSpinner from "./LoadingSpinner";

const ChatComponent = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [alive, setAlive] = useState(true);

  useEffect(() => {
    const checkStatus = async () => {
      fetch("http://localhost:5001/health", {
        method: "GET",
        headers: {
          "Content-Type": "Application/json",
        },
      })
        .then((response) => {
          console.log(response)
          return response.json()
        })
        .then((data) => {
          console.log(data.status);
          if (data.status === "up") {
            setAlive(true);
            setIsLoading(false);
          } else {
            setIsLoading(true);
            setAlive(false);
          }
        })
        .catch((error) => {
          console.error("API check failed", error);
          setAlive(false);
          setIsLoading(false);
        });
    };

    // Call the checkStatus function
    checkStatus();

    const interval = setInterval(checkStatus, 10000); // Check every 10 seconds
    return () => clearInterval(interval); // Cleanup interval on unmount
  }, []); // The empty array causes this effect to only run on mount and unmount

  const sendMessage = (content) => {
    setIsLoading(true);

    const newMessage = {
      position: "right",
      type: "text",
      text: inputValue, // Use inputValue from the state
      date: new Date(),
    };
    setMessages([...messages, newMessage]);
    setInputValue("");

    fetch("http://localhost:5001/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: inputValue }), // Use inputValue here
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((responseData) => {
        const botMessage = {
          position: "left",
          type: "text",
          text: responseData.response, // Use inputValue from the state
          date: new Date(),
        };
        // Add the bot's response message
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      })
      .catch((error) => {
        console.error("Could not send the message to the API", error);
      })
      .finally(() => {
        setIsLoading(false); // End loading
      });
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      // Send message on Enter key, but not when Shift is held
      e.preventDefault();
      sendMessage();
    }
  };


  return (
    <div className="chat-container">
      {alive ? (
        <>
          <div className="messages-container">
            {messages.map((msg, index) => (
              <CustomMessage
                key={index}
                text={msg.text}
                position={msg.position}
                dateString={msg.date.toLocaleTimeString()}
                isUserMessage={msg.position === "right"}
              />
            ))}
          </div>
          <div className="App">
            {isLoading && <LoadingSpinner /> }
          </div>
          <Input
            placeholder="Type here..."
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handleKeyPress} // Add the key press handler
            rightButtons={
              <Button
                color="white"
                backgroundColor="black"
                text="Send"
                onClick={sendMessage}
              />
            }
          />
        </>
      ) : (
        <ApiNotFound />
      )}
    </div>
  );
};

export default ChatComponent;
