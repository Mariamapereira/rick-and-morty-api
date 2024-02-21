from flask import Flask, render_template, jsonify
import urllib.request, json

app = Flask(__name__)


# Endpoint para listar personagens
@app.route("/")
def root_function():
    return {"mensagem": "Tudo ok!"}


@app.route("/list")
def list_json():
    # Implementação para listar personagens

    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    return {"characters": dict["results"]}


@app.route("/characters")
def list_characters():
    # Implementação para listar personagens

    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    return render_template("characters.html", characters=dict["results"])


# Endpoint para exibir perfil do personagem
@app.route("/character/<id>")
def character_profile(id):
    # Implementação para exibir perfil do personagem

    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)


# Endpoint para listar localizações
@app.route("/locations")
def list_locations():
    # Implementação para listar localizações
    return render_template("templates\locations.html", locations=locations)


# Endpoint para exibir perfil da localização
@app.route("/location/<int:id>")
def location_profile(id):
    # Implementação para exibir perfil da localização
    return render_template("templates\location.html", location=location)


# Endpoint para listar episódios
@app.route("/episodes")
def list_episodes():
    # Implementação para listar episódios
    return render_template("templates\episodes.html", episodes=episodes)


# Endpoint para exibir perfil do episódio
@app.route("/episode/<int:id>")
def episode_profile(id):
    # Implementação para exibir perfil do episódio
    return render_template("templates\episode.html", episode=episode)


# if __name__ == '__main__':
#     app.run(debug=True)
