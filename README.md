# proj_fetch_meta_data_team_83

This is Team_83 Project Repository 

## Team 83 Project >> Fetch_Metadata <br>

### MetaTrack :: Metadata extractor platform

[MetaTrack](metaTrack.PNG) 
<br>

# METATRACK 
A platform that collects and displays metadata of uploaded file.The web application allow users to  extract metadata from file uploaded, then export, save, download and share if the user decides to. 

## Table of Content
* [General Overview of project](#General-Overview-of-project)
* [Technologies/framework](#Technologies/framework)
* [Features](#Features)
* [How to Make Use of MetaTrack](#How-to-Make-Use-of-The-MetaTrack)
* <details>
<summary> Contribute [How to Set Up and Run the Project](#)</summary>
   - Create a pull request
   - Configure the project for local machine
   - Configure your database
</details><br>

* [Project Requirements and Dependencies](#Project-Requirements-and-Dependencies)
* [Authors/Contributors](#Authors/Contributors)


### Checkout the Design [here](https://www.figma.com/file/KyMXrf2whjJerytHr8occj/Meta-Data-Website?node-id=127%3A1494)<br>

### See the database schema [here](https://www.figma.com/file/fIeIf2BakTUAXfUTv9EFnx/Team-83-DATABASE-SCHEMA?node-id=0%3A1)<br>


## General Overview of project
What are metadata? Metadata are information that is not readily apparent from the face of an electronic document. Metadata are data that provides information about other data but not the content of the data, such as the text of a message or the image itself. 
 They provide information about one or more aspects of the data; it is used to summarize basic information about data that can make tracking and working with specific data easier. It contains information needed to understand and effectively use the data. However, its significance becomes apparent as we consider its functional use.

In this project, we created a platform MetaTrack, MetaTrack is a platform  where users can fetch metadata from a file uploaded,then they can export, save, download and share if the user decides to.  
*MetaTrack provides useful information/data to user about their files
*MetaTrack allows user to save their files for future references.



## Technologies/framework used <br>
- Designers 
   - figma
   - 
- Developers
   - HTML
   - CSS
   - Javascript
   - Python
   - Django
   - Django rest framework


   ## Features of project
- User unathenticated
   - Visit the platform to view basic information about it
   - View and Interact with the documentation
   - Register to view more details
   - No access to use until registered

   <br>
- User Authenticated
   - Full access to the platform
   - Allow users upload files (image, csv, pdf and json)
   - Generate / Fetch metadata of the files uploaded
   - Display meta data to users
   - Allow export, download, share and website embed
   - Allow user save data and come back to download



## How to Make Use of MetaTrack
- A user visit the platform, MetaTrack
- A user can read more on what MetaTrack is all about
- A user can use the website with ease and not getting lost (good usability)



- A user signup to register on the platform
- User login to have access to the features of MetaTrack
- User can upload files(csv, image, pdf,json, video files), and save on the platform.
- User can view a list of all saved files.
- User can extract file metadata.
- User can view preferred files and its metadata.
- user can save extracted metadata
- User  can check/see security implications of uploaded files
 



## Contribute >> How to Set Up and Run the Project locally

### Create a pull request

1. clone the repo using `git clone https://github.com/zuri-training/proj_fetch_meta_data_team_83/`

2. open your terminal and cd into team_83 using `cd proj_fetch_meta_data_team_83`

3. create a new branch with your username using `git checkout -b <your-username>`
   _please replace your-username with the user name you are using on slack_

4. Then add it to the repository using `git remote add upstream https://github.com/zuri-training/proj_fetch_meta_data_team_83`

5. create a `.env` file and add it to your `.gitignore` file

6. push it back to github using `git push -u origin <your-username>`

## Project Requirements and Dependencies
- Configure the project for local machine

1. Create a virtual environment and activate `python -m venv env`
   - To activate in windows powershell `env\Scripts\activate.ps1`
   - To activate in command prompt (cmd) `env\Scripts\activate`
   - To activate in bash `source env/Scripts/activate`
     NB: If you use any other name to replace "env" above, add it to your .gitignore file
2. upgrade pip using `pip install --upgrade pip`
3. install the dependencies using `pip install -r requirements.txt`
4. cd into the project folder `cd fetch_metadata`

- Configure your database

1. Go to [postgresql website](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and download postgresql database version 13.7 for uniformity
2. Install with adminstrator priviledges and set your superuser password
3. open pgAdmin 4<br><br> ![pgAdmin](pgAdmin1.gif)<br><br>
   - click server, and right click you PostgreSQL version
   - create new database and input your superuser password
4. Type the following in your `.env` file <br>
   `PG_DB = '<database_name>'` <br>
   `PG_USER = '<postgres_user>'` <br>
   `PG_PASSWORD = "<your_password>"` <br>
   `PG_HOST = "127.0.0.1"` <br>
   `PG_PORT = "<port_number>"` <br>
   replace database*name, postgres_user, your_password and port_number with the database name you created, postgres user , your password and your portnumber.
   \_The postgres-user is usually* `postgres` _and The port number is usually_ `5432` _unless you changed it_
5. run `python manage.py runserver`

Any errors? [beep me](https://wa.link/y15x4c)





### Read more on project [here] ()

<br>
# Credits

[Ingressive for Good + Zuri Training](https://training.zuri.team/)

## Authors
[@thobiy](https://github.com/Thobiy) <br>
[@]()

## Contributors
<details>
<summary>Developers</summary>
<br>

[@Idimmusix](https://github.com/Idimmusix) <br>
[@dariemjnr](https://github.com/dariemjnr) <br>
[@Chisquare7](https://github.com/Chisquare7) <br>
[@onwuachumba](https://github.com/onwuachumba) <br>
[@Thobiy](https://github.com/Thobiy) <br>
[@Omowumiishola](https://github.com/Omowumiishola) <br>
[@oluwatobiloba1](https://github.com/oluwatobiloba1) <br>
[@Seek-Techs](https://github.com/Seek-Techs) <br>
</details><br>

<details>
<summary>Designers</summary>
<br>

[@Amaka] <br>
[@Babygeh](https://github.com/Babygeh) <br>
[@horpehyemmy](https://github.com/horpehyemmy)  <br>
[@Dvrmvc](https://github.com/Dvrmvc) <br>
[@Tinux001](https://github.com/Tinux001) <br>
[@AdebiyiPeace](https://github.com/AdebiyiPeace) <br>

</details>


