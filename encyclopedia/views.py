# all the comments are for me to navigate thru
# Import modules and functions to start
from . import util
from django.shortcuts import render
import markdown
import random

# Define function importing md to html 
def convert_md_to_html(title):
    # Get content for title
    content = util.get_entry(title)
    if content is None:
        return None
    else:
        # Create markdown object
        markdowner = markdown.Markdown()
        # Use the comvert md to convert
        return markdowner.convert(content)

# Define view for index page
def index(request):
    # Render index page with list
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Define a view to display the entryy
def entry(request, title):
    # Convert the md to html "md to html tool"
    html_content = convert_md_to_html(title)
    if html_content is None:
        # Render an error if it not exist
        return render(request, "encyclopedia/errr.html", {
            "message": "Entry doesn't exist"
        })
    else:
        # Render the entry page with title 
        return render(request, "encyclopedia/entryy.html", {
            "title": title,
            "content": html_content
        })

# Define search views
def search(request):
    # Initialize recomended list
    recommendation = []

    if request.method == "POST":
        entry_search = request.POST['q']
        # Convert to html html content md tool
        html_content = convert_md_to_html(entry_search)

        if html_content is not None:
            # Render with results
            return render(request, "encyclopedia/entryy.html", {
                "title": entry_search,
                "content": html_content
            })
        else:
            # create a list of many reccomendations if not found
            allEntries = util.list_entries()
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)

            # Render the search results or reccomend 
            return render(request, "encyclopedia/seaarch.html", {
                "recommendation": recommendation
            })

# Define a view to create new page
def new_page(request):
    if request.method == "GET":
        # Render the new form 
        return render(request, "encyclopedia/neww.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        title_exist = util.get_entry(title)
        if title_exist is not None:
            # Render an error page if its already existing
            return render(request, "encyclopedia/errr.html", {
                "message": "Entry already exists"
            })
        else:
            # Save the new entries and render new pages from it
            util.save_entry(title, content)
            html_content = convert_md_to_html(content)
            return render(request, "encyclopedia/neww.html", {
                "title": title,
                "content": html_content
            })

# Define a view for entry editingg
def edit(request):
    if request.method == 'POST':
        title = request.POST.get('entry_title', '') 
        content = util.get_entry(title)
        # Render the edit page with the title and content
        return render(request, "encyclopedia/edittt.html", {
            "title": title,
            "content": content
        })

# Define a view to save edited
def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        # Save the edited entry  and rndr new pages
        util.save_entry(title, content)
        html_content = convert_md_to_html(content)
        return render(request, "encyclopedia/neww.html", {
            "title": title,
            "content": html_content
        })

# Define a viewww
def rand(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = convert_md_to_html(rand_entry)
    # Rndr the random entry page with tiitle + its content
    return render(request, "encyclopedia/entryy.html", {
        "title": rand_entry,
        "content": html_content
    })
