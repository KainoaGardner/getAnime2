import API_URL from "./Env.jsx";
import { useState, useEffect } from "react";

function Airing({ handleError, removeAnime, token, jp, sort, sortAnime }) {
  const [airing, setAiring] = useState([]);
  useEffect(() => {
    getAiring();
  }, [removeAnime, sort]);

  const getAiring = async () => {
    try {
      const response = await fetch(
        "http://" + API_URL + "entries/watchlist/airing",
        {
          method: "GET",
          headers: { Authorization: `Bearer ${token}` },
        },
      );

      const data = await response.json();
      if (response.ok) {
        setAiring(sortAnime(data));
      } else {
        handleError(data.detail);
      }
    } catch (error) {
      console.log(error);
    }
  };

  if (airing.length === 0) {
    return (
      <>
        <div>
          <h1>Airing Today</h1>
          <h2>Nothing Airing today</h2>
        </div>
      </>
    );
  }

  return (
    <>
      <div>
        <h1>Airing Today</h1>
        <div>
          {airing.map((animeObj) => (
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

export default Airing;
