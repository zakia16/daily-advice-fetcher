# Daily Advice Fetcher - n8n Edition

This project is a **low-code automation** built using [n8n](https://n8n.io/), designed to fetch and send random advice via email using the [Advice Slip API](https://api.adviceslip.com/).
I originally created this project in Python. 


## How it works in Python

- Sends a GET request to the Advice Slip API.
- Parses the JSON response.
- Prints the advice to the console.
- Handles network errors gracefully.

## The n8n workflow:

1. Triggers when you manually click **"Execute Workflow"**
2. Sends an HTTP GET request to fetch a random piece of advice from [https://api.adviceslip.com/advice](https://api.adviceslip.com/advice)
3. Sends the advice as a Gmail message to your email
![image](https://github.com/user-attachments/assets/669a5402-663d-4144-bb37-39e28dd5b6a0)


## Requirements for Python 

- Python 3.x
- `requests` library

```bash
pip install requests
```

## Usage

Run the script from the terminal:

```bash
python fetch_advice.py
```

## License

This project is open source and free to use


![image](https://github.com/user-attachments/assets/ca867451-ee31-42b2-9818-a50069d53d12)



