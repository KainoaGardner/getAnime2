import API_URL from "./Env.jsx";
import { useState, useEffect } from "react";
import CheckToken from "./Auth.jsx";
import Watchlist from "./Watchlist.jsx";
import Season from "./Season.jsx";
import Airing from "./Airing.jsx";

function Lists({ setPage, handleError }) {
  const [list, setList] = useState("airing"); //airing watchlist season
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [jpTitles, setJpTitles] = useState(false);
  const [sort, setSort] = useState("id_a"); //id_d id_a name_d name_a

  useEffect(() => {
    if (!CheckToken()) {
      setPage("login");
      handleError("You must be logged in");
      return;
    } else {
      setToken(localStorage.getItem("token"));
      getSettings();
    }
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

  const addAnime = async (mal_id) => {
    const idList = [];
    idList.push(Number(mal_id));
    const body = {
      entries: idList,
    };

    try {
      const response = await fetch("http://" + API_URL + "entries/add", {
        method: "POST",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Authorization: `Bearer ${token}`,
        },

        body: JSON.stringify(body),
      });

      const data = await response.json();
      if (response.ok) {
        if (data.length > 0) {
          handleError(data[0].title + " added to watchlist");
        } else {
          handleError("Already in watchlist");
        }
      } else {
        console.log(data);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const removeAnime = async (mal_id) => {
    const idList = [];
    idList.push(Number(mal_id));
    const body = {
      entries: idList,
    };

    try {
      const response = await fetch("http://" + API_URL + "entries/remove", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          Authorization: `Bearer ${token}`,
        },

        body: JSON.stringify(body),
      });

      const data = await response.json();
      if (response.ok) {
        console.log(data);
        handleError(data[0].title + " removed from watchlist");
      } else {
        console.log(data);
      }
    } catch (error) {
      console.log(error);
    }
  };

  const handleAddAnime = (event) => {
    const formData = new FormData(event.currentTarget);
    event.preventDefault();
    const mal_id = formData.get("mal_id");
    event.currentTarget.reset();
    addAnime(mal_id);
  };

  const handleRemoveAnime = (event) => {
    const formData = new FormData(event.currentTarget);
    event.preventDefault();
    const mal_id = formData.get("mal_id");
    event.currentTarget.reset();
    removeAnime(mal_id);
  };

  function idACompare(a, b) {
    if (Number(a.mal_id) < Number(b.mal_id)) {
      return -1;
    }
    if (Number(a.mal_id) > Number(b.mal_id)) {
      return 1;
    }
    return 0;
  }

  function idDCompare(a, b) {
    if (Number(a.mal_id) < Number(b.mal_id)) {
      return 1;
    }
    if (Number(a.mal_id) > Number(b.mal_id)) {
      return -1;
    }
    return 0;
  }

  function titleDCompare(a, b) {
    if (a.title < b.title) {
      return 1;
    }
    if (a.mal_id > b.mal_id) {
      return -1;
    }
    return 0;
  }

  function titleACompare(a, b) {
    if (a.title < b.title) {
      return -1;
    }
    if (a.title > b.title) {
      return 1;
    }
    return 0;
  }

  const sortAnime = (list) => {
    switch (sort) {
      case "id_a":
        return list.sort(idACompare);
      case "id_d":
        return list.sort(idDCompare);
      case "title_a":
        return list.sort(titleACompare);
      case "title_d":
        return list.sort(titleDCompare);
      default:
        return list.sort(idACompare);
    }
    return [];
  };

  return (
    <>
      <div className="mainBody">
        <div className="listBody">
          <button
            className={list === "airing" ? "navButton selected" : "navButton"}
            onClick={() => setList("airing")}
          >
            Your Airing
          </button>
          <button
            className={
              list === "watchlist" ? "navButton selected" : "navButton"
            }
            onClick={() => setList("watchlist")}
          >
            Your Watchlist
          </button>
          <button
            className={list === "season" ? "navButton selected" : "navButton"}
            onClick={() => setList("season")}
          >
            Season
          </button>
        </div>
        <div className="inputBody">
          <div className="addremBody">
            <div className="addremMain">
              <h2>Add Anime</h2>
              <form className="" onSubmit={handleAddAnime}>
                <input type="number" name="mal_id" placeholder="Mal Id" />
                <button className="submit" type="submit">
                  Add
                </button>
              </form>
            </div>

            <div className="addremMain">
              <h2>Remove Anime</h2>
              <form onSubmit={handleRemoveAnime}>
                <input type="number" name="mal_id" placeholder="Mal Id" />
                <button className="submit" type="submit">
                  Remove
                </button>
              </form>
            </div>
          </div>
        </div>

        <div className="sort">
          <button
            className={sort === "id_a" ? "navButton selected" : "navButton"}
            onClick={() => setSort("id_a")}
          >
            Ascending Id
          </button>
          <button
            className={sort === "id_d" ? "navButton selected" : "navButton"}
            onClick={() => setSort("id_d")}
          >
            Descending Id
          </button>
          <button
            className={sort === "title_a" ? "navButton selected" : "navButton"}
            onClick={() => setSort("title_a")}
          >
            Ascending Name
          </button>
          <button
            className={sort === "title_d" ? "navButton selected" : "navButton"}
            onClick={() => setSort("title_d")}
          >
            Descending Name
          </button>
        </div>
      </div>

      <ListType
        list={list}
        token={token}
        handleError={(err) => handleError(err)}
        addAnime={(mal_id) => addAnime(mal_id)}
        removeAnime={(mal_id) => removeAnime(mal_id)}
        jpTitles={jpTitles}
        sort={sort}
        sortAnime={(list) => sortAnime(list)}
      />
    </>
  );
}

function ListType({
  list,
  token,
  handleError,
  addAnime,
  removeAnime,
  jpTitles,
  sort,
  sortAnime,
}) {
  switch (list) {
    case "watchlist": {
      return (
        <Watchlist
          token={token}
          handleError={(err) => handleError(err)}
          removeAnime={(mal_id) => removeAnime(mal_id)}
          jp={jpTitles}
          sort={sort}
          sortAnime={(list) => sortAnime(list)}
        />
      );
    }
    case "season": {
      return (
        <Season
          token={token}
          handleError={(err) => handleError(err)}
          addAnime={(mal_id) => addAnime(mal_id)}
          jp={jpTitles}
          sort={sort}
          sortAnime={(list) => sortAnime(list)}
        />
      );
    }
    default: {
      return (
        <Airing
          token={token}
          handleError={(err) => handleError(err)}
          removeAnime={(mal_id) => removeAnime(mal_id)}
          jp={jpTitles}
          sort={sort}
          sortAnime={(list) => sortAnime(list)}
        />
      );
    }
  }
}

export default Lists;
