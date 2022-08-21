# Project_Fetch_Metadata_Team_83
# [MetaTrack](metatrack_logo.svg)<br>

Metatrack is a project executed by team 83 in the 2022 cohort of Zuri's training..

## TABLE OF CONTENTS

- [What is Metatrack?](#what-is-meta-track)
- [Is it necessary?](#is-it-necessary)
- [Tech Stack](#tech-stack)
- [Features](#how-will-it-benefit-you)
- [Special Links](#special-links)
- [How to test the app on your local machine](#run-the-app-in-your-local-machine)


### What is Metatrack

Metatrack is a Web Application for saving digital files and extracting  Metadata of those files.
You also have an option to save, export, download, share and embed in your own website.

To learn more about metadata and metatrack, [read our documentation](metatrack.herokuapp.com/documentation)

### Is it necessary

In a world where most people see only the contents of digital files, we provide a way for a you to see the data behind the content... even without opening it.<br>
If you are a Photographer, Journalist, Lawyer, NFT and Web 3 enthusiast, programmer, or any metadata cruncher, some times you need to know the metadata behind your digital file... 'and that, my friend, is where we come in'.


### Tech Stack

This project was designed with [Figma and Figjam](https://www.figma.com/file/KyMXrf2whjJerytHr8occj/Meta-Data-Website?node-id=127%3A1494), and built with HTML, CSS, django and postgresql database.


### How will it benefit you
The metatrack project has some amazing feature of immense benefit and they include:



#### Upload files and generate metadata:
We give you the ability to upload and generate metadata for your particular file type with just a click.

#### Download files:
 You can also download the  generated metadata in a `.mttrck` digital format and read it with any text  editor of your choice.


#### Save files:
Upon uploading your digital file, the file is forever safely stored in the Metatrack cloud for you until when you decide to get rid of it.

#### Website embed:
Programmers can easily embed generated metadata into a website’s code.

## Special Links

#### [Project Documentation]().

####  [Database Schema Diagram](https://www.figma.com/file/fIeIf2BakTUAXfUTv9EFnx/Team-83-DATABASE-SCHEMA?node-id=0%3A1).

#### See our [design on Figma](https://www.figma.com/file/KyMXrf2whjJerytHr8occj/Meta-Data-Website?node-id=127%3A1494)

### Run the app in your local machine
#### pre-requisites
These are some of the apps that should be installed in your local machine for a seamless flow.

  1. Postgresql database
  2. Redis
  3. Exiftool
  4. Python 3.8 - 3.10
#### How to set it up
  1. Clone the repository `git clone https://github.com/zuri-training/proj_fetch_meta_data_team_83/`

  2. configure the project for local machine

   - Create a virtual environment and activate `python -m venv env`
   - Install the python dependencies using `pip install -r requirements.txt`
   - `cd into fetch_metadata`

  3. Configure your database:
 We have hard-coded the database variables into the settings.py, that means you need to create your database in postgresql.
 If you are new to postgresql, follow these steps to install
##### On windows
    1. Go to [postgresql website](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and download postgresql database version 13.7 for uniformity
    2. Install with adminstrator priviledges and set your superuser password
    3. open pgAdmin 4<br><br> ![pgAdmin](pgAdmin1.gif)<br><br>
      - click server, and right click you PostgreSQL version
     - create new database and input your superuser password
  4. Create a `.env` file and type the following <br>
   `PG_DB = '<database_name>'` <br>
   `PG_USER = '<postgres_user>'` <br>
   `PG_PASSWORD = "<your_password>"` <br>
   `PG_HOST = "127.0.0.1"` <br>
   `PG_PORT = "<port_number>"` <br>
   replace database*name, postgres_user, your_password and port_number with the database name you created, postgres user , your password and your portnumber.
   \_The postgres-user is usually* `postgres` _and The port number is usually_ `5432` _unless you changed it_
  5. install the requirements.txt

  6. Open a new terminal and start a redis server using `redis-server`.

  7. Start celery using `python -m celery fetch_metadata worker`

  8. Runserver using `python manage.py runserver`
##### On linux


Any issues? please create an issue.

### Contribute
Contributiins are welcome.
To contribute, simply fork the repository,
update your code and create a pull request.

### License
=======


