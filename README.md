<h1 align="center">Django Social Network SoNet</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">A small social network for the graduation project of TeachMeSkills courses</h3>

<p align="center">
    <a href="https://github.com/nnnLik/social_network-django/stargazers">
        <img src="https://img.shields.io/github/stars/nnnLik/social_network-django.svg?logo=github">
    <a href="https://github.com/nnnLik/social_network-django">
        <img src="https://img.shields.io/github/commit-activity/w/nnnLik/social_network-django">
    <a href="https://github.com/nnnLik/social_network-django">
        <img src="https://img.shields.io/github/repo-size/nnnLik/social_network-django"></a>
    <a href="https://github.com/python/cpython">
        <img src="https://img.shields.io/badge/Python-3.9-FF1493.svg"></a>
    <a href="https://github.com/python/cpython">
        <img src="https://img.shields.io/badge/Python-3.8-FF1493.svg"></a>
    <a href="https://img.shields.io/github/languages/top/nnnLik/social_network-django">
        <img src="https://img.shields.io/github/languages/top/nnnLik/social_network-django">
    <a href="https://discord.com/channels/982762046317821992/982762046317821994">
        <img src="https://img.shields.io/discord/982762046317821992?style=flat"></a>
    <a href="https://github.com/nnnLik/social_network-django/network/members">
        <img src="https://img.shields.io/github/forks/nnnLik/social_network-django.svg?color=blue&logo=github"></a>
        <img src="https://visitor-badge.laobi.icu/badge?page_id=nnnLik.social_network-django" alt="visitors"/>   
</p>

![image](https://raw.githubusercontent.com/nnnLik/social_network-django/master/static/Banner.gif)
    
<details><summary><h4>What I used in this project</h4></summary>
    <a href="https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python">
        <img src="https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python">
    <a href="https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django">
        <img src="https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django">
    <a href="https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django">
        <img src="https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django">
    <a href="https://img.shields.io/badge/-Docker-3776AB?style=flat&logo=Docker&logoColor=white">
        <img src="https://img.shields.io/badge/-Docker-3776AB?style=flat&logo=Docker&logoColor=white">
    <a href="https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat-square&logo=Postgresql">
        <img src="https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat-square&logo=Postgresql">
    <a href="https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white">
        <img src="https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white">
    <a href="https://img.shields.io/badge/Postman-FCA121?style=flat-square&logo=postman">
        <img src="https://img.shields.io/badge/Postman-FCA121?style=flat-square&logo=postman">
</details>

<h4>Installation</h4>

1. Fork the [social_network-django](https://github.com/nnnLik/social_network-django) repository on Github
1. Clone your fork to your local machine:
   ```bash
   git clone git@github.com:<yourname>/social_network-django.git
   ```
1. Go to the project root directory:
   ```bash
   cd social_network-django
   ```
1. To install python dependencies create virtual env and аctivate the it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate:
   ```
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
1. Make migrations:
   ```bash
   python3 manage.py makemigrations
   python manage.py migrate
   ```
1. Now you can start the project:
   ```bash
   python3 manage.py runserver
   ```
1. You can also fill the database with test users if you need to. Just run this command:
   ```bash
   python3 manage.py makerecords
   ```
