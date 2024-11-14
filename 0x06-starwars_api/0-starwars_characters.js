#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Check if movieId was provided
if (!movieId) {
  console.error("Usage: ./0-starwars_characters.js <Movie ID>");
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  
  // Parse the response body as JSON
  const data = JSON.parse(body);

  // Get the characters array from the response
  const characters = data.characters;

  // Fetch each character's data in order and print their names
  const fetchCharacterNames = async () => {
    for (const characterUrl of characters) {
      await new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
            resolve();
          }
        });
      });
    }
  };

  fetchCharacterNames().catch(console.error);
});

