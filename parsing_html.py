#Testing understanding

from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")

for string in ["Name: ", "Favorite Color: "]:
    string_start_index = html_text.find(string)
    text_start_index = string_start_index + len(string)

    next_html_tag_offset = html_text[text_start_index:].find("<")
    text_end_index = text_start_index + next_html_tag_offset

    raw_text = html_text[text_start_index : text_end_index]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)