#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

// Step 2: Construct the URL for the SWAPI /films/{id} endpoint
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

// Step 3: Use the request module to fetch the movie data from the SWAPI
request(movieUrl, function(error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);

  // Step 4: Extract the list of characters from the movie data
  const characterUrls = movieData.characters;

  // Step 5: Use the request module to fetch the data for each character in the list
  characterUrls.forEach(function(characterUrl) {
    request(characterUrl, function(error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);

      // Step 6: Extract the name of each character and print it to the console
      console.log(characterData.name);
    });
  });
});

