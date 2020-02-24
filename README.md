
# SFIA Project 1 - QA Consulting

E-Commerce application.

## Index
[Brief](#brief)
   * [Solution](#solution)
   * [Setup](#setup)

[Project Management](#pro)

[Risk Assessment](#ris)

[Architecture](#arch)
   * [Entity Relationship Diagrams](#erd)
   * [Use Case Diagram](#use)
   * [Class Diagram](#cla)
	
[Testing](#testing)
   * [Analyse Report](#report)
     
[Deployment](#depl)
   * [Technologies Used in the Development](#tech)
     
[Interface](#inte)
   * [Demo](#demo)
   
[Author](#auth)


<a name="brief"></a>
## The Brief

To create an OOP-based application with utilisation of supporting tools (Github, Jenkins, Linux ), methodologies ( Agile ) and technologies that encapsulate all core modules covered during QA Intensive training such HTML, Python and SQL ).
Aplication posses the capacity to manipulate a database ( CRUD - create, read, update and delete functionality ) using front end interface created using Flask Python framework.

This project involve concepts from all core training modules, as such:
* Agile
* Python Fundamentals
* Python Testing
* Git
* Continuous Integration
* Basic Linux
* Python Web Development
* Cloud Fundamentals
* Databases

<a name="solution"></a>
### Solution

I decided to create an e-commerce application that would allow the user to create and update own account, add and delete review of the store or product and also add, read and delete product from the products table acessing to the Store page.

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


<a name="pro"></a>
## Project Management

<a href="https://ibb.co/SRYZT3L"><img src="https://i.ibb.co/TmjNXgC/asasasas.png" alt="asasasas" border="0"></a>

<a name="ris"></a>
## Risk Assessment

<a href="https://ibb.co/FsJ2HbT"><img src="https://i.ibb.co/s5QnWvY/riskassements.png" alt="riskassements" border="0"></a>

<a name="arch"></a>
## Architecture

<a name="erd"></a>
### Entity Relationship Diagrams
Initial Plan and Delivered Solution ( in blue ):

<a href="https://ibb.co/wY3DvrF"><img src="https://i.ibb.co/0Q8PwVR/gfdfd.png" alt="gfdfd" border="0"></a>

As shown in this ERD, I ended up changing the focus of the tables Users, Product, Review and favou ( Favourites). Here is explaned the relationship on my database.

<a name="use"></a>
### Use Case Diagram
[![use-case26853d33381d65c4.png](https://www.imageupload.net/upload-image/2020/02/20/use-case26853d33381d65c4.png)](https://www.imageupload.net/image/RucKy)

<a name="cla"></a>
### Class Diagram
<a href="https://ibb.co/yktFTmY"><img src="https://i.ibb.co/2Mx320s/68747470733a2f2f692e6962622e636f2f373279707648422f7364736164736164732e706e67.png" alt="68747470733a2f2f692e6962622e636f2f373279707648422f7364736164736164732e706e67" border="0"></a>

## Testing
Flask Unit Testing
<a name="report"></a>
### Analyse Report

<a href="https://ibb.co/pj2hdfG"><img src="https://i.ibb.co/YB20hcY/results.png" alt="results" border="0"></a><br />

## Deployment
The build, test and deployment process was automated using Jenkins, with a webhook to GitHub which was triggered with every push event
This application can be deployed both locally and externally through a virtual machine. 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/KsvZC3v/68747470733a2f2f692e6962622e636f2f643650364637322f3638373437343730373333613266326637373737373732653639366436313637363537353730366336663631363432653665363537343266373537303663366636313634326436393664363136373635326633.jpg" alt="68747470733a2f2f692e6962622e636f2f643650364637322f3638373437343730373333613266326637373737373732653639366436313637363537353730366336663631363432653665363537343266373537303663366636313634326436393664363136373635326633" border="0"></a>

<a name="tech"></a>
### Technologies Used
* [Trello](https://trello.com/b/VFRNnQYX/project-sfia) - Project Management
* SQLlite - Database
* Python - Flask Framework
* Jenkins - CI Server
* pytest - Test Reporting & Static Testing
* [Git](https://github.com/PauloRibeiroIT/Paulo_SFIA1) - Version Control System
* GCP - Live Environment

<a name="inte"></a>
## Interface
[![sssss.md.png](https://www.imageupload.net/upload-image/2020/02/20/sssss.md.png)](https://www.imageupload.net/image/RuoPp)

<a name="demo"></a>
### Demo
Demo accessible in the url below: http://35.223.133.178:5000/home

<a name="auth"></a>
## Author
Paulo Ribeiro - DevOps Consultant
2020
