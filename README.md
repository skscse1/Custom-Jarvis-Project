
# Alexa-like Voice Assistant in Python

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This is a **voice-activated virtual assistant** built in Python, inspired by Alexa. The assistant can:

- Listen to user voice commands
- Open websites
- Play music from a custom library
- Fetch news headlines
- Answer general questions using **OpenAI GPT** 

It uses both offline (`pyttsx3`) and online (`gTTS`) text-to-speech engines for flexibility.

**Author:** Sukesh

---

## Features

- Speech recognition using `SpeechRecognition`
- Text-to-speech using `pyttsx3` (offline) and `gTTS` (online)
- Web automation to open popular websites
- Music playback from a custom library
- AI-powered question answering via OpenAI GPT
- Fetching live news using NewsAPI

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main script:

```bash
python main.py
```

1. The assistant will initialize and say “Initializing Alexa…”.
2. Say **"Alexa"** to activate it.
3. Give commands like:

- `"Open Google"`
- `"Play Despacito"`
- `"Give me the news"`
- `"Who is Elon Musk?"` (AI-powered responses)

---

## Configuration

1. **OpenAI API Key**  
   - Replace `YOUR_API_KEY_HERE` in the code with your OpenAI API key or use an environment variable:

   ```python
   import os
   api_key = os.getenv("OPENAI_API_KEY")
   ```

2. **News API Key**  
   - Replace `YOUR_NEWS_API_KEY` in the code with a valid [NewsAPI](https://newsapi.org/) key.

3. **Custom Music Library**  
   - Update `musiclibrary.py` with your songs and links:

   ```python
   music = {
       "song_name": "link_to_song",
   }
   ```

---

## Dependencies

- Python 3.11+
- `SpeechRecognition`
- `pyttsx3`
- `gTTS`
- `pygame`
- `requests`
- `openai`
- `musiclibrary.py` (custom module)

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add some feature"`
4. Push to branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
