"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['jerk','mean','ugly', 'terrible', 'fat', 'malicious']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Go to Hello Page</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
                    
        <br>
        <label>Choose your compliment: </label>
          <input type="radio" name="compliment" value="smart">
          <label>Smart</label>

          <input type="radio" name="compliment" value="pretty">
          <label>Pretty</label>

          <input type="radio" name="compliment" value="cute">
          <label>Cute</label>
          
          <br>
          <input type="submit" value="Submit">
        </form>
        <br>
        
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <br>
          Click to receive a random diss
          <button type="submit">Diss</button>
        </form>
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    random_diss = choice(INSULTS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {random_diss}!
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    chosen_compliment = request.args.get("compliment")

    random_compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {random_compliment} and {chosen_compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
