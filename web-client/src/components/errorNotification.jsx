import React from "react";

const ErrorNotification = () => {
  return (
    <div
      className="alert alert-danger"
      role="alert"
      id="error-alert"
      style={{
        zIndex: "999",
        position: "absolute",
        right: "20px",
        top: "-100px",
        transition: "top 0.5s ease"
      }}
    ></div>
  );
};

export default ErrorNotification;
