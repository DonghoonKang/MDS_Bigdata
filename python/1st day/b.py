def makeHomePage(name, interest):
    file=open("homepage.html","wt")
    file.write("""<!DOCTYPE html>
    <html>
    <head>
    <title>"""+name+"""'s Home Page</title>
    </head>
    <body>
    <h1>Welcome to """+name+"""'s Home Page</h1>
    <p>Hi! I am """+name+""". This is my homepage.
    I am interested in """ +interest+""".</p>
    </body>
    </html>""")
    file.close()

makeHomePage("kevin","basketball")
import webbrowser
webbrowser.open("homepage.html")
