-- All shows to be selected
SELECT hbtn_0d_tvshows.tv_shows.title,
hbtn_0d_tvshows.tv_show_genres.genre_id FROM hbtn_0d_tvshows.tv_shows
NATURAL JOIN hbtn_0d_tvshows.tv_show_genres ORDER BY hbtn_0d_tvshows.tv_show_genres.genre_id ASC, hbtn_0d_tvshows.tv_shows.title ASC;
