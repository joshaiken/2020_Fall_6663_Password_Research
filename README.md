# Memorable Password Generator
* Author: Joshua Aiken
* September 2020 to October 2020
* 2020_Fall_6663_Password_Research

## Table of Contents
* [About](#about)
* [Technologies](#technologies)
* [Setup](#setup)
* [Development Tasks](#development-plan)
* [Sources & Credits](#sources)

## About
* 2020 Fall CSCI 6663 - Software Security__
* Professor: Minhaz Zibran, University of New Orleans 
 
 This tool was written as part of a research project for the above class to generate passwords that are (hopefully, as this is the thesis being tested) both more memorable (to an end-user) and computationally complex than an average password. 

## Technologies
This project is created with and has dependencies on the following:
* Python 3.8.2
* pip3
* pytest 6.1.1


## Setup
To run this project, run the PasswordGenerator.py file.

## Development Tasks
1. ~~Test new environment w/ helloworld~~
2. ~~Test unit testing on new environment~~
3. Parse Dictionary CSV for a random...
    1. noun
    2. adverb
    3. adjective
4. Output CSV of 1000 enties each of...
    1. 4 words (CamelCase)
    2. 3 words (CamelCase)
5. Manually Evaluate terms for reasonableness
6. Implement "Coherent" structures which are allowed to be generated
    1. e.g. "AdjectiveNounNounNoun" = "CorrectHorseBatteryStaple" (thanks XKCD - https://xkcd.com/936)
7. Make Seperate function to query PasswordGenerator.py and retreive output
    1. print to command line
    2. output to alert box
    3. output to string

----- Minimum Usable Product for Research Purposes -----

8. Prompt user for WordNik API key
9. Get Random word from API
10. Classify word as a "noun, adjective, adverb" or discard it
11. Generate Passwords from list

## Sources & Credits
No credits as of yet. 

## Useless Note
Personally, I prefer using ~~strikethrough~~ to show progress over
- [ ] checkboxes, strictly because I enjoy the wry humor one can communicate with them 
- [x] even though I have not problem wht checkboxes