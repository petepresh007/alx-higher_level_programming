-- All shows to be selected
SELECT hbtn_0d_tvshows.tv_shows.title, hbtn_0d_tvshows.tv_show_genres.genre_id
FROM hbtn_0d_tvshows.tv_shows
INNER JOIN hbtn_0d_tvshows.tv_show_genres ON hbtn_0d_tvshows.tv_shows.id = hbtn_0d_tvshows.tv_show_genres.show_id
ORDER BY hbtn_0d_tvshows.tv_shows.title ASC, hbtn_0d_tvshows.tv_show_genres.genre_id ASC;
