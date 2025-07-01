from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError
from typing import Optional, Any
import os
import shutil
import subprocess
from tqdm import tqdm
from src.utils import (
    seconds_from_timestamp,
    sanitize_filename,
    ensure_dir,
)

class YouTubeDownloader:
    """
    A class for downloading YouTube videos and audio with optional trimming and progress feedback.
    """

    def __init__(self, url: str):
        """Initialize the YouTubeDownloader object with a video URL.

        Args:
            url (str): The YouTube video URL.
        """
        self.url = url
        self.yt: Optional[YouTube] = None
        self._pbar = None
        self._load_video()
    
    def _load_video(self) -> None:
        """Attempts to load the YouTube object from the provided URL, with progress callbacks.
        """
        try:
            self.yt = YouTube(
                self.url,
                on_progress_callback=self._on_progress,
                on_complete_callback=self._on_complete
            )
        except (VideoUnavailable, RegexMatchError) as e:
            raise ValueError(f"Cannot load video: {e}")
    
    def list_streams(self) -> dict:
        """
        Returns available streams in a dictionary:
        { 'video': [...], 'audio': [...] }

        Returns:
            dict: Dictionary containing video and audio stream lists.
        """
        streams = self.yt.streams
        return {
            "video": streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc(),
            "audio": streams.filter(only_audio=True).order_by("abr").desc()
        }

    def download(
        self,
        output_path: str,
        filename: str,
        audio_only: bool = False,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        resolution: Optional[str] = None
    ) -> str:
        """
        Downloads the selected stream and optionally trims it using ffmpeg.

        Args:
            output_path (str): Folder to save the file.
            filename (str): Output file name (Without extension).
            audio_only (bool): Whether to download audio-only.
            start_time (str): Optional start time (e.g., "00:05:36").
            end_time (str): Optional end time (e.g., "00:07:03").
            resolution (str): Video resolution to filter (e.g., "720p"). 

        Returns:
            str: Path to the final saved file.
        """
        ensure_dir(output_path)
        filename = sanitize_filename(filename)

        stream = None
        if audio_only:
            stream = self.yt.streams.filter(only_audio=True).order_by("abr").desc().first()
            file_path = os.path.join(output_path, f"{filename}.mp4")  # Will rename to .mp3
        else:
            if resolution:
                stream = self.yt.streams.filter(progressive=True, file_extension="mp4", res=resolution).first()
            if not stream:
                stream = self.yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
            file_path = os.path.join(output_path, f"{filename}.mp4")
        
        print(f"\nStarting download: {filename}")
        stream.download(output_path=output_path, filename=filename)

        # Trim if needed
        if start_time and end_time:
            trimmed_path = os.path.join(output_path, f"{filename}_trimmed.mp4")
            self._trim_with_ffmpeg(file_path, trimmed_path, start_time, end_time)
            os.remove(file_path)
            return trimmed_path
        
        # Rename audio-only to .mp3
        if audio_only:
            mp3_path = os.path.join(output_path, f"{filename}.mp3")
            os.rename(file_path, mp3_path)
            return mp3_path
        
        return file_path

    def _trim_with_ffmpeg(self, input_file: str, output_file: str, start: str, end: str) -> None:
        """Trims a media file using ffmpeg from start to end time.

        Args:
            input_file (str): Path to the input file.
            output_file (str): Path to the output trimmed file.
            start (str): Start time in format "HH:MM:SS".
            end (str): End time in format "HH:MM:SS"

        Raises:
            EnvironmentError: If ffmpeg is not installed or not found in system PATH.
            RuntimeError: If ffmpeg execution fails.
        """
        if not shutil.which("ffmpeg"):
            raise EnvironmentError(
                "'ffmpeg' is not installed or not found in your system PATH.\n"
                "Please install ffmpeg from https://ffmpeg.org/download.html and try again."
            )
        try:
            subprocess.run(
                [
                    "ffmpeg",
                    "-i", input_file,
                    "-ss", start,
                    "-to", end,
                    "-c", "copy",
                    output_file
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError:
            raise RuntimeError("Failed to trim the video with ffmpeg.")

    def _on_progress(self, stream: Any, chunk: bytes, bytes_remaining: int) -> None:
        """Callback function to show download progress.

        Args:
            stream: The stream being downloaded.
            chunk: The data chunk received.
            bytes_remaining: The remaining bytes to be downloaded.
        """
        if self._pbar is None:
            total = stream.filesize
            self._pbar = tqdm(total=total, unit="B", unit_scale=True, desc="Downloading...")

        bytes_downloaded = self._pbar.total - bytes_remaining
        self._pbar.n = bytes_downloaded
        self._pbar.refresh()
    
    def _on_complete(self, stream: Any, file_path: str) -> None:
        """Callback function to be called when download is complete.

        Args:
            stream: The completed stream.
            file_path: The path to the completed file.
        """
        if self._pbar:
            self._pbar.close()
        print("\nDownload completed successfully!")
