import React from "react";
import api from "./../api/user";
import { showError } from "./../notification";

export default class SignupForm extends React.Component {
  state = {
    email: "",
    username: "",
    password: "",
    confirmPassword: "",
    checkBox: false
  };

  getEmail = event => {
    this.setState({
      email: event.target.value
    });
  };

  getUsername = event => {
    this.setState({
      username: event.target.value
    });
  };

  getPassword = event => {
    this.setState({
      password: event.target.value
    });
  };

  getConfirmPassword = event => {
    this.setState({
      confirmPassword: event.target.value
    });
  };

  submitForm = event => {
    event.preventDefault();
    if (!this.state.email) {
      return showError("E-mail is required");
    }
    if (!this.state.username) {
      return showError("Username is required");
    }
    if (!this.state.password) {
      return showError("Password is required");
    }
    if (!this.state.checkBox) {
      return showError("Check terms and conditions");
    }
    if (this.state.password !== this.state.confirmPassword) {
      return showError("Passwords don't match");
    }
    api.profile
      .userSignup({
        email: this.state.email,
        username: this.state.username,
        password: this.state.password
      })
      .then(response => {
        console.log(response);
      })
      .catch(err => {
        showError(err.response.data.description);
      });
  };

  getCheckbox = () => {
    this.setState({
      checkBox: !this.state.checkBox
    });
  };

  render() {
    return (
      <form onSubmit={this.submitForm}>
        <h1 style={{ textAlign: "center" }}>Sign up</h1>
        <div className="form-group">
          <label htmlFor="email">Email address</label>
          <input
            type="email"
            className="form-control"
            id="email"
            aria-describedby="emailHelp"
            onChange={this.getEmail}
          />
          <small id="emailHelp" className="form-text text-muted">
            We'll never share your email with anyone else.
          </small>
        </div>
        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            className="form-control"
            id="username"
            onChange={this.getUsername}
          />
        </div>

        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            onChange={this.getPassword}
          />
        </div>
        <div className="form-group">
          <label htmlFor="confirmPassword">Confirm password</label>
          <input
            type="password"
            className="form-control"
            id="confirmPassword"
            onChange={this.getConfirmPassword}
          />
        </div>
        <div className="form-group form-check">
          <input
            type="checkbox"
            className="form-check-input"
            id="exampleCheck1"
            onChange={this.getCheckbox}
          />
          <label className="form-check-label" htmlFor="exampleCheck1">
            I agree with terms and conditions
          </label>
        </div>
        <button type="submit" className="btn btn-primary">
          Sign up
        </button>
      </form>
    );
  }
}
