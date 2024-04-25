-- groups of scores
USE hbtn_0c_0;
SELECT score, COUNT(score) AS number FROM second_tabe GROUP BY score;
