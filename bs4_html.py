from bs4 import BeautifulSoup

html_file = "page_1.html"  # path to the HTML file

with open(html_file, "r") as f:
    soup = BeautifulSoup(f, "html.parser")  # parse the HTML file

sheet_title = ""
sheet_number = ""

# find the elements containing the sheet title and sheet number
for div in soup.find_all("div"):
    span = div.find("span")
    if span and "SHEET TITLE" in span.get_text():
        sheet_title = div.get_text().strip()
    elif span and "SHEET NUMBER" in span.get_text():
        sheet_number = div.get_text().strip()

print("Sheet Title:", sheet_title)
print("Sheet Number:", sheet_number)
