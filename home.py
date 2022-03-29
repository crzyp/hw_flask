from flask import Flask

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
    name = "Lisa"
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    list_items = ""
    for items in city_names:
        list_items += '<li>' + items + '</li>'
    return ('''
    <html>
        <body>
            <h1>Welcome ''' + name + '''</h1>
            <p><a href="https://www.google.com">not google</a></p>
            <ul>''' + list_items + '''
            </ul>
       </body>
    </html>''')

myapp_obj.run()
