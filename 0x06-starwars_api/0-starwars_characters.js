#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

request('https://swapi-api.hbtn.io/api/films/' + movieId, function (err, res, body) {
  if (err) {
    console.error('Error fetching movie:', err);
    return;
  }

  const data = JSON.parse(body);
  
  if (res.statusCode !== 200 || !data.characters) {
    console.error(`Movie with ID ${movieId} not found.`);
    return;
  }

  const actors = data.characters;
  exactOrder(actors, 0);
});

const exactOrder = (actors, x) => {
  if (x === actors.length) return;

  request(actors[x], function (err, res, body) {
    if (err) {
      console.error('Error fetching character:', err);
      return;
    }

    console.log(JSON.parse(body).name);

    exactOrder(actors, x + 1);
  });
};
