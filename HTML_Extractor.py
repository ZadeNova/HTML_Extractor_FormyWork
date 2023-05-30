import bs4
import time
from bs4 import BeautifulSoup

URL = r""
file_Name = ".html"

soup = BeautifulSoup(open(f"{URL}\{file_Name}", encoding='utf-8'), 'html.parser')



# Remove table tags

table_Tags = soup.find_all('table',{'style':'border: none; background-color: transparent;'})
tbody_Tags = soup.find_all('tbody')
tr_Tags = soup.find_all('tr',{'style':'border: none;'})
td_Tags = soup.find_all('td',{'style':'padding: 0; padding-right: 32px; border: none;'})
td_Tags2 = soup.find_all('td',{'style':'width: 120px; border: none;'})
# Put in a list. Find all tables and get the last table. Last table is usually for author. Remove the table and replace it with div class = author
if len(table_Tags) == 0:
    print("Empty. No table")
else:
    table_Tags[-1].unwrap()
    tbody_Tags[-1].unwrap()
    tr_Tags[-1].unwrap()
    td_Tags[-1].unwrap()
    td_Tags2[-1].unwrap()

# Change all the h1/h2 tags to h3 tags

h1_tags = soup.find_all('h1')
h2_tags = soup.find_all('h2')

for h1_tag in h1_tags:
    h1_tag.name = 'h3'

for h2_tag in h2_tags:
    h2_tag.name = 'h3'

# Change a certain class to h6 tags.
special_P_Tags = soup.find_all('p',{'style':'font-weight: bold; letter-spacing: 1px;'})

for p_Tag in special_P_Tags:
    if 'style' in p_Tag.attrs:
        del p_Tag.attrs['style']
    if 'class' in p_Tag.attrs:
        del p_Tag.attrs['class']
    p_Tag.name = 'h6'



# Extract from main content div onwards.
start_div = soup.find('div', {'class':'rte'})

div_Contents = start_div.contents
extracted_HTML = []
extracted_HTML = div_Contents
#for important_content in div_Contents:
#    if important_content.name == 'div':
#        important_content.unwrap()
#        print(important_content)
        #important_content.div.unwrap()
        #extracted_HTML.append(important_content)

#extracted_HTML = [important_content for important_content in div_Contents]
# Remove all the spacings.
#thelist = [element for element in extracted_HTML if element.name != 'div']
#extracted_HTML = thelist


#for h1 in extracted_HTML:
#    print(f'{h1.name} {h1}')
#    if h1.name == "h1" or h1.name == 'h2':
#
#        print(h1)


# Removal of certain tag classes
classes_TobeRemoved = ['read-more','featured-item--overlay ethos-featured--overlay','featured-overlay ethos-overlay','featured-overlay__content','featured-overlay__text','featured-overlay__close','close extra-small-text','icon-close','ethos-featured-story','ethos-featured-story__content']

Cleaned_HTML = BeautifulSoup("".join(map(lambda x: str(x), extracted_HTML)), 'html.parser')
for class_name in classes_TobeRemoved:
    for div in Cleaned_HTML.find_all('div', {'class':class_name}):
        div.unwrap()

# Remove h4 tag
for h4_Tag in Cleaned_HTML.find_all('h4',{'class':'title'}):
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



