import React from "react";
import "./App.css";
import ChatComponent from "./components/ChatUI";
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";

function App() {
  return (
    <div className="App">
      <ChatComponent />
    </div>
  );
}

export default App;
