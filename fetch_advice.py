#!/usr/bin/env python3

import requests

def fetch_advice():
    try:
        url = "https://api.adviceslip.com/advice"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad response status

        # Parse the JSON response to extract advice
        advice_data = response.json()
        advice = advice_data['slip']['advice']
        print(f"Here's a piece of advice: \"{advice}\"")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching advice: {e}")

if __name__ == "__main__":
    fetch_advice()
