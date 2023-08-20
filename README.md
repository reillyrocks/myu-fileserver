# myu
TODOS:
- Look into traefik, at a glance I think I like it more than nginx.
- Honestly security... is challenging. I want to go to the great wide web... 
But I think this will be a pet project running in my local network. My appreciation for security engineers is now very high. 
I will probably put it on my raspberry pi at some point.

### What I have learned (also a reminder to me not to repeat mistakes)
- CORS was not the issue... soo  I do not want to expose my fastapi app to the world!!
I want to keep it in the Docker network, only exposing a front end (an area i am unfamiliar with). So
I built a front end that was html and js to do a fetch request to my api.... I thought it was a CORS issue,
when it was not working. It is simple: **the user is *NOT* part of the docker network**. I had to hammer this 
into my head a few times. 
The users **browser loads**, and runs the html/javascript... not the front end apache landing page :facepalm:
- The front end will need to be a full app, not some javascript. It will need its own "backend" of sorts that
will interact with the fastapi. I wonder if i could do a swagger page. 


### I like sustainability, and scalability.
**Sustainable** means readable, simple, maintainable to me
**Scalability** means flexibility, modularity, and really enables microservices. 

---

### docker container 1 (dc1): reverse proxy
`nginx` reverse proxy, points to the api. Doesn't do load balancing (yet?) or anything, just there for security

### docker container 2 (dc2): api
`poetry` for the package manager, best with dependency management. 

`fastapi` app. High performance is not important for me... I genuinely like the framework. It is intuitive, very pythonic, and its integration 
with pydantic and other services (like `openapi` code gen (swagger)) are big sells. `Flask` has become messy imo. Too
many ways to do one thing, a reason why `go` is cool to me.

### docker container 3 (dc3): db
Honestly. I do not know if I need a db. I think a file system set up is sufficient.  
I like `sql`.... but for this project `noSQL` would be preferred.


# Running
create creds files: `.htpasswd`

`htpasswd -c .htpasswd <username>`

`docker compose up`
it will be running at localhost (use password from above)