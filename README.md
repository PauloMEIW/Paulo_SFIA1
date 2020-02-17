# SFIA Project - Solo Project at QA Consulting

E-Commerce application

## Index
[Brief](#brief)
   * [Solution](#solution)
   * [Setup](#setup)
   
[Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)
   * [Multi Tier Architechture Diagram](#mla)
	
[Testing](#testing)
   * [Report](#report)
     
[Deployment](#depl)
   * [Technologies Used](#tech)
     
[Front End Design](#FE)

[Improvements for the Future](#improve)

[Acknowledgements](#ack)

[Author](#auth)

<a name="brief"></a>
## The Brief

To create an OOP-based application with utilisation of supporting tools (Github, Jenkins, Linux ), methodologies ( Agile ) and technologies that encapsulate all core modules covered during QA Intensive training such HTML, Python and SQL ).
Aplication posses the capacity to manipulate a database ( CRUD - create, read, Update and delete functionality )using front end interface created using Flask Python framework.

<a name="solution"></a>
### Solution



I decided to create a personal yoga application that would allow the user to create poses and routines, as well as add and remove poses from each routine.
The many to many relationship between poses and routines is working, where poses can be added and removed from routines.

<a name="setup"></a>
### Setup
```bash
# create virtual environment
python3 -m venv
# load virtual environment
source venv/bin/activate
# make sure our dependencies are installed
pip install -r requirements.txt
```

<a name="arch"></a>
## Architecture

<a name="erd"></a>
### Entity Relationship Diagrams


<a name="test"></a>
## Testing
????????????????   tests have been used for automated testing, and SonarLint/SonarQube for static reporting and refactoring.

<a name="rep"></a>
### Report

Picture and resuls of the test


<a name="dep"></a>
## Deployment
The build, test and deployment process was automated using Jenkins, with a webhook to GitHub which was triggered with every push event

This application can be deployed both locally and externally through a virtual machine. The constants.js file has commented out options to switch from an external to local IP address.   edittttttttttttttttttttttttttt
imagem dos tools usadosssssssssssss

<a name="tech"></a>
### Technologies Used
* SQLlite - Database
* AAAAAAA - Deployment
* Jenkins - CI Server
* AAAAAA- Dependency Management
* AAAAAA - Test Reporting
* AAAAAA - Static Testing
* [Git](https://github.com/PauloRibeiroIT/Paulo_SFIA1) - VCS
* [Trello](https://trello.com/b/VFRNnQYX/project-sfia) - Project Tracking
* GCP - Live Environment


<a name="fro"></a>
## Front End Design

<a name="auth"></a>
## Author
Paulo Ribeiro - DevOps Consultant
2020
