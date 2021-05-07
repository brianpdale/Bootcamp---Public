from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')
def dojo():
    return('Dojo!')
@app.route('/success')
def success():
    return "success"
@app.route('/say/hi/<name>')
def hello_name(name):
    print (name)
    return "Hi, " + str(name) + "!"
@app.route('/repeat/<num>/<word>')
def word_times(word, num):
    return (str(word) * int(num))
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.