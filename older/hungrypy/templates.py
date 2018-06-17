import os #Operating System- this allows python, linux and windows to play nicely together

def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path) #getcwd == "get current working directory"
    if not os.path.isfile(file_path):  #checks for valid path
        raise Exception("This is not a valid template path. %s"%(file_path))
    return file_path


def get_template(path): # method to open the file and read the contents
    file_path = get_template_path(path)
    return open(file_path).read()
file_ = "templates/email_messages.txt"


def render_context(template_string, context): #context will be a dictionary
    return template_string.format(**context) #** means format the string based on a dictionary
file_ = "templates/email_messages.txt"
file_html = "templates/email_messages.html"
template = get_template(file_)
template_html = get_template(file_html)
context = {
    "name": "Larry",
    "date": None,
    "total": None,
}
print(render_context(template, context))
print(render_context(template_html, context))


#better way to do line below is the render_context method above
#template_text = get_template(file_).format(name="Larry", date="abc", total=None) #string substution for "name" in the file


"""
/abc/ad/file.txt  this is a mac path
\hi\this\is\a\file.txt  this is a windows path
open("\hi\this\is\a\file.txt").read()
open(/abc/ad/file.txt).read()
"""
# os.path.join()  #this will make a path system agnostic