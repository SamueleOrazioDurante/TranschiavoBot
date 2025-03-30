

## Index
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Running with Docker](#running-with-docker)
7. [Logging and Debugging](#logging-and-debugging)

---

## Introduction
TranschiavoBot is a simple Telegram bot written in Python designed to download files from WeTransfer and SwissTransfer links. It utilizes Selenium for automating web interactions, making it an ideal solution for users who frequently receive download links via Telegram and wish to streamline file retrieval.

---

## Features
- **Automatic Download:** Detects and downloads files from WeTransfer and SwissTransfer links.
- **Selenium Automation:** Uses Selenium to automate the download process via a headless browser.
- **Telegram Integration:** Seamlessly integrates with Telegram to receive and process messages.
- **Docker Support:** Easily deployable using Docker.
- **Simple Configuration:** Manage settings via environment variables and configuration files.

---

## Installation
### Prerequisites
- Python 3.7 or higher (see `requirements.txt` for dependencies)
- pip package manager
- Selenium WebDriver (ChromeDriver or GeckoDriver, depending on your preferred browser)
- A valid Telegram Bot API token

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/SamueleOrazioDurante/TranschiavoBot.git
   ```
2. **Navigate to the repository directory:**
   ```bash
   cd TranschiavoBot
   ```
3. **(Optional) Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up environment variables:**
   - Copy the file `example.env` to `.env` and update it with your Telegram Bot token and any other configuration parameters.

---

## Configuration
- **config.py:** Contains the bot’s configuration, including the Telegram token and other relevant settings.
- **example.env:** Provides a sample configuration for environment variables. Rename and customize this file as needed.
- **tokenManager.py:** Manages API tokens securely to ensure proper authentication.

---

## Usage
To start the bot, run:
```bash
python main.py
```
The bot will connect to Telegram and begin listening for messages. Upon receiving a WeTransfer or SwissTransfer download link, it will trigger the download process using Selenium.

---

## Running with Docker
You can run the bot in a Docker container for easier deployment:
1. **Build the Docker image:**
   ```bash
   docker build -t transchiavobot .
   ```
2. **Run the container:**
   ```bash
   docker run --env-file .env transchiavobot
   ```
Alternatively, use the provided `docker-compose.yml`:
```bash
docker-compose up -d
```

---

## Logging and Debugging
- **logger.py** and **fileLogger.py** are responsible for logging the bot's activity.
- Logs are output to both the console and, if configured, to log files.
- You can adjust the logging level in `config.py` to assist with debugging.

# Documentazione in Italiano

## Indice
1. [Introduzione](#introduzione)
2. [Caratteristiche](#caratteristiche)
3. [Installazione](#installazione)
4. [Configurazione](#configurazione)
5. [Utilizzo](#utilizzo)
6. [Esecuzione con Docker](#esecuzione-con-docker)
7. [Logging e Debugging](#logging-e-debugging)

---

## Introduzione
TranschiavoBot è un semplice bot per Telegram scritto in Python, progettato per scaricare file da link di WeTransfer e SwissTransfer. Utilizza Selenium per automatizzare le interazioni web, rendendolo una soluzione ideale per gli utenti che ricevono frequentemente link di download su Telegram e desiderano semplificare il recupero dei file.

---

## Caratteristiche
- **Download Automatico:** Rileva e scarica automaticamente file da link di WeTransfer e SwissTransfer.
- **Automazione con Selenium:** Utilizza Selenium per automatizzare il processo di download tramite un browser headless.
- **Integrazione con Telegram:** Si integra perfettamente con Telegram per ricevere ed elaborare i messaggi.
- **Supporto Docker:** Facilmente deployabile utilizzando Docker.
- **Configurazione Semplice:** Gestione delle impostazioni tramite variabili d'ambiente e file di configurazione.

---

## Installazione
### Prerequisiti
- Python 3.7 o superiore (vedi `requirements.txt` per le dipendenze)
- Gestore di pacchetti pip
- Selenium WebDriver (ChromeDriver o GeckoDriver, a seconda del browser scelto)
- Un token valido per Telegram Bot API

### Passaggi
1. **Clona il repository:**
   ```bash
   git clone https://github.com/SamueleOrazioDurante/TranschiavoBot.git
   ```
2. **Naviga nella cartella del repository:**
   ```bash
   cd TranschiavoBot
   ```
3. **(Opzionale) Crea e attiva un ambiente virtuale:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```
4. **Installa le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Configura le variabili d'ambiente:**
   - Copia il file `example.env` in `.env` e imposta il token del tuo bot Telegram e gli altri parametri di configurazione.

---

## Configurazione
- **config.py:** Contiene la configurazione del bot, incluso il token di Telegram e altre impostazioni rilevanti.
- **example.env:** File di esempio per le variabili d'ambiente. Rinominalo e personalizzalo in base alle tue esigenze.
- **tokenManager.py:** Gestisce in modo sicuro i token API per garantire una corretta autenticazione.

---

## Utilizzo
Per avviare il bot, esegui:
```bash
python main.py
```
Il bot si connetterà a Telegram e inizierà ad ascoltare i messaggi. Quando riceve un link di download da WeTransfer o SwissTransfer, avvierà il processo di download utilizzando Selenium.

---

## Esecuzione con Docker
È possibile eseguire il bot tramite Docker per una gestione semplificata:
1. **Costruisci l'immagine Docker:**
   ```bash
   docker build -t transchiavobot .
   ```
2. **Avvia il container:**
   ```bash
   docker run --env-file .env transchiavobot
   ```
In alternativa, utilizza il file `docker-compose.yml` fornito:
```bash
docker-compose up -d
```

---

## Logging e Debugging
- **logger.py** e **fileLogger.py** gestiscono il logging delle attività del bot.
- I log vengono inviati sia alla console che, se configurato, a file di log.
- È possibile regolare il livello di logging in `config.py` per facilitare il debugging.
