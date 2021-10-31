
# Student Registration Details

Developed a form to accept and display details of the users.

## Run Locally

Clone the project

```bash
  git clone https://github.com/Vibhav0/PythonProjects.git
```

Go to the project directory

```bash
  cd Student_Registration_Details
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`ALGORITHM`=`"HS256"`

To generate a secure random secret key use the command:

`openssl rand -hex 32`

## Class Diagram

![Class Diagram](https://user-images.githubusercontent.com/73296863/139574346-4fad26f1-54fb-4ebb-b1fe-994a3e47606f.png)

## ER Diagram


![er-diagram drawio](https://user-images.githubusercontent.com/73296863/139577567-c789b688-0386-4cb4-8815-652a1b5b8574.png)

## Tech Stack

**Client:** HTML5, CSS, Bootstrap, Javascript

**Server:** Uvicorn


## Related

Here are some related projects

[Auth](https://github.com/Vibhav0/Auth)


## Appendix

[Live Using NGINX as webserver](https://conscript-web.ddns.net/login/)

[Live Demo on heroku](https://conscript-webapplication.herokuapp.com)


## Feedback

If you have any feedback, please reach out to me at survevibhav09@gmail.com

