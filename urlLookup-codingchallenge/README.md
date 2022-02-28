# Exercise URL Lookup
A web service written in Go, that responds to GET requests to find if a URL is safe to browse or not

# Coding Exercise
For this exercise, we would like to see how you go about solving a rather straightforward coding challenge and 
architect-ing for the future. One of our key values in how we develop new systems is to start with very simple
implementations and progressively make them more capable, scalable and reliable. And releasing them each step of 
the way. As you work through this exercise it would be good to "release" frequent updates by pushing updates to a shared 
git repo (we like to use Bitbucket's free private repos for this, but gitlab or github also work). It's up to you how 
frequently you do this and what you decide to include in each push. Don't forget some unit tests 
(at least something representative).

**_Here's what we would like you to build:_**
### URL lookup service
We have an HTTP proxy that is scanning traffic looking for malware URLs. Before allowing HTTP connections to be made, 
this proxy asks a service that maintains several databases of malware URLs if the resource being requested is known to 
contain malware.

Write a small web service, in the language/framework your choice, that responds to GET requests where the caller passes 
in a URL and the service responds with some information about that URL. The GET requests look like this:
```GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}```

The caller wants to know if it is safe to access that URL or not. As the implementer, you get to choose the response 
format and structure. These lookups are blocking users from accessing the URL until the caller receives a response 
from your service. Give some thought to the following:
1. The size of the URL list could grow infinitely, how might you scale this beyond the memory capacity of this VM? 
Bonus if you implement this.
2. The number of requests may exceed the capacity of this VM, how might you solve that? Bonus if you implement this.
3. What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand 
URLs a day with updates arriving every 10 minutes.
4. Bonus points if you containerize the app. Email us your ideas.

# Test the environment 
The exercise was written/tested entirely on MacOS and thus the following instructions assume a similar environment
 where docker engine is fully supported.
 
Before proceeding, the URL lookup service architecture is explained bellow: 
```
+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                   |
|                                                                                                                                                   |
|                       +--------+          +-------------------------+      +-------------------------+        +------+      +----------+          |
|                       |        |          |                         |      |      REDIS CLUSTER      |        |      |      |          |          |
|          +----------->+        |          |        +-------------+  |      |      +-----------+      |        |      +<-----+  FOLDER  |          |
|          |            |        |          |        |             |  |      |      |           |      |        |  U   |      |  MOUNTS  |          |
|          |   +------->+   N    |          |   +--->+  LOOKUP     <-------->+      |  REDIS1   |      |        |      |      +----------+          |
|          |   |        |        |          |   |    |  APP-1      |  |      |      |           |      |        |  P   |                            |
| +--------+-+ |   +--->+   G    |      +---+---+-+  |             |  |      |      +-----------+      |        |      |                            |
| |          | |   |    |        |      |         |  +-------------+  |      |      +-----------+      |        |  D   |                            |
| | CLIENTS  +-+-+ |    |   I    |      | LOOKUP  |                   |      |      |           |      |        |      |      +----------+          |
| |          |   | |    |        +<---->+ SERVICE |  +-------------+  |      |      |  REDIS2   |      <--------+  A   |      |          |          |
| +--+-------+   +-++   |   N    |      |         |  |             |  |      |      |           |      |        |      |      |  LIVE    |          |
|    |           |  |   |        |      +---+---+-+  |  LOOKUP     <-------->+      +-----------+      |        |  T   |      |  UPDATES |          |
|    +--+--------+  |   |   X    |          |   |    |  APP-2      |  |      |           ...           |        |      |      |          |          |
|       |           |   |        |          |   +--->+             |  |      |      +-----------+      |        |  E   +<-----+  POST    |          |
|       +-----------+   |Load    |          |        +-------------+  |      |      |           |      |        |      |      |   /      |          |
|                       |Balancer|          |                         |      |      |  REDISN   |      |        |  R   |      |  RSS     |          |
|                       |        |          |                 ...     |      |      |           |      |        |      |      |          |          |
|                       |        |          |                         |      |      +-----------+      |        |      |      |          |          |
|                       +--------+          +-------------------------+      +-------------------------+        +------+      +----------+          |
|                                                                                                                                                   |
|                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

```  

To address 2. from the requirements we added an nginx load balancer in front of the lookup service to manage the
increasing load of requests and response. New nodes will be able to be spun up or we can use the
scaling options of docker swarm to provide with more servicing apps. 
  
To address 1. the data store was implemented with a redis cluster of 1 masters and 2 slaves total so that we can
provide HA for the data. To support the infinite grow of blacklisted URLs we need to have
support for data persistence into a physical media. The choice of Redis was made since it supports persistence. It
also supports minimal footprint as the keys can be saved in-memory for faster lookups where as the data can be
stored into a physical media. Redis will save data on disk periodically so in case of a crash we would have the data
available to one of the other two redis instances. Another point worth mentioning is that redis provides with both HA
and Sharding, so if we have a need in the future to scale both Writes and Reads, those functionalities are
orthogonal and can be combined. 

To address 3. our solution provides initial load of blacklisted url from the "Updater" service. Essentially there is 
a loop that checks every 10-minutes for news files under a mounted in the container folder. A future implementation
would be to have a system feeding the uploader with URLs in real time. For this to be implemented minor changes would 
have to take place in the code as the loop is already in place. There is also already implemented support for POST 
requests in the lookup service to manually add new URLs for quick testing. 
 
_**NOTE #1**_: The url data returned is very simplistic in the first iteration as it only returns if a website is
 safe or
not. There is a lot of room for further improvements by adding for example creation/updates timestamps. The service
would be able to perform clean-ups for outdated URLs or if URLs are not valid any more after a time interval. 
   
_**NOTE #2**_ There were no changes in the incoming format of the GET request, but there is room for improvements on the 
parsing of the URL by adding additional validation checks according to the RFC, as well as adding more metadata (i.e timestamps of request) 

## 1. Build the images
To build the images needed to run the exercise, browse into the docker folder and issue: 
```bash
$ git clone https://github.com/brecode/urlLookup.git
$ cd urllookup/docker
$ docker-compose build
```

When done you should be able to see the following images when executing: 
```bash
$ docker images
REPOSITORY     TAG       IMAGE ID            CREATED            SIZE
updater       latest   1d8e8dbb1bab        16 minutes ago      9.14MB
webapp        latest   ee7a3c89d4d1        20 minutes ago      9.84MB

```

The rest of the images will automatically be downloaded. 

## 2. Initialize a Docker Swarm 
For the deployment of our service we are going to need a docker swarm. To initialize a new docker swarm execute:
```bash
$ docker swarm init
```

You should be able to see something similar to the following: 
```bash
Swarm initialized: current node (f744cqd9un1d5vap95v95lb2f) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-37elfm07sz08683kvs8hhiwoneto1x7z43amhgliglvndmna0i-ccfhdttfvl224xazmtwqelvsc 192.168.65.3:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

You are now ready to deploy the URL lookup service. Just run: 
```bash 
docker stack deploy --compose-file docker-compose.yaml urllookup
```

To check if a website is legit you can browse into the blacklist folder, pick a URL and query from the browser like so:
```bash
$ http://0.0.0.0/urlinfo/1/dl.downf468.com/n/3.0.26.3/4789537/setup.exe
```

or from a terminal
```bash
$    curl -vv -X GET http://0.0.0.0/urlinfo/1/dl.downf468.com/n/3.0.26.3/4789537/setup.exe
```

