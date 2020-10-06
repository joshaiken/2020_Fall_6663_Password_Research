# Memorable Password Generator
Author: Joshua Aiken
September 2020 to October 2020
2020_Fall_6663_Password_Research

## Table of Contents
* [About](#about)
* [Technologies](#technologies)
* [Setup](#setup)
* [Development Plan](#development-plan)
* [Sources & Credits](#sources)

## About
 2020 Fall CSCI 6663 - Software Security
 Professor: Minhaz Zibran, University of New Orleans
 This tool was written as part of a research project for the above class
 to generate passwords that are (hopefully, as this is the thesis being tested)
 both more memorable (to an end-user) and computationally
 complex than an average password. 

## Technologies
This project is created with and has dependencies on the following:
Python 3.8.2

## Setup
To run this project, 

## Development Plan
1 - Test new environment w/ helloworld
2 - Test unit testing on new environment
3 - Parse Dictionary CSV for a random...
    a - noun
    b - adverb
    c - adjective
4 - Output CSV of 1000 enties each of...
    a - 4 words (CamelCase)
    b - 3 words (CamelCase)
5 - Manually Evaluate terms for reasonableness
6 - Implement "Coherent" structures which are allowed to be generated
    e.g. "AdjectiveNounNounNoun" = "CorrectHorseBatteryStaple" (thanks XKCD - https://xkcd.com/936)
7 - Make Seperate function to query PasswordGenerator.py and retreive output
    a - print to command line
    b - output to alert box
    c - output to string

----- Minimum Usable Product for Research Purposes -----

8 - Prompt user for WordNik API key
9 - Get Random word from API
10 - Classify word as a "noun, adjective, adverb" or discard it
11 - Generate Passwords from list

## Sources & Credits
No credits as of yet. 