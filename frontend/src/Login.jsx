import API_URL from "./Env.jsx";
import "./Login.css";

function Login({ setPage, handleError }) {
  const handleLogin = (event) => {
    const formData = new FormData(event.currentTarget);
    event.preventDefault();
    const username = formData.get("username");
    const password = formData.get("password");
    postLogin(username, password);
  };

  const postLogin = async (username, password) => {
    const body = new URLSearchParams();
    body.append("username", username);
    body.append("password", password);
    try {
      const response = await fetch("http://" + API_URL + "auth/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: body.toString(),
      });

      const data = await response.json();
      if (response.ok) {
        console.log(data);
        localStorage.setItem("token", data["access_token"]);
        setPage("watchlist");
      } else {
        handleError(data.detail);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      <div className="mainBody">
        <h1>Login</h1>
        <form className="inputBody" onSubmit={handleLogin}>
          <input
            className="input"
            type="text"
            name="username"
            placeholder="Username"
            required
          />
          <input
            className="input"
            type="password"
            name="password"
            placeholder="Password"
            required
          />
          <button className="submit" type="submit">
            Submit
          </button>
        </form>
      </div>
    </>
  );
}

export default Login;
