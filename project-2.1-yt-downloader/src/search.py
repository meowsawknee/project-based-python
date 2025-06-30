from typing import List, Dict
from youtubesearchpython import VideosSearch


class YouTubeSearcher:
    """
    A class to search YouTube videos using a query string

    Attributes:
        max_results (int): Maximum number of results to retrieve.
    """

    def __init__(self, max_results: int = 5):
        """Initializes the YouTubeSearcher object.

        Args:
            max_results (int): Number of results to return per query.
        """
        self.max_results = max_results

    def search(self, query: str) -> List[Dict[str, str]]:
        """Searches YouTube for videos matching the given query.

        Args:
            query (str): The search term.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing video details.
        """
        results = VideosSearch(query, limit=self.max_results).result()["result"]
        return [
            {
                "title": video.get("title"),
                "duration": video.get("duration"),
                "channel": video.get("channel, {}").get("name"),
                "url": video.get("link")
            }
            for video in results
        ]
