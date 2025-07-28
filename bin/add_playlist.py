#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path
import requests
from bs4 import BeautifulSoup

# --- Configuration ---
# The root directory of the Jekyll project.
# The script assumes it is located in the 'bin' subdirectory of the project.
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
IMAGE_DIR = PROJECT_ROOT / "assets" / "images"
MUSIC_FILE = PROJECT_ROOT / "music.md"

def clean_filename(text):
    """
    Cleans a string to be suitable for a filename.
    - Removes special characters.
    - Replaces spaces with underscores.
    - Converts to lowercase.
    """
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    return text.replace(' ', '').replace('-', '')

def get_playlist_metadata(url):
    """
    Fetches the Spotify playlist page and extracts metadata.

    Args:
        url (str): The URL of the Spotify playlist.

    Returns:
        A tuple containing (playlist_title, image_url) or (None, None) on error.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the full page title
        full_title = soup.find('title').text

        # Extract the playlist name from the title (e.g., "My Playlist - playlist by User | Spotify")
        playlist_title = full_title.split(' - ')[0].strip()

        # Find the cover image URL from the 'og:image' meta tag
        og_image_tag = soup.find('meta', property='og:image')
        image_url = og_image_tag['content'] if og_image_tag else None

        if not playlist_title or not image_url:
            print("Error: Could not extract playlist title or image URL.", file=sys.stderr)
            return None, None

        return playlist_title, image_url
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        return None, None

def download_image(url, shortname):
    """
    Downloads an image and saves it to the IMAGE_DIR.

    Args:
        url (str): The URL of the image to download.
        shortname (str): The base name for the saved image file.

    Returns:
        The Path object of the saved image, or None on error.
    """
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        # Determine the file extension from the URL, default to .png
        file_extension = Path(url).suffix or '.png'
        image_path = IMAGE_DIR / f"{shortname}{file_extension}"

        with open(image_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Successfully downloaded image to: {image_path}")
        return image_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}", file=sys.stderr)
        return None

def add_entry_to_music_file(playlist_url, shortname, image_path, title):
    """
    Appends a new playlist entry to the music.md file.
    """
    relative_image_path = f"/{image_path.relative_to(PROJECT_ROOT)}"
    entry = (
        f"* [{title}]({playlist_url})\n"
        f"  ![]({relative_image_path})\n"
        f"  > A great playlist."
    )

    with open(MUSIC_FILE, 'a') as f:
        f.write("\n\n" + entry)
    print(f"Successfully added entry for '{title}' to {MUSIC_FILE}")


def main():
    """Main function to orchestrate the script."""
    parser = argparse.ArgumentParser(
        description="Automate adding a Spotify playlist to your Jekyll site."
    )
    parser.add_argument("url", help="The full URL of the Spotify playlist.")
    args = parser.parse_args()

    print(f"Fetching metadata for playlist: {args.url}")
    title, image_url = get_playlist_metadata(args.url)

    if not title or not image_url:
        sys.exit(1)

    shortname = clean_filename(title)
    print(f"Generated shortname: {shortname}")

    # Ensure the image directory exists
    IMAGE_DIR.mkdir(exist_ok=True)

    image_path = download_image(image_url, shortname)
    if not image_path:
        sys.exit(1)

    add_entry_to_music_file(args.url, shortname, image_path, title)


if __name__ == "__main__":
    main()
