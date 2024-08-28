# Personality-Chatbot


## Description

This project is a Telegram bot integrated with OpenAI's GPT API, designed to engage in conversations with users. The bot handles user messages, stores conversation history in a SQLite database, and dynamically generates responses using AI. The project is built using Python, leveraging libraries such as python-telegram-bot for Telegram API interaction, SQLAlchemy for ORM, and FastAPI for optional webhook-based deployment.


## Features


Dynamic Responses: The bot interacts with users, processes their input, and generates responses using the OpenAI GPT API.

User Management: Tracks users and their conversation history in an SQLite database.

Polling & Webhook Support: The bot can operate via Telegram's polling method or through a FastAPI-based webhook.

Error Handling: Basic error management to ensure smooth user experience.


## Project Structure


main.py: Main entry point for the bot. Handles Telegram commands and messages.

crud.py: Contains CRUD functions for interacting with the database.

db_connection.py: Manages database connections and models.

Database.py: Defines the SQLAlchemy models for users and messages.

.env: Environment variables for API keys and configurations (not included in the repository).


## Prerequisites

Ensure you have the following installed on your system:

Python 3.7+

pip (Python package installer)

SQLite (or any other database, if you're using a different DB backend)



