import React from "react";
import "./style/home.css";
import SignupForm from "../components/signupForm";
import SigninForm from "./../components/signinForm";
import HomeLogo from "./../components/homeLogo";

export default class Home extends React.Component {
  state = {
    currentForm: "signup"
  };

  showForm = () => {
    switch (this.state.currentForm) {
      case "signup":
        return <SignupForm />;
      case "signin":
        return <SigninForm />;
      default:
        return <SignupForm />;
    }
  };

  setCurrentForm = type => {
    this.setState({
      currentForm: type
    });
  };

  render() {
    return (
      <div>
        <div className="home-form">
          <div className="btn-group" role="group" aria-label="Basic example">
            <button
              type="button"
              className="btn btn-secondary"
              onClick={() => {
                this.setCurrentForm("signin");
              }}
            >
              SignIn
            </button>
            <button
              type="button"
              className="btn btn-secondary"
              onClick={() => {
                this.setCurrentForm("signup");
              }}
            >
              SignUp
            </button>
          </div>
          <div className="form-container">{this.showForm()}</div>
        </div>
        <HomeLogo />
      </div>
    );
  }
}
