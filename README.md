# General purpose web-observer tool

A utility script to observe websites (hence, web-observer).

Define custom behavior for scraping uniform datasets from 
general web-pages which may be different from each other.

## Usage

Suppose the goal is to scrape several job boards for postings, 
where all the boards have vastly different HTML formatting.

Create a script `board_1.py` in the `observers` directory, 
and in that script, define a function with the `@observer(url)` decorator:
```python
from bs4 import BeautifulSoup
from common.observer import observer


# @observer("https://www.randomjobboard.com/careers")
def jobs(html):  
    # The function consumes the above URL's HTML as a string
    
    soup = BeautifulSoup(html, 'html.parser')  # Use something like BS4 to scrape
    
    main_div = soup.find(id='div_with_all_the_jobs')
    a_tags = main_div.find_all('a', recursive=True)
    
    # Whatever other logic you want
    
    return [{"title": child.text, "link": child['href']} for child in a_tags]
```
This can be repeated for as many different sites as you want, 
and each function decorated with `@observer(url)` will 
be called automatically from `main.py`.

Main functionality: wip
