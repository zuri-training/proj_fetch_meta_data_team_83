# Idimmachukwu Okoro's contribution to team 83 fetch meta data

 - I and Regina created the database schema design page in figma [click here to view](https://www.figma.com/file/fIeIf2BakTUAXfUTv9EFnx/Team_83-DATABASE-SCHEMA?node-id=91%3A102)
 - With respect to [this issue](https://github.com/zuri-training/proj_fetch_meta_data_team_83/issues/20), I developed the accounts configuration for our app  [click here to view the code](https://github.com/zuri-training/proj_fetch_meta_data_team_83/tree/main/fetch_metadata/apps/accounts)

    I have created the authentication and authorisation endpoints, 
    -  custom user model object whose entry point to our application requires an email and username
    -  configured the user to user their username as a slug to view their profile
    -  custom user profile comprising of the profile picture, the job description, A short bio.
    -  custom user forms backend for signup,  login, password change, 
    -  backend views for the custom user and custom user profile to enable CRUD operations on the user object
    - configured the urls to connect with the front end.
    -  I created a custom admin, that can view all information about the users for regulation purposes
 - I implemented our [exifcreator](https://github.com/zuri-training/proj_fetch_meta_data_team_83/blob/main/fetch_metadata/apps/file_control/exifcreator.py) to write metadata to a `.mttrck` file and save the file path to the database asynchronously using [celery](https://github.com/zuri-training/proj_fetch_meta_data_team_83/blob/main/fetch_metadata/apps/file_control/tasks.py). The file thus generated is downloadable by the end user
 - I also assisted in templating the frontend html to the backend