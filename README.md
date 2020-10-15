<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/hirokiyaginuma/scriptspinner-website">
    <img src="/templates/static/img/SS_logo_github.png" alt="Logo" width="80%" height="80%">
  </a>

  <h3 align="center">Script Spinner Website</h3>

  <p align="center">
    https://scriptspinner.com/
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<a href="https://github.com/hirokiyaginuma/scriptspinner-website">
    <img src="/templates/static/img/SS_website_github.png" alt="Website" width="50%" height="50%">
</a>

Script Spinner is the software for planning, organizing and executing script content. This repository is the development code for the official script spinner website.



### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* [Python](https://www.python.org/)
* [Git](https:/git-scm.com/)

To check if you have python and git installed on your computer, go to the terminal and enter the following:

```sh
python --version
```
```sh
git --version
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/hirokiyaginuma/scriptspinner-website
```
2. Make sure you are in the project directory
```sh
cd scriptspinner-website
```
3. Start your virtual environment
Windows:
```sh
python -m venv myvenv
```
Linux and OS X:
```sh
python3 -m venv myvenv
```
3. Activate your virtual environment (Make sure you're on the virtual environment evrrytime you launch the terminal.)
Windows:
```sh
myvenv\Scripts\activate
```
Linux and OS X:
```sh
source myvenv/bin/activate
```
4. Install required package for the project
```sh
pip install -r requirements.txt
```
5. Create envirnment file for local development (For details, see [python-decouple](https://github.com/henriquebastos/python-decouple/))
Create a .env text file on your repository's root directory in the form like:
```
DEBUG=True
SECRET_KEY=ThisIsSupposedToBeSecret
ALLOWED_HOSTS=*
DB_NAME=dbname
DB_USER=dbusername
DB_PASSWORD=dbpassword
DB_HOST=dbhostname
DB_PORT=dbport
```
For our contributors: Please ask me about the detail setting about env file on the developmental server and production server.




<!-- USAGE EXAMPLES -->
## Usage

This repository is used to develop the official Script Spinner website. To start the development server, you need to enter the following command:
```sh
python manage.py runserver
```



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/hirokiyaginuma/scriptspinner-website/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b your-branch-name`)
3. Commit your Changes (`git commit -m 'Comment goes here'`)
4. Push to the Branch (`git push origin your-branch-name`)
5. Open a Pull Request



<!-- LICENSE -->
## License

TBA



<!-- CONTACT -->
## Contact

Hiroki Yaginuma -  hirokiyaginuma21@gmail.com

Project Link: [https://github.com/hirokiyaginuma/scriptspinner-website](https://github.com/hirokiyaginuma/scriptspinner-website)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Python Tutorial](https://www.w3schools.com/python/python_intro.asp)
* [Django Tutorial](https://tutorial.djangogirls.org/en/)
* [Bootstrap Documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hirokiyaginuma/scriptspinner-website.svg?style=flat-square
[contributors-url]: https://github.com/hirokiyaginuma/scriptspinner-website/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hirokiyaginuma/scriptspinner-website.svg?style=flat-square
[forks-url]: https://github.com/hirokiyaginuma/scriptspinner-website/network/members
[stars-shield]: https://img.shields.io/github/stars/hirokiyaginuma/scriptspinner-website.svg?style=flat-square
[stars-url]: https://github.com/hirokiyaginuma/scriptspinner-website/stargazers
[issues-shield]: https://img.shields.io/github/issues/hirokiyaginuma/scriptspinner-website.svg?style=flat-square
[issues-url]: https://github.com/hirokiyaginuma/scriptspinner-website/issues
[license-shield]: https://img.shields.io/github/license/hirokiyaginuma/scriptspinner-website.svg?style=flat-square
[license-url]: https://github.com/hirokiyaginuma/scriptspinner-website/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hiroki-yaginuma-6719271b6
[product-screenshot]: images/screenshot.png
