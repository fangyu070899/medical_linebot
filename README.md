# medical linebot
#### TOC Project 111-1

<!-- TABLE OF CONTENTS -->

<ol>
<li><a href="#about-the-project">About The Project</a></li>
<li><a href="#environment">Environment</a></li>
<li><a href="#technics">Technics</a></li>
<li>
  <a href="#getting-started">Getting Started</a>
  <ul>
    <li><a href="#greeting-messages">Greeting messages</a></li>
  </ul>
</li>
<li><a href="#features">Features</a></li>
<li><a href="#FSM">FSM</a></li>
<li><a href="#state">State</a></li>
<li><a href="#demo">Demo</a></li>
<li><a href="#reference">Reference</a></li>
</ol>




<!-- ABOUT THE PROJECT -->
## About The Project
This is a line bot you can ask for medical knowledge, including diseases, symptoms, exercises and so on. The information contained in this linebot comes from the web "康健知識庫".



## Environment
* python 3.10.9
* Deploy by Heroku

## Technics 
* line bot : Built by the official LINE Messaging API.
* Backend: Built the backend with Flask to handle the webhook.
* FSM: Create FSM with pytransitions for the users state management.
* web scraping : Use selenium and chrome driver to retrieve medical information from several webpages.

<!-- GETTING STARTED -->
## Getting Started

### Greeting messages
<div >
    <image src="https://i.imgur.com/fiksM3E.jpg" width=300>
    <image src="https://i.imgur.com/l06J1QY.jpg" width=300>
<div/>

### rich menu & text input
<div >
    <image src="https://i.imgur.com/qKzbZxR.jpg" width=300>
    <image src="https://i.imgur.com/ooOtw15.jpg" width=300>
<div/>


<!-- ROADMAP -->
## Features
* 健康百科 (for example)        
1. You can select a category, and then linebot will list all options ( use several images )
2. There are some quick reply buttons, so you don't have to type the word if what you want to search is included. Just click it.
3. Quick reply in final state (below three) are different from the keywords. That is, how many options and what kind of options appear is decided by how much information is on the website.
4. All pictures are super pretty. ( Of course, I made them. XD )
<div >
    <image src="https://i.imgur.com/iefbBXx.jpg" width=300>
    <image src="https://i.imgur.com/TieInfA.jpg" width=300>
    <image src="https://i.imgur.com/2aiV0Rk.jpg" width=300>
    <image src="https://i.imgur.com/Kb2K8NQ.jpg" width=300>
    <image src="https://i.imgur.com/f3gd0Ua.jpg" width=300>
    <image src="https://i.imgur.com/nagHy5H.jpg" width=300>
<div/>

## FSM
![](https://i.imgur.com/w4uiVFe.png)

## State
* user : The entry. In this state, you can send text messages or click the rich menu below to start the conversation.
* searched_term : When you asks for a disease, symptom description or anything the linebot knows, you will get to this state. In this state, linebot replies the information of specific keyword (which the user want to know), and then it will asks that whether you want to know more information time and again. As a result, this is a final state. 
* suggest_term : if linebot received something doesn't match a single disease or symptom, it will list all possible options for you.
* disease : List all deseases in a specific category you chose. 
* symptom : List all symptoms in a specific category you chose. 
* _category : The states which you can choose category.

## Demo
### 健康百科
<div>
    <image src="https://i.imgur.com/iefbBXx.jpg" width=300>
    <image src="https://i.imgur.com/TieInfA.jpg" width=300>
    <image src="https://i.imgur.com/2aiV0Rk.jpg" width=300>
    <image src="https://i.imgur.com/Kb2K8NQ.jpg" width=300>
    <image src="https://i.imgur.com/f3gd0Ua.jpg" width=300>
    <image src="https://i.imgur.com/nagHy5H.jpg" width=300>
<div/>    
<br />
      
### 症狀百科
<div>
    <image src="https://i.imgur.com/jDwosxk.jpg" width=300>
    <image src="https://i.imgur.com/xdS6aQ4.jpg" width=300>
    <image src="https://i.imgur.com/qKQVb0Y.jpg" width=300>
<div/>       
<br />
      
### 飲食百科
<div>
    <image src="https://i.imgur.com/MLEEIMX.jpg" width=300>
    <image src="https://i.imgur.com/203Jttf.jpg" width=300>
    <image src="https://i.imgur.com/1xDL3pg.jpg" width=300>
<div/>     
<br />
      
### 運動百科
<div>
    <image src="https://i.imgur.com/WUl1w2j.jpg" width=300>
    <image src="https://i.imgur.com/Z2iFhmx.jpg" width=300>
    <image src="https://i.imgur.com/59UxNn5.jpg" width=300>
<div/>  
<br />
      
### 營養百科
<div>
    <image src="https://i.imgur.com/wwtkf26.jpg" width=300>
    <image src="https://i.imgur.com/iLEO5Nb.jpg" width=300>
    <image src="https://i.imgur.com/1L8NhwZ.jpg" width=300>
<div/>    
<br />
      
### 打字輸入
<div>
    <image src="https://i.imgur.com/2MmxuLG.jpg" width=300>
    <image src="https://i.imgur.com/nYh7b6G.jpg" width=300>
<div/>    

<!-- ACKNOWLEDGMENTS -->
## Reference

* [康健知識庫](https://kb.commonhealth.com.tw/)
* 疾管家
<p align="right">(<a href="#readme-top">back to top</a>)</p>




