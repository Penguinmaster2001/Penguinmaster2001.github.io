
import sys
import os



assembled_pages_dir = "./assembledPages/"

page_parts_dir = "./pageParts/"

snippets_dir = "./pageParts/snippets/"

insert_code = [ "<!-- ##",  "## -->" ]


snippet_code_html: dict = dict();



def assemble_pages():

    get_snippets()

    insert_snippets()



def get_snippets():
    global snippet_code_html

    for file in filter(lambda file: file.endswith('.html'), os.listdir(snippets_dir)):
        with open(f"{snippets_dir}{file}", 'r') as f:
            snippet_code_html[f"{insert_code[0]}{file[:-5]}{insert_code[1]}"] = f.read()




def insert_snippets():

    for file in filter(lambda file: file.endswith('.html'), os.listdir(page_parts_dir)):
        assembled_page = ""

        with open(f"{page_parts_dir}{file}", 'r') as f:

            for line in f.readlines():
                assembled_page += line
                for snippet_code in snippet_code_html.keys():
                    if line.find(snippet_code) >= 0:
                        assembled_page += snippet_code_html[snippet_code]
        
        with open(f"{assembled_pages_dir}{file[:-5]}.html", 'w') as f:
            f.write(assembled_page)



if __name__ == "__main__":

    assemble_pages()
