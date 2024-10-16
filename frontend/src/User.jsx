import API_URL from "./Env.jsx";
import CheckToken from "./Auth.jsx";
import { useState, useEffect } from "react";
import "./Login.css";

function User({ setPage, handleError, username, setUsername }) {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [jpTitles, setJpTitles] = useState(false);

  useEffect(() => {
    if (!CheckToken()) {
      setPage("login");
      handleError("You must be logged in");
      return;
    }
    setToken(localStorage.getItem("token"));
    getCurrentUser();
    getSettings();
  }, []);

  const getSettings = async () => {
    try {
      const response = await fetch("http://" + API_URL + "users/settings", {
        method: "GET",
        headers: { Authorization: `Bearer ${token}` },
      });

      const data = await response.json();
      if (response.ok) {
        setJpTitles(data.japanese_titles);
      } else {
        handleError(data.detail);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const putSettings = async () => {
    const body = {
      japanese_titles: !jpTitles,
    };
    try {
      const response = await fetch("http://" + API_URL + "users/settings", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Authorization: `Bearer ${token}`,
        },

        body: JSON.stringify(body),
      });

      const data = await response.json();
      if (response.ok) {
        setJpTitles(data.japanese_titles);
      } else {
        handleError(data.detail);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const getCurrentUser = async () => {
    try {
      const response = await fetch("http://" + API_URL + "users/current", {
        method: "GET",
        headers: { Authorization: `Bearer ${token}` },
      });

      const data = await response.json();
      if (response.ok) {
        setUsername(data.username);
      } else {
        handleError(data.detail);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const logout = () => {
    setUsername("");
    localStorage.clear();
    setPage("login");
    handleError(`${username} logged out`);
  };

  return (
    <>
      <div className="mainBody">
        <h1>{username === "" ? "User" : username}</h1>
        <div className="inputBody">
          <button className="input" onClick={() => putSettings()}>
            Toggle Japanese Titles: {jpTitles ? "True" : "False"}
          </button>
          <button className="input" onClick={() => logout()}>
            Logout
          </button>
        </div>
      </div>
    </>
  );
}

export default User;
