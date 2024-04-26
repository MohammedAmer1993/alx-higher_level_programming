-- select cities and states 
SELECT id, cities.name, states.name FROM cities
INNER JOIN states
ON cities.state_id = state.id;
