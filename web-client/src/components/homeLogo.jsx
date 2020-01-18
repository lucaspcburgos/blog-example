import React from "react";
import "./../style/homeLogo.css";

export default class HomeLogo extends React.Component {
  render() {
    return (
      <div className="home-logo-container">
        <div>
          <label>Blog</label>
          <br></br>
          <label style={{ color: "#4CB1F7" }}>Example</label>
        </div>
      </div>
    );
  }
}
