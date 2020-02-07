from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response



@app.route("/table")
def fill_table():
  users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi', 'entry_number': '1'},
   {'first_name' : 'John', 'last_name' : 'Supsupin', 'entry_number': '2'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen', 'entry_number': '3'},
   {'first_name' : 'KB', 'last_name' : 'Tonel', 'entry_number': '4'}
  )

  return render_template("htmltable.html", users = users)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
