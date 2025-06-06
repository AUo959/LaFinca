from bs4 import BeautifulSoup

files = [
    "index.html",
    "index_1.html",
    "index_2.html",
    "index_3.html",
    "index_4.html"
]

# Use the head from the first file
with open(files[0], "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")
    head = soup.head
    bodies = [soup.body]

# Collect body contents from the rest
for file in files[1:]:
    with open(file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        if soup.body:
            bodies.append(soup.body)

# Create merged HTML
merged_html = "<!DOCTYPE html>\n<html>\n"
