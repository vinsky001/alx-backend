import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Event listener for errors
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Function to update a hash in Redis
const updateHash = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

// Function to print the contents of a hash in Redis
const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

// Main function
const main = () => {
  // Hash object with field-value pairs
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  // Loop through the hash object and update the Redis hash
  for (const [field, value] of Object.entries(hashObj)) {
    updateHash('HolbertonSchools', field, value);
  }

  // Print the contents of the updated Redis hash
  printHash('HolbertonSchools');
};

// Event listener for when the client is connected to the Redis server
client.on('connect', () => {
  console.log

