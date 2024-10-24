
import os



assembled_pages_dir = "./"

page_parts_dir = "./pageParts/"

snippets_dir = "./pageParts/snippets/"

insert_code = [ "<!-- ##",  "## -->" ]


page_html: dict = dict()
snippet_code_html: dict = dict()



def assemble_pages():

    get_pages()

    make_action_snippets()

    get_snippets()

    insert_snippets_into_pages()



def get_pages():
    global page_html

    for file in filter(lambda file: file.endswith('.html'), os.listdir(page_parts_dir)):
        with open(f"{page_parts_dir}{file}", 'r') as f:
            page_html[file] = f.read()

    



def make_action_snippets():
    global snippet_code_html
    
    navigation_snippet = "<div class=\"navigation\">\n"

    for page in page_html.keys():
        g = ""
        navigation_snippet += f"<a href=\"./{page}\">{page.removesuffix(".html").title()}</a>\n"

    navigation_snippet += "</div>\n"

    snippet_code_html[snippet_name_to_code("navigation")] = navigation_snippet



def get_snippets():
    global snippet_code_html

    for file in filter(lambda file: file.endswith('.html'), os.listdir(snippets_dir)):
        with open(f"{snippets_dir}{file}", 'r') as f:
            snippet_code_html[snippet_name_to_code(file.removesuffix(".html"))] = insert_snippets(f.read())



def snippet_name_to_code(snippet: str) -> str:
    return f"{insert_code[0]}{snippet}{insert_code[1]}"




def insert_snippets_into_pages():

    for page in page_html.keys():
        with open(f"{assembled_pages_dir}{page[:-5]}.html", 'w') as f:
            f.write(insert_snippets(page_html[page]))




def insert_snippets(template: str) -> str:
        
    assembled_page = template

    for snippet_code in snippet_code_html.keys():
        assembled_page = assembled_page.replace(snippet_code, snippet_code_html[snippet_code])

    return assembled_page





if __name__ == "__main__":

    assemble_pages()
