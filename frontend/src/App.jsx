import { useState } from "react";
import Login from "./Login.jsx";
import Register from "./Register.jsx";
import Error from "./Error.jsx";
import Lists from "./Lists.jsx";
import User from "./User.jsx";

import "./App.css";

function App() {
  const [page, setPage] = useState("lists");
  const [error, setError] = useState("");
  const [username, setUsername] = useState("");

  const handleError = (err) => {
    setError(err);
    setTimeout(() => {
      setError("");
    }, 5000);
  };

  return (
    <>
      <div className="mainBody">
        <div className="navBody">
          <button
            className={page === "lists" ? "navButton selected" : "navButton"}
            onClick={() => setPage("lists")}
          >
            Lists
          </button>
          <button
            className={page === "user" ? "navButton selected" : "navButton"}
            onClick={() => setPage("user")}
          >
            User
          </button>
          <button
            className={page === "login" ? "navButton selected" : "navButton"}
            onClick={() => setPage("login")}
          >
            Login
          </button>
          <button
            className={page === "register" ? "navButton selected" : "navButton"}
            onClick={() => setPage("register")}
          >
            Register
          </button>
        </div>
      </div>
      <Error error={error} />
      <Tab
        page={page}
        setPage={(page) => setPage(page)}
        handleError={(err) => handleError(err)}
        username={username}
        setUsername={(username) => setUsername(username)}
      />
    </>
  );
}

function Tab({ page, setPage, handleError, username, setUsername }) {
  switch (page) {
    case "list":
      return (
        <Lists
          setPage={(page) => setPage(page)}
          handleError={(err) => handleError(err)}
        />
      );

    case "login":
      return (
        <Login
          setPage={(page) => setPage(page)}
          handleError={(err) => handleError(err)}
        />
      );

    case "register":
      return (
        <Register
          setPage={(page) => setPage(page)}
          handleError={(err) => handleError(err)}
        />
      );

    case "user":
      return (
        <User
          setPage={(page) => setPage(page)}
          handleError={(err) => handleError(err)}
          username={username}
          setUsername={(username) => setUsername(username)}
        />
      );

    default:
      return (
        <Lists
          setPage={(page) => setPage(page)}
          handleError={(err) => handleError(err)}
        />
      );
  }
}

export default App;
