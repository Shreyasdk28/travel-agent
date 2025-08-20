import json
import os
import requests
from langchain.tools import tool


class SearchTools:

    @tool("Search the internet")
    @staticmethod
    def search_internet(query: str) -> str:
        """Search the internet about a given topic and return relevant results."""
        top_result_to_return = 4
        url = "https://google.serper.dev/search"

        # Ensure API key exists
        api_key = os.environ.get("SERPER_API_KEY")
        if not api_key:
            return "Error: SERPER_API_KEY environment variable not set."

        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': api_key,
            'content-type': 'application/json'
        }

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            return f"Error fetching results: {str(e)}"

        # Check for valid results
        if 'organic' not in data:
            return "Sorry, I couldn't find anything. Check if your Serper API key is correct."

        results = data['organic']
        string = []

        for result in results[:top_result_to_return]:
            try:
                string.append("\n".join([
                    f"Title: {result.get('title', 'N/A')}",
                    f"Link: {result.get('link', 'N/A')}",
                    f"Snippet: {result.get('snippet', 'N/A')}",
                    "\n-----------------"
                ]))
            except Exception:
                continue

        return '\n'.join(string) if string else "No results found."
