# propose

## Collaborators
* [Chris Ball](https://github.com/chrisba11)
* [Paul Williamsen](https://github.com/paulwilliamsen)
* [Milo Anderson](https://github.com/TheMiloAnderson)

## Purpose
This project is the brain child of Chris, who is coming from a background in cabinetry and worked for many shops that struggle to have a firm grasp on pricing for their products. During his tenure at his most recent employer, he was tasked with developing a pricing tool that made proposals much easier and faster for designers to produce. Since Excel was the only reasonable tool he was familiar with, he built that pricing tool using Excel. He has been dreaming of producing a web application for cabinet shops that would serve the same purpose and much more, but without the limitations of Excel. This project is essentially our attempt to provide a proof of concept for that dream.

## Features
* Create & modify Accounts, Materials & Hardware lists
* Specify labor costs per Project & per finish style (stretch goal)
* Create & modify Projects within an Account, and Specifications & Rooms within a Project
* Cabinets are created & managed with relationships to Specifications and Rooms: Specifications define material & construction options; Rooms are (at present) mostly a way to group & organize cabinets
* Create multiple drawers, associated with a Cabinet
* User can view a detailed invoice of project costs

## Getting Started Locally
After cloning the repo, you'll need to create an .env file. The file ".env_example" is included in this repo to show the values this app needs to run. You can easily get a Django secret key from one of many online generators. The email settings are only necessary if you want to demonstrate the new user email registration functionality. 

To run the project locally, navigate into the web/ folder (the docker-compose.yml in the root directory is intended for live deployment). Next, run `docker-compose up --build` in your terminal to download all the dependencies and start the containers.

When this is done, you might want to create a superuser for Django admin purposes. Run `docker-compose exec web bash` to shell into the container, then `./manage.py createsuperuser` and follow the prompts.

Hopefully that all worked, and you can now view the project at http://localhost:8000. It won't look like much until it has some data; luckily we've made a script to handle that for you.

Run `docker-compose exec web bash` to shell into the container if you aren't already there, then run `./manage.py dummy_data`. This will delete any data in the DB, then re-populate it with a variety of Accounts, Projects, Cabinets, Specifications, etc.

## Tools Used
* Django
* django-registration & django-sass-processor
* factory-boy for testing setup
* Postgresql via Psycopg
* Docker

## Project Organization
[Entity-Relationship Diagram](https://dbdiagram.io/d/5cc20c1bf7c5bb70c72fc2b1)
