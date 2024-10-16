import API_URL from "./Env.jsx";
import "./Login.css";

function Register({ setPage, handleError }) {
  const handleLogin = (event) => {
    const formData = new FormData(event.currentTarget);
    event.preventDefault();
    const username = formData.get("username");
    const password = formData.get("password");
    postRegister(username, password);
  };

  const postRegister = async (username, password) => {
    const body = {
      username: username,
      password: password,
    };
    try {
      const response = await fetch("http://" + API_URL + "users/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
        },
        body: JSON.stringify(body),
      });

      const data = await response.json();
      if (response.ok) {
        setPage("login");
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
        <h1>Register</h1>
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

export default Register;
