# 0x03. Queuing System in JS

![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/1486e02a78cdf7b4557c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230523%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230523T093354Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b6cf428d1ade446a259c20c0f2c5d2c3b61aa945c9d5b09ae8eda8051dbcd268)

## Resources

**Read or watch**:

- [Redis quick start](https://intranet.alxswe.com/rltoken/8xeApIhnxgFZkgn54BiIeA)
- [Redis client interface](https://intranet.alxswe.com/rltoken/1rq3ral-3C5O1t67dbGcWg)
- [Redis client for Node JS](https://intranet.alxswe.com/rltoken/mRftfl67BrNvl-RM5JQfUA)
- [Kue](https://intranet.alxswe.com/rltoken/yTC3Ci2IV2US24xJsBfMgQ) *deprecated but still use in the industry*

## Tasks

### 0. Install a redis instance

Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - [https://redis.io/download/](https://intranet.alxswe.com/rltoken/v6VB9ZwmVfppL0OmzbmVWQ)):

```sh
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
```

- Start Redis in the background with `src/redis-server`

```sh
src/redis-server &
```

- Make sure that the server is working with a ping `src/redis-cli ping`

```sh
PONG
```

- Using the Redis client again, set the value `School` for the key `Holberton`

```sh
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```

- Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)

```sh
kill [PID_OF_Redis_Server]
```

Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

Requirements:

- Running `get Holberton` in the client, should return `School`

### 1. Node Redis client

Install [node_redis](https://intranet.alxswe.com/rltoken/mRftfl67BrNvl-RM5JQfUA) using npm

Using Babel and ES6, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:

- It should log to the console the message `Redis client connected to the server` when the connection to Redis works correctly
- It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work

Requirements:

- To import the library, you need to use the keyword `import`

### 2. Node Redis client and basic operations

In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).

Add two functions:

- `setNewSchool`:
  - It accepts two arguments `schoolName`, and `value`.
  - It should set in Redis the value for the key `schoolName`
  - It should display a confirmation message using `redis.print`
- `displaySchoolValue`:
  - It accepts one argument `schoolName`.
  - It should log to the console the value for the key passed as argument

At the end of the file, call:

- `displaySchoolValue('Holberton');`
- `setNewSchool('HolbertonSanFrancisco', '100');`
- `displaySchoolValue('HolbertonSanFrancisco');`

Requirements:

- Use callbacks for any of the operation, we will look at async operations later

### 3. Node Redis client and async operations

In a file `2-redis_op_async.js`, let’s copy the code from the previous exercise (`1-redis_op.js`)

Using `promisify`, modify the function `displaySchoolValue` to use ES6 `async / await`

Same result as `1-redis_op.js`

### 4. Node Redis client and advanced operations

In a file named `4-redis_advanced_op.js`, let’s use the client to store a hash value
Create Hash:

Using `hset`, let’s store the following:

- The key of the hash should be `HolbertonSchools`
- It should have a value for:
  - `Portland=50`
  - `Seattle=80`
  - `New York=20`
  - `Bogota=20`
  - `Cali=40`
  - `Paris=2`
- Make sure you use `redis.print` for each `hset`

Display Hash:

Using `hgetall`, display the object stored in Redis. It should return the following:

Requirements:

- Use callbacks for any of the operation, we will look at async operations later
