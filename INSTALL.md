# Cinematch Install Guide

## Table of Contents

  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setup](#setup)
  - [Running Cinematch](#running-cinematch)

## Introduction

Cinematch is a tool for finding desired movies based on current mood and status. It is composed of a backend API and a frontend chat interface, both utilizing the OpenAI assistant platform for finetuning their LLM and generating responses.

## Prerequisites

Cinematch API requires Python. Download Python from the [official website](https://www.python.org/downloads/).

Required Python packages:

- OpenAI
- Flask
- Flask-Cors

> **Note:** These packages can be installed using PIP during the installation process.

The Cinematch Web Platform requires:

- ReactJS
- JavaScript
- npm (to install dependencies)

## Installation

To install Cinematch:

1. Clone the repository:
   ```bash
   git clone git@github.com:CSaltx/cinematch.git
   ```
2. Navigate to the repository and install required packages:
   - For the backend:
     ```bash
     cd backend
     pip install -r requirements.txt
     ```
   - For the frontend:
     ```bash
     cd frontend/chat-app/
     npm install
     ```

## Setup

To set up the project:

1. Navigate to `.env` file in the backend directory (`cinematch/backend`).
2. Open the **key.pdf** file.
3. Insert the API key into the `.env` file:
   ```bash
   OPENAI_API_KEY="YOUR-API-KEY"
   ```

> **NOTE**: This is to ensure that the API Key will not be parsed by OpenAI's crawler and remove the usage of the key. It also allows for the key to be removed from the repo fairly easily for production build if desired with an environment file for safety. Normally, it would be done like this but as this is being submitted, the API key is needed for submission. However, if this was a production build, the key would be stored via an API or only stored locally and NEVER in the github repo for security.

## Running Cinematch

Cinematch consists of an API and a web platform.

1. To run the API:
   - Navigate to the backend folder:
     ```bash
     python api.py
     ```
2. To run the web platform:
   - Open a new terminal window.
   - Navigate to the frontend/chat-app folder:
     ```bash
     npm start
     ```

The API should run on `localhost:5001/{route}` and the web server on `localhost:3000`, assuming no port conflicts.
