#Ish Kwatra
#RA2011026010345
import re

def compile_markdown(markdown_string):

    # Convert headers

    markdown_string = re.sub(r'^# (.*)$', r'<h1>\1</h1>',

                             markdown_string, flags=re.MULTILINE)

    markdown_string = re.sub(r'^## (.*)$', r'<h2>\1</h2>',

                             markdown_string, flags=re.MULTILINE)

    markdown_string = re.sub(

        r'^### (.*)$', r'<h3>\1</h3>', markdown_string, flags=re.MULTILINE)

    markdown_string = re.sub(

        r'^#### (.*)$', r'<h4>\1</h4>', markdown_string, flags=re.MULTILINE)

    markdown_string = re.sub(

        r'^##### (.*)$', r'<h5>\1</h5>', markdown_string, flags=re.MULTILINE)

    markdown_string = re.sub(

        r'^###### (.*)$', r'<h6>\1</h6>', markdown_string, flags=re.MULTILINE)

    # Convert bold and italic text

    markdown_string = re.sub(

        r'\*\*(.*)\*\*', r'<strong>\1</strong>', markdown_string)

    markdown_string = re.sub(

        r'__(.*)__', r'<strong>\1</strong>', markdown_string)

    markdown_string = re.sub(r'\*(.*)\*', r'<em>\1</em>', markdown_string)

    markdown_string = re.sub(r'_(.*)_', r'<em>\1</em>', markdown_string)

    # Convert links

    markdown_string = re.sub(

        r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', markdown_string)

    # Convert images

    markdown_string = re.sub(

        r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1">', markdown_string)

    # Convert paragraphs

    markdown_string = re.sub(

        r'^([^\n].*)\n\n', r'<p>\1</p>\n', markdown_string, flags=re.MULTILINE)

    return markdown_string

markdown_string = "# Hello, world!\n\nThis is some **bold** and *italic* text.\n\n[Here's a link](https://www.example.com).\n\nAnd here's an image: ![Alt text](https://www.example.com/image.jpg)"

html_string = compile_markdown(markdown_string)

print()

print(html_string)

print()

