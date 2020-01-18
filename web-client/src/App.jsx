import React, { Component } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Home from "./views/home";
import ErrorNotification from "./components/errorNotification";

class App extends Component {
  render() {
    return (
      <div className="App">
        <ErrorNotification />
        <BrowserRouter>
          <Switch>
            <Route exact path="/" component={Home} />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
