from fetch import submissions
from generator import create_file

for sub in submissions:
    create_file(sub["title"], sub["titleSlug"])