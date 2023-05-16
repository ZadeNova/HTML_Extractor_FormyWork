import bs4
import time
from bs4 import BeautifulSoup

URL = r""

soup = BeautifulSoup(open(URL, encoding='utf-8'), 'html.parser')

# Extract from main content div onwards.
start_div = soup.find('div', {'class':'rte'})

div_Contents = start_div.contents
extracted_HTML = []

for important_content in div_Contents:
    if important_content.name == 'div':
        important_content.div.unwrap()
        #extracted_HTML.append(important_content)

extracted_HTML = [important_content for important_content in div_Contents]
# Remove all the spacings.
#thelist = [element for element in extracted_HTML if element.name != 'div']
#extracted_HTML = thelist

# Here is the space to edit the HTML. (Change/edit the HTML tags)
for h1 in extracted_HTML:
    if h1.name == "h1" or h1.name == 'h2':
        h1.name = 'h3'

# Removal of certain tag classes
classes_TobeRemoved = ['read-more','featured-item--overlay ethos-featured--overlay','featured-overlay ethos-overlay','featured-overlay__content','featured-overlay__text','featured-overlay__close','close extra-small-text','icon-close','ethos-featured-story','ethos-featured-story__content']

Cleaned_HTML = BeautifulSoup("".join(map(lambda x: str(x), extracted_HTML)), 'html.parser')
for class_name in classes_TobeRemoved:
    for div in Cleaned_HTML.find_all('div', {'class':class_name}):
        div.unwrap()

# Remove h4 tag
for h4_Tag in Cleaned_HTML.find_all('h4'):
    h4_Tag.decompose()

for span in Cleaned_HTML.find_all('span',{'class':'close extra-small-text'}):
    span.decompose()
for a_Tag in Cleaned_HTML.find_all('a',{'class':'read-more__link'}):
    a_Tag.decompose()

#for hr_Tags in Cleaned_HTML.find_all('hr'):
#    div_Tag = soup.new_tag('div',attrs={'class':'break'})
#    hr_Tags.replaceWith(div_Tag)

no_Spacing_HTML = []
for i in Cleaned_HTML:  #extracted_HTML
    no_Spacing_HTML.append(str(i).strip())







with open('output.txt','w' ,encoding='UTF-8') as file:
    for i in no_Spacing_HTML:
        file.write(i + '\n')



