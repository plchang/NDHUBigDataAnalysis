# -*- coding: utf-8 -*-
"""Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GUIgqGo5nj9Fe0np43jFb_9X5LQAgTJF

大數據作業一

授課教師: 雍忠

範例程式

# 程式作業編輯區

Compute the total duration of the top 250 films.
123 hours 45 minutes
Note that the above is just an example of correct format, but
not a correct answer, while your program needs to compute
the correct answer.

Two tasks are required for the Python program:
a) Collect the data of the top 250 films and save into a csv file
(default name: “films250.csv”. The csv file includes rank,
name, year, duration, rating, and rate (or audience rating).
b) Calculate the total duration of all the top 250 movies. The
answer needs to be translated into correct x hours and y
minutes, and 0 £ y < 60.

Goal: Write a Python program to retrieve data from a
designated web page.
• Target web page:
https://www.imdb.com/chart/top/?ref_=nv_mv_250
"""

import requests # Ask from website
from bs4 import BeautifulSoup # Soup
import pandas as pd # plot
import logging
import re
import IPython

IPython.get_ipython().run_cell_magic('javascript', '', 'IPython.notebook.kernel.execute("IPython.notebook.config.NotebookApp.iopub_data_rate_limit = 1000000000000")')

IPython.get_ipython().run_cell_magic('javascript', '', 'IPython.notebook.kernel.execute("IPython.notebook.config.NotebookApp.rate_limit_window = 10")')

pip install html5lib

# Configure logging
logging.basicConfig(filename='my_log.log', level=logging.DEBUG)

# Define url
imbd_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

#Set headers.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send request to web page
response = requests.get(imbd_url, headers=headers)

# Send a log message
logging.debug(response)

"""Generate parse tree"""

# Reference: https://steam.oxxostudio.tw/category/python/spider/beautiful-soup.html
# soup = BeautifulSoup(response.text, "html.parser")  # 轉換成標籤樹
soup = BeautifulSoup(response.text, "html5lib")
# print(soup.prettify())
# print(soup.find('div', class_='cli-title-metadata'))
title = soup.title                  # 取得 title
print(title)                      # 印出 title

# Parse the HTML content , "html.parser", parser to be used.

# Send a log message
logging.debug(response.content)

# Build new list to store data
movie_rank = []
movie_name = []
movie_year = []
movie_duration = []
movie_rating = []
movie_rate = []



rank = []
name_list = []

count = 0
# Loop through the movie entries and extract information
containers = soup.find_all("div", class_="ipc-page-content-container ipc-page-content-container--center sc-872d7ac7-0 fqEQWL", limit=251)  # container
i = 0
for container in containers:
  print("container", container)
  for rankName_elem in container.select("h3", class_="ipc-title__text", limit=251):
    if rankName_elem and i != 0 and i <= 251:
      rankName = rankName_elem.text.split()
      print("rankName", rankName)

      print(type(rankName[0]))

      rank = rankName[0].strip(".")
      print("rank ", rank)
      movie_rank.append(rank)
      rank = []

      name_list = ' '.join(rankName[1:])
      print("name_list", name_list)
      movie_name.append(name_list)
      name_list = []
    i = i + 1
  for rate_elem in container.select("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"):
    j = 0
    if rate_elem and j < 250:
      # Check if the span element has the aria-label attribute
      rate = rate_elem.get("aria-label")
      if rate:
        rateList = rate

        # Use regular expression to find the numerical value
        rating_match = re.search(r'\d+\.\d+', rate)

        # Check if a match is found and extract the rating
        if rating_match:
          imdb_rating = str(rating_match.group())
          movie_rate.append(imdb_rating)

      j = j + 1
  count = count + 1
  print("count = ", count)

print(movie_rank)
print(movie_name)
print(movie_year)
print(movie_duration)
print(movie_rating)
print(movie_rate)





print(movie_rank)
print(movie_name)
print(movie_rate)

# Find the div containing the metadata
metadata_elems = container.find_all('div', class_='sc-479faa3c-7 jXgjdT cli-title-metadata')

for metadata_elem in metadata_elems[:250]:
  print("Entering loop for metadata_elem:", metadata_elem)
  # Check if the metadata div is found
  if metadata_elem:
    # Find all spans within the metadata div
    metadata_items = metadata_elem.find_all('span', class_='sc-479faa3c-8 bNrEFi cli-title-metadata-item')
    print(metadata_items)
    # Check if at least three spans are found
    if len(metadata_items) == 3:
      # Extract year, duration, and rating
      year = metadata_items[0].text.strip()
      duration = metadata_items[1].text.strip()
      rating = metadata_items[2].text.strip()
      # Append these values to corresponding lists


      print(f"Year: {year}, Duration: {duration}, Rating: {rating}")
    elif len(metadata_items) == 2:
      if "m" in metadata_items[0] or "h" in metadata_items[0]:
        year = "NAN"
        duration = metadata_items[0].text.strip()
        rating = metadata_items[1].text.strip()
      elif "m" in metadata_items[1] or "h" in metadata_items[1]:
        year = metadata_items[0].text.strip()
        duration = metadata_items[1].text.strip()
        rating = "NAN"
      else:
        year = metadata_items[0].text.strip()
        duration = "NAN"
        rating = metadata_items[1].text.strip()

    elif len(metadata_items) == 1:
      if "m" in metadata_items[0] or "h" in metadata_items[0]:
        year = "NAN"
        duration = metadata_items[0].text.strip()
        rating = "NAN"
      elif len(metadata_items[0]) == 4:
        year = metadata_items[0].text.strip()
        duration = "NAN"
        rating = "NAN"
      else:
        year = "NAN"
        duration = "NAN"
        rating = metadata_items[0].text.strip()
    else:
      year = "NAN"
      duration = "NAN"
      rating = "NAN"
  else:
    year = "NAN"
    duration = "NAN"
    rating = "NAN"
  movie_year.append(year)
  movie_duration.append(duration)
  movie_rating.append(rating)



print(movie_year)
print(movie_duration)
print(movie_rating)





# Ensure all lists have the same length
max_len = max(len(movie_rank), len(movie_name), len(movie_year), len(movie_duration), len(movie_rating), len(movie_rate))
print("max_len", max_len)
movie_rank = movie_rank[:max_len]
movie_name = movie_name[:max_len]
movie_year = movie_year[:max_len]
movie_duration = movie_duration[:max_len]
movie_rating = movie_rating[:max_len]
movie_rate = movie_rate[:max_len]

print(len(movie_rank))
print(len(movie_name))
print(len(movie_year))
print(len(movie_duration))
print(len(movie_rating))
print(len(movie_rate))

# Create a DataFrame directly
movie_data = pd.DataFrame({
    'Rank': movie_rank,
    'Name': movie_name,
    'Year': movie_year,
    'Duration': movie_duration,
    'Rating': movie_rating,
    'Rate': movie_rate
})

# Save it as a CSV file
movie_data.to_csv('films250.csv', index=False)

total_min = 0
for i, duration in enumerate(movie_duration):

  print(duration)

  durations = duration.split()
  print(len(durations))
  if len(durations) >= 2:

    hour = durations[0].strip("h ")
    min = durations[1].strip("m")

    total_min = total_min + (int(hour) * 60) + int(min)
  else:
    if "m" in durations[0]:
      print(durations[0].strip("m"))
      print(type(durations[0].strip("m")))
      min = durations[0].strip("m")
      total_min = total_min + int(min)
    elif "h" in durations[0]:
      print(durations[0].strip("h"))
      print(type(durations[0].strip("h")))
      hour = durations[0].strip("h")
      total_min = total_min + (int(hour) * 60)



print("total_min", total_min)

total_hours = total_min // 60
total_minutes = total_min % 60

print(f"Total duration of the top 250 films: {total_hours} hours {total_minutes} minutes")





"""# Reference

- https://abdulrwahab.medium.com/how-to-build-a-python-web-scraper-to-capture-imdb-top-100-movies-908bf9b6bc19

- BeautifulSoup https://steam.oxxostudio.tw/category/python/spider/beautiful-soup.html

- https://hackmd.io/@aaronlife/python-topic-beautifulsoup

- https://steam.oxxostudio.tw/category/python/spider/beautiful-soup.html#a5

- https://www.learncodewithmike.com/2020/02/python-beautifulsoup-web-scraper.html

- https://www.educative.io/answers/how-to-use-beautiful-soups-findall-method

- https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id19

- Web develope https://developer.mozilla.org/zh-TW/docs/Learn/Getting_started_with_the_web/HTML_basics

- https://developer.chrome.com/blog/inside-browser-part3/

- WAI-ARIA https://www.w3.org/TR/wai-aria/#aria-label

- regular-expressions https://developers.google.com/edu/python/regular-expressions?hl=zh-tw
"""

# 取得屬性值
# 範例 https://www.learncodewithmike.com/2020/02/python-beautifulsoup-web-scraper.html

# 利用find_all()方法搜尋網頁中所有<h3>標籤且itemprop屬性值為headline的節點，接著，透過for迴圈讀取串列(List)中的節點，由於<h3>標籤底下只有一個<a>標籤，所以可以利用BeautifulSoup套件的select_one()方法進行選取
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a"))

# 利用get()方法(Method)取得href屬性值中的網址
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").get("href"))

markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

soup.get_text()
u'\nI linked to example.com\n'
soup.i.get_text()
u'example.com'

"""測試區

"""

texts = []
for element in soup.select("li"): # loop through the list of elements and append each text item to a list.
    texts.append(element.get_text())

# Use .find_all() and index into the list:

spans = div.find_all('span', class_='myclass')
first_span = spans[0]
second_span = spans[1]
third_span = spans[2]

double_string_list = [['d', 'o', 'g'], ['c', 'a', 't']]

word_list = [''.join(inner_list) for inner_list in double_string_list]

print(word_list)

original_list = ['a', 'n', 't']

combined_string = ''.join(original_list)

print(combined_string)

new_list = [combined_string]

print(new_list)

original_list = [['a', 'n', 't'], ['c', 'a', 't']]

combined_list = [[''.join(sublist)] for sublist in original_list]

print(combined_list)

original_list = ['The', 'Sound', 'of', 'Music']

combined_string = ' '.join(original_list)

result_list = [combined_string]

print(result_list)

import re

original_list = ['IMDb rating: 9.3']

# Use regular expression to find the numerical value
rating_match = re.search(r'\d+\.\d+', original_list[0])

# Check if a match is found and extract the rating
if rating_match:
    imdb_rating = float(rating_match.group())
    result_list = [imdb_rating]
    print(result_list)
else:
    print("No IMDb rating found.")

try:
    duration = yearDurationRatingRate_elem[1].text.strip()
except IndexError:
    print("No element at index 1")
    duration = None

div = soup.find('div', class_='cli-title-metadata')

# Get all spans
spans = div.find_all('span')

# Or select by the class
spans = div.select('span.cli-title-metadata-item')

# Print number of spans
print(len(spans))

# Extract text from first span
print(spans[0].text)

if spans:

  for span in spans:
    try:
      last_year = None

      year = span.text
      # Rest of year logic

    except IndexError:
       year = None

    try:
      last_duration = None
      duration_span = spans[i+1]
      duration = duration_span.text
      # Duration logic

    except IndexError:
      duration = None