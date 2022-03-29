from flask import Flask

myapp_obj = Flask(__name__)
name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myapp_obj.route("/")
def home():
    list_items = ""
    for items in city_names:
        list_items += '<li>' + items + '</li>'
    return ('''
    <html>
        <body>
            <h1>Welcome ''' + name + '''!</h1>
            <p><a href="www.google.com">not google</a></p>
            <ul>''' + list_items + '''
            </ul>
       </body>
    </html>''')

#myapp_obj.run()
