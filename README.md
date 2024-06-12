# myu
### WHAT IS THIS?
- a playground of ideas
- nothing organized
- fastapp is messy and should eventually be moved, but works in this mess for now
- docker network will be created and used across all the apps

### What I want to do.
- Create script to run nextcloud and set up per my desires
- Add layer [nextcloud](https://nextcloud.com/) with proper security.
- Add front end.... gonna use [claude](https://claude.ai/chats) tbh - better than random thrown together junk. **
- move this mess into its proper repos

### I like sustainability, and scalability.
**Sustainable** means readable, simple, maintainable to me
**Scalability** means flexibility, modularity, and really enables microservices. 

--- 

### front end first attempt
- first attempt at a front end was _not_ a CORS issue... soo I do not want to expose my fastapi app to the world!!
  I want to keep it in the Docker network, only exposing a front end (an area i am unfamiliar with). So
  I built a front end that was html and js to do a fetch request to my api.... I thought it was a CORS issue,
  when it was not working. It is simple: **the user that loads the web page is *NOT* part of the docker network**. 
  So obvious once i figured it out... so will have to do a backend to that OR have the api return a ui ughh
- Now going to use something else to run and connect with

### Whats the idea???
![diagram from excalidraw](/extrastuff/whatitwilllooklike.png)