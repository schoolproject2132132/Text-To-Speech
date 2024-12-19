# Text to Speech Script

## Description

This Python script takes user input (text) and converts it into speech. It works across **Linux**, **macOS**, and **Windows** operating systems. Depending on the platform, the script uses different text-to-speech tools:

- **Linux**: Uses `espeak`
- **macOS**: Uses the built-in `say` command
- **Windows**: Uses the `pyttsx3` library

## Features
- Converts text input into speech.
- Cross-platform support (Linux, macOS, Windows).
- Easy to use with no setup required (on macOS and Linux; just install dependencies on Windows).

## Requirements

- **Linux**: Ensure that `espeak` is installed (`sudo apt install espeak` on Ubuntu).
- **macOS**: The `say` command is built into macOS, so no installation is needed.
- **Windows**: Install the `pyttsx3` library using `pip`.

## Installation

1. Install Python on your system (if it's not already installed).
2. Install the required library for **Windows**:
   ```bash
   pip install pyttsx3
