from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
@app.route('/playlists')  # added another route
def playlists():
    return render_template("playlists.html")


@app.route('/recommendations')  # recommendation
def recommendations():
    return render_template("recommendations.html")


app.run(host='0.0.0.0', port=8080)
