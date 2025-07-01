import argparse
import sys
from downloader import YouTubeDownloader
from search import YouTubeSearcher
from config import DEFAULT_SEARCH_RESULTS, DEFAULT_OUTPUT_DIR, DEFAULT_FILENAME, DEFAULT_RESOLUTION, DEFAULT_AUDIO_ONLY


def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="YouTube Downloader - Download videos or audio from YouTube with optional trimming."
    )

    parser.add_argument(
        "--url",
        type=str,
        help="YouTube video URL"
    )

    parser.add_argument(
        "--output",
        type=str,
        default=DEFAULT_OUTPUT_DIR,
        help="Folder to save the file (default: downloads/)"
    )

    parser.add_argument(
        "--name",
        type=str,
        default=DEFAULT_FILENAME,
        help="Desired output file name (Without extension)"
    )

    parser.add_argument(
        "--quality",
        type=str,
        default=DEFAULT_RESOLUTION,
        help="Video resolution (e.g., 720p). Ignored in audio-only mode."
    )

    parser.add_argument(
        "--audio-only",
        action="store_true",
        default=DEFAULT_AUDIO_ONLY,
        help="Download audio only (default: False)"
    )

    parser.add_argument(
        "--start",
        type=str,
        default=None,
        help="Start time to trim (format: HH:MM:SS)"
    )

    parser.add_argument(
        "--end",
        type=str,
        default=None,
        help="End time to trim (format: HH:MM:SS)"
    )

    parser.add_argument(
        "--search",
        type=str,
        help="Search for a YouTube video"
    )

    return parser.parse_args()


def run_search_and_select(query: str, max_results: int = DEFAULT_SEARCH_RESULTS) -> str:
    """
    Search YouTube and allow user to select a video URL

    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to display

    Returns:
        str: The URL of the selected video.
    """
    print(f"\nSearching YouTube for: '{query}'\n")
    searcher = YouTubeSearcher(max_results=max_results)
    results = searcher.search(query)

    if not results:
        print("No results found.")
        sys.exit(1)

    for idx, video in enumerate(results, 1):
        print(f"{idx}. {video['title']} ({video['duration']})")
        print(f"    Channel: {video['channel']}")
        print(f"    URL: {video['url']}\n")

    while True:
        try:
            choice = int(input(f"Enter the number of the video you want to download [1-{max_results}]: "))
            if 1 <= choice <= max_results:
                return results[choice - 1]['url']
            else:
                print(f"Please enter a number between 1 and {max_results}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """
    Main function to coordinate download or search based on CLI args.
    """
    args = parse_arguments()

    if args.search:
        args.url = run_search_and_select(args.search)

    if not args.url:
        print("Error: You must provide --url for download or --search for searching.")
        sys.exit(1)

    try:
        downloader = YouTubeDownloader(args.url)

        file_path = downloader.download(
            output_path=args.output,
            filename=args.name,
            audio_only=args.audio_only,
            start_time=args.start,
            end_time=args.end,
            resolution=args.quality
        )

        print(f"\nFile saved at: {file_path}")

    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
