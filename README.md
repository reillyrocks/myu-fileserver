# myu

### What I want to do.
- `my-repo/server/setup` file is desired and loved. Needs to be converted to Ansible 
- Add [Authelia](https://www.authelia.com/) to layer [nextcloud](https://nextcloud.com/) with proper security.
- Add front end.... test out bard/chatgpt - may be better than random thrown together junk. **


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