Booru Grab (Danbooru + Rule34) — README

A tiny, single-file Python script that reads a text file of booru post links, downloads the corresponding images/videos, and saves their tags as prompts.
Currently only booru has been tested. 
USE WITH CAUTION!

Input: text file with one URL per line (Windows CRLF and trailing blank lines are OK)

Output: numbered files like 000.jpg, 000.txt, 001.png, 001.txt, …

Supports:

Danbooru (danbooru.donmai.us) via /posts/<id>.json

Rule34 (rule34.xxx) via Gelbooru JSON API

Features

Saves original/large image (falls back to preview if needed)

Writes comma-separated tags (prompts) next to each image

Respects sites with a polite --delay between requests

Skips blank lines and # comments in the links file

Works with CRLF (Windows) or LF (Unix) line endings

Requirements

Python 3.9+

requests library

Install once:

pip install requests
# or on Windows PowerShell:
py -m pip install requests

Setup

Save the script as booru_grab.py (use any name you like).
Put your links file (e.g., blending_dataset.txt) in the same folder, or use full paths.

Example links file:

# Danbooru
https://danbooru.donmai.us/posts/1234567

# Rule34
https://rule34.xxx/index.php?page=post&s=view&id=7654321

# trailing blank line is fine

Usage
Windows (PowerShell)

From the folder containing the script and links file:

PS D:\Grabber> py .\booru_grab.py .\blending_dataset.txt -o .\out --start 0 --delay 1.0


Or using full paths:

PS C:\> py "D:\Grabber\booru_grab.py" "D:\Grabber\blending_dataset.txt" -o "D:\Grabber\out"

macOS / Linux
python booru_grab.py ./blending_dataset.txt -o ./out --start 0 --delay 1.0

Arguments

links_file (positional): Text file with one URL per line

-o, --outdir: Output directory (default: booru_out)

--start: Starting index for filenames (default: 0)
Produces 000.jpg/.txt, 001.*, …

--delay: Seconds to sleep between posts (default: 1.0)

--dry-run: Print what would be saved without downloading

A small help for an auxilliaru script: <img width="1467" height="253" alt="image" src="https://github.com/user-attachments/assets/904c6c4b-471c-4cbe-9bd5-3ac907a40f48" />

