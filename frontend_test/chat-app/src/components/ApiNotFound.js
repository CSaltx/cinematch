import React from "react";

const NotFoundPage = () => {
  const styles = {
    container: {
      height: "100vh",
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      backgroundColor: "#121212",
      color: "#ffffff",
      fontFamily: '"Helvetica Neue", Helvetica, Arial, sans-serif',
    },
    header: {
      fontSize: "6rem",
      fontWeight: "bold",
      letterSpacing: "0.1rem",
    },
    subtext: {
      fontSize: "1.5rem",
      margin: "1rem 0",
    },
    advice: {
      fontSize: "1rem",
      color: "#bbbbbb",
    },
    button: {
      marginTop: "2rem",
      padding: "1rem 2rem",
      fontSize: "1rem",
      borderRadius: "2rem",
      border: "none",
      backgroundColor: "#f05454",
      color: "white",
      cursor: "pointer",
      transition: "background-color 0.3s",
    },
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>404</h1>
      <p style={styles.subtext}>Oops! The API is down.</p>
      <p style={styles.advice}>Check the URL or go back to the homepage.</p>
      <button
        style={styles.button}
        onClick={() => (window.location.href = "/")}
      >
        Retry
      </button>
    </div>
  );
};

export default NotFoundPage;
