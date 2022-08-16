# Project_Fetch_Metadata_Team_83

# ![MetaTrack-logo](metatrack_logo.svg) Metatrack<br>

Metatrack is a project executed by team 83 in the 2022 cohort of Zuri's training..

## TABLE OF CONTENTS

- [What is Metatrack?](#what-is-meta-track)
- [Is it necessary?](#is-it-necessary)
- [Tech Stack](#tech-stack)
- [Features And Benefits](#features-and-benefits)
- [How to use Metatrack](#how-to-use-metatrack)
- [Special Links](#special-links)
- [How to test the app on your local machine](#run-the-app-in-your-local-machine)
- [Contribute](#contribute)
- [Credits](#credits)
- [license](#license)

### What is Metatrack

Metatrack is a Web Application for saving digital files and extracting Metadata of those files.
You also have an option to save, export, download, share and embed in your own website.

To learn more about metadata and metatrack, [read our documentation](metatrack.herokuapp.com/documentation)

### Is it necessary

In a world where most people see only the contents of digital files, we provide a way for a you to see the data behind the content... even without opening it.<br>
If you are a Photographer, Journalist, Lawyer, NFT and Web 3 enthusiast, programmer, or any metadata cruncher, some times you need to know the metadata behind your digital file... 'and that, my friend, is where we come in'.

### Tech Stack

This project was designed with [Figma and Figjam](https://www.figma.com/file/KyMXrf2whjJerytHr8occj/Meta-Data-Website?node-id=127%3A1494), and built with HTML, CSS, django and postgresql database.

### Features And Benefits

The metatrack project has some amazing feature of immense benefit and they include:

#### Upload files and generate metadata:

We give you the ability to upload and generate metadata for your particular file type with just a click.

#### Download files:

You can also download the generated metadata in a `.mttrck` digital format and read it with any text editor of your choice.

#### Save files:

Upon uploading your digital file, the file is forever safely stored in the Metatrack cloud for you until when you decide to get rid of it.

#### Website embed:

Programmers can easily embed generated metadata into a website’s code.

### How To Use Fetch_Metadata

1. visit the platform to view basic information about the web app
2. view and interact with the documentation
3. register to view more details
4. Upload files(Image, CSV, pdf, and json)
5. Generate/fetch metadata of the files uploaded
6. Export, download, and share
7. Save data and come back to download

## Special Links

#### [Project Documentation]().

#### [Database Schema Diagram](https://www.figma.com/file/fIeIf2BakTUAXfUTv9EFnx/Team-83-DATABASE-SCHEMA?node-id=0%3A1).

#### See our [design on Figma](https://www.figma.com/file/KyMXrf2whjJerytHr8occj/Meta-Data-Website?node-id=127%3A1494)

#### Go to the website [here](metatrack.zurifordummies.com) and [here](metatrack.herokuapp.com)

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

contributions are always welcome!

- #### Fork The Project Repository
  Find the project's repository on github, and then 'fork' it by clicking the fork button in the upper right corner.
- #### Clone Your Fork
  While still in the repository, click the green clone or download button and then copy the https url.

Using git on the local machine, clone your fork using the url copied: git clone url_of_fork.

- #### Add The Project Repository As The "Upstream" Remote

  Add it to the repository using `git remote add upstream https://github.com/zuri-training/proj_fetch_meta_data_team_83` .
  Use `git remote -v` to check that you now have two remotes: an origin that points to your fork, and an upstream that points to the project repository.

- #### Pull Request

  Use `git pull upstream main` to "pull" any changes from the "main" branch of the "upstream" into the local repository.

- #### Create A New Branch

  Create a new branch using `git checkout -b <branch_name>` to create a new branch and then immediately switch to it. the name of the branch should briefly describe what you are working on.

- #### Make Changes In Local Repository Using A Text Editor Or IDE.

- #### Commit Changes

  After making a set of changes, use `git add -A` to stage changes and `git commit -m <description of changes> <branch of the "origin">` (which is your fork on github).

- #### Begin The Pull Request

  Return to fork on github, and referesh the page. Click the green compare & pull request button to begin the pull request. Alternatively, you can switch to your branch using the branch button and then click the new pull request button.

- #### Create The Pull Request
  Below the pull request form, you will see a list of the commits you made in your branch, as well as the "diffs" for all of the files you changed.

If everything looks good, click the green create pull request button!

- #### Synchronize Your Fork With The Project Repository

At this point, your fork is out of sync with the project repository's main branch.

To get it back in sync, use `git pull upstream main`

### Credits

To [ingressive for good and zuri team](https://training.zuri.team/) for the training and opportunity to carryout this project.

### Contributors

Our team is made up of wonderful people, who all cotributed to this project to make it successful

1. [Idimmachukwu Okoro](github.com/idimmusix) Team Lead/Backend Developer
2. [Victoria Oladosu-Theverifiedvee](github.com/theverifiedvee) Assistant Team Lead/Product Designer
3. [Oluwatobiloba Bamisebi](github.com/oluwatobiloba1) Documenter/Backend Developer
4. [Chijioke Chibuike](github.com/chisquare7) Frontend Team Lead
5. [Regina Onwuachumba](github.com/onwuachumba) Frontend Developer/Team Motivator
6. [Abigail Agarin](github.com/abbiagarin) Frontend Developer/Assitant Documenter
7. [Adeyeni Joseph Damilola](github.com/dvrmvc) Product Designer
8. [Naandam Dariem](github.com/dariemjnr) Frontend Developer
9. [Tobi Emmanuel](github.com/thobiy) Backend Developer
10. [Yusuff Olatunji Sikiru](github.com/seek-techs) Backend Developer
11. [Miracle Anyanwu](github.com/pyth0nkod3r) Backend Developer
12. [Joshua](github.com/joshthefullstack) Frontend Developer
13. [Omowumi Ishola](github.com/omowumiishola) Backend Developer
    . [Opeyemi Mulkkah](github.com/horpehyemmy) Product Designer
14. [Ottah Blessing Oghenewarhe](github.com/moblessing) Product Designer
15. [Adebiyi Peace](github.com/adebiyipeace) Product Designer
16. [Chinedu](github.com/edujuventus) Product Designer
17. [Inamu Grace Osina](github.com/osina91) Product Designer
18. [Ajadi Muibat Taiwo](github.com/muhibbah) Product Designer
19. [Tinux](github.com/tinux001) Product Designer
20. [Atinuke Yewande](github.com/ye-wande) Product Designer

### License

=======
