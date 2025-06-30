import argparse
import sys
from downloader import YouTubeDownloader


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="YouTube Downloader - Download videos or audio from YouTube with optional trimming."
    )

    parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="YouTube video URL"
    )

    parser.add_argument(
        "--output",
        type=str,
        default="downloads",
        help="Folder to save the file (default: downloads/)"
    )

    parser.add_argument(
        "--name",
        type=str,
        default="downloaded_file",
        help="Desired output file name (Without extension)"
    )

    parser.add_argument(
        "--quality",
        type=str,
        default=None,
        help="Video resolution (e.g., 720p). Ignored in audio-only mode."
    )

    parser.add_argument(
        "--audio-only",
        action="store_true",
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

    return parser.parse_args()

def main():
    args = parse_arguments()

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
