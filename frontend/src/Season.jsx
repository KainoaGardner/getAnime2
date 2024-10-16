import API_URL from "./Env.jsx";
import { useState, useEffect } from "react";

function Season({ handleError, addAnime, jp, sort, sortAnime }) {
  const [season, setSeason] = useState([]);
  useEffect(() => {
    getSeason();
  }, [sort]);

  const getSeason = async () => {
    try {
      const response = await fetch("http://" + API_URL + "lists/season", {
        method: "GET",
      });

      const data = await response.json();
      if (response.ok) {
        const seasonList = [];
        for (const animeId in data) {
          const animeObj = {
            mal_id: animeId,
            title: data[animeId].title,
            japanese_title: data[animeId].japanese_title,
            image: data[animeId].image,
          };
          seasonList.push(animeObj);
        }
        setSeason(sortAnime(seasonList));
      } else {
        handleError(data.detail);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      <div>
        <h1>Season</h1>
        {season.map((animeObj) => (
          <div className="mainBody" key={animeObj.mal_id}>
            <div className="animeMain">
              <div className="animeLeft">
                <h3 className="animeTitle">
                  {jp ? animeObj.japanese_title : animeObj.title}
                </h3>
                <h3>{animeObj.mal_id}</h3>
                <button
                  className="addremButton"
                  onClick={() => addAnime(animeObj.mal_id)}
                >
                  Add
                </button>
              </div>

              <img src={animeObj.image} />
            </div>
          </div>
        ))}
      </div>
    </>
  );
}

export default Season;
