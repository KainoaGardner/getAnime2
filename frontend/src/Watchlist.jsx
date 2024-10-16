import API_URL from "./Env.jsx";
import { useState, useEffect } from "react";

function Watchlist({ handleError, removeAnime, token, jp, sort, sortAnime }) {
  const [watchlist, setWatchlist] = useState([]);
  const [confirm, setConfirm] = useState("");

  useEffect(() => {
    getWatchlist();
  }, [removeAnime, sort]);

  const getWatchlist = async () => {
    try {
      const response = await fetch("http://" + API_URL + "entries/all", {
        method: "GET",
        headers: { Authorization: `Bearer ${token}` },
      });

      const data = await response.json();
      if (response.ok) {
        setWatchlist(sortAnime(data));
      } else {
        handleError(data.detail);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const clearWatchlist = async () => {
    setConfirm("");
    try {
      const response = await fetch("http://" + API_URL + "entries/clear", {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
      });

      const data = await response.json();
      if (response.ok) {
        setWatchlist([]);
      } else {
        handleError(data.detail);
      }
    } catch (error) {
      console.log(error);
    }
  };

  if (watchlist.length === 0) {
    return (
      <>
        <div>
          <h1>Watchlist</h1>
          <h2>Empty watchlist</h2>
        </div>
      </>
    );
  }

  return (
    <>
      <div>
        <div className="mainBody">
          <h1>Watchlist</h1>
          {confirm !== "" ? (
            <div className="inputBody">
              <h3>Are you sure you want to clear</h3>
              <button onClick={() => clearWatchlist()}>Clear</button>
              <button onClick={() => setConfirm("")}>Cancel</button>
            </div>
          ) : (
            <button
              className="addremButton"
              onClick={() => setConfirm("confirm")}
            >
              Clear Watchlist
            </button>
          )}
        </div>

        <div>
          {watchlist.map((animeObj) => (
            <div className="mainBody" key={animeObj.mal_id}>
              <div className="animeMain">
                <div className="animeLeft">
                  <h3 className="animeTitle">
                    {jp ? animeObj.japanese_title : animeObj.title}
                  </h3>
                  <h3>{animeObj.mal_id}</h3>
                  <button
                    className="addremButton"
                    onClick={() => removeAnime(animeObj.mal_id)}
                  >
                    Remove
                  </button>
                </div>
                <img src={animeObj.image} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default Watchlist;
