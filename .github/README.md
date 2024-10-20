<h1 align="left">Seasonal Anime Episode Watchlist and Daily Airing Web Scaper</h1>
<https://ganime.kainoagardner.xyz/>
<img src="ganime.png"
     alt="Image"
     style="float: left; margin-right: 10px; height: 500px" />

Anime Ids are based of MAL API
<https://myanimelist.net>

Anime Episode Schedule scraper from LiveChart
<[https://myanimelist.net](https://www.livechart.me/schedule)>

<h2>Terminal Commands</h2>
<h3>User Settings</h3>

#### Options 
>
> - li [username] [password] //login 
> - lo //logout
> - r [username] [password] //register


<h3>List Anime -l</h3>

#### Options 
>
> - today, t  //user's today airing
> - watchlist wl  //user's watchlist
> - all a //seasonal list

<h3>Example</h3>

```shell
foo@bar: getAnime -l t
---Watchlist Airing Today---
1 ID: 21 One Piece
2 ID: 235 Meitantei Conan
```

<h3>Add Delete Clear</h3>
<p>Use Mal Id to add and delete anime</p>

#### Options 
>
> - a [Id] //add anime to watchlist
> - d [Id]  //delete anime from watchlist
> - c //clear entire watchlist

<h3>Example</h3>

```shell
foo@bar: getAnime -a 21
---Adding---
1 ID: 21 One Piece
```

```shell
foo@bar: getAnime -d 21
---Deleting---
1 ID: 21 One Piece
```




