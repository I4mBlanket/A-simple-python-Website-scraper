import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import os
import sys

def headings_number():
    headings_count = 1
    for heading_count in range(1, 100):
      headings_count =+ 1

def get_user_selection():
    print("What do you want to extract from the website?")
    print("1. Links")
    print("2. Headings")
    print("3. Images")
    print("4. Paragraphs")
    print("5. Forms")
    print("6. Lists")
    print("7. Tables")
    print("8. Meta Tags")
    print("9. Scripts")
    print("10. Stylesheets")
    print("11. Divs")
    print("12. Spans")
    print("13. Buttons")
    print("14. Comments")
    print("15. Sections")
    print("16. Navbars")
    print("17. Footers")
    print("18. Logos")
    print("19. Icons")
    print("20. Captions")
    user_choice = input("Enter your choice (1-20): ")
    return user_choice

def extract_links(soup):
    links = soup.find_all('a')
    with open('links_output.txt', 'w') as f:
        for link in links:
            print(link.get('href'), file=f)

def extract_headings(soup):
    headings = soup.find_all(headings_number)
    with open('headings_output.txt', 'w') as f:
        for heading in headings:
            print(heading.text, file=f)

def extract_images(soup):
    images = soup.find_all('img')
    with open('images_output.txt', 'w') as f:
        for image in images:
            print(image.get('src'), file=f)

def extract_paragraphs(soup):
    paragraphs = soup.find_all('p')
    with open('paragraphs_output.txt', 'w') as f:
        for paragraph in paragraphs:
            print(paragraph.text, file=f)

def extract_forms(soup):
    forms = soup.find_all('form')
    with open('forms_output.txt', 'w') as f:
        for form in forms:
            print(form, file=f)

def extract_lists(soup):
    lists = soup.find_all(['ul', 'ol'])
    with open('lists_output.txt', 'w') as f:
        for listed_item in lists:
            print(listed_item, file=f)

def extract_tables(soup):
    tables = soup.find_all('table')
    with open('tables_output.txt', 'w') as f:
        for table in tables:
            print(table, file=f)

def extract_meta_tags(soup):
    meta_tags = soup.find_all('meta')
    with open('meta_tags_output.txt', 'w') as f:
        for meta_tag in meta_tags:
            print(meta_tag, file=f)

def extract_scripts(soup):
    scripts = soup.find_all('script')
    with open('scripts_output.txt', 'w') as f:
        for script in scripts:
            print(script, file=f)

def extract_stylesheets(soup):
    stylesheets = soup.find_all('link')
    with open('stylesheets_output.txt', 'w') as f:
        for stylesheet in stylesheets:
            if stylesheet.get('rel') == 'stylesheet':

             print(stylesheet.get('href'), file=f)

def extract_divs(soup):
    divs = soup.find_all('div')
    with open('divs_output.txt', 'w') as f:
        for div in divs:
            print(div, file=f)

def extract_spans(soup):
    spans = soup.find_all('span')
    with open('spans_output.txt', 'w') as f:
        for span in spans:
            print(span, file=f)

def extract_buttons(soup):
    buttons = soup.find_all('button')
    with open('buttons_output.txt', 'w') as f:
        for button in buttons:
            print(button, file=f)

def extract_comments(soup):
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    with open('comments_output.txt', 'w') as f:
        for comment in comments:
            print(comment, file=f)

def extract_sections(soup):
    sections = soup.find_all('section')
    with open('sections_output.txt', 'w') as f:
        for section in sections:
            print(section, file=f)

def extract_navbars(soup):
    navbars = soup.find_all(class_='navbar')
    with open('navbars_output.txt', 'w') as f:
        for navbar in navbars:
            print(navbar, file=f)

def extract_footers(soup):
    footers = soup.find_all('footer')
    with open('footers_output.txt', 'w') as f:
        for footer in footers:
            print(footer, file=f)

def extract_logos(soup):
    logos = soup.find_all(class_='logo')
    with open('logos_output.txt', 'w') as f:
        for logo in logos:
            print(logo, file=f)

def extract_icons(soup):
    icons = soup.find_all(class_='icon')
    with open('icons_output.txt', 'w') as f:
        for icon in icons:
            print(icon, file=f)

def extract_captions(soup):
    captions = soup.find_all('caption')
    with open('captions_output.txt', 'w') as f:
        for caption in captions:
            print(caption, file=f)

url = input("Enter the URL of the website you want to scrape: ")
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    choice = get_user_selection()

    if choice == '1':
        extract_links(soup)
    elif choice == '2':
        extract_headings(soup)
    elif choice == '3':
        extract_images(soup)
    elif choice == '4':
        extract_paragraphs(soup)
    elif choice == '5':
        extract_forms(soup)
    elif choice == '6':
        extract_lists(soup)
    elif choice == '7':
        extract_tables(soup)
    elif choice == '8':
        extract_meta_tags(soup)
    elif choice == '9':
        extract_scripts(soup)
    elif choice == '10':
        extract_stylesheets(soup)
    elif choice == '11':
        extract_divs(soup)
    elif choice == '12':
        extract_spans(soup)
    elif choice == '13':
        extract_buttons(soup)
    elif choice == '14':
        extract_comments(soup)
    elif choice == '15':
        extract_sections(soup)
    elif choice == '16':
        extract_navbars(soup)
    elif choice == '17':
        extract_footers(soup)
    elif choice == '18':
        extract_logos(soup)
    elif choice == '19':
        extract_icons(soup)
    elif choice == '20':
        extract_captions(soup)
    else:
        print("Invalid choice. Please select a valid option.")
else:
    print("Failed to retrieve the website. Status code:", response.status_code)
