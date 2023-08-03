# myu
TODOS:
- Honestly security, and website networking... is challenging.
worried this will be a pet project running at localhost.

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

My Sustain and Scale -ability (SnS) senses are telling me, 3 containers for this fileserver backend 
is the right approach. <sub> (I could be wrong, please tell me - i need to learn!) </sub>
---

### docker container 1 (dc1): reverse proxy
`nginx` reverse proxy, points to the api. Doesn't do load balancing (yet?) or anything, just there for security

### docker container 2 (dc2): api
`poetry` for the package manager, best with dependency management. 

`fastapi` app. High performance is not important for me... I genuinely like the framework. It is intuitive, very pythonic, and its integration 
with pydantic and other services (like `openapi` code gen (swagger)) are big sells. `Flask` has become messy imo. Too
many ways to do one thing, a reason why `go` is cool too.

### docker container 3 (dc3): db
I like `sql`.... but I also don't (sorry!!). For a personal project `noSQL` stuff is brainless, fast and preferred.
Since it is a different container I could change it some day if I am going to scale up (but probably not. no one likes tech debt LOL)

I am not sure what I will use**, but something simple like `MongoDB` for what will be only like 3 tables. Honestly the filesystem, or dicts
might be good enough. :shrug:

# Running
create creds files: `.htpasswd`

`htpasswd -c .htpasswd <username>`

`docker compose up`
it will be running at localhost (use password from above)