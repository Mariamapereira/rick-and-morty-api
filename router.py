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


@app.route("/characters/page/<number_page>")
def list_characters_page(number_page):
    # Implementação para listar personagens

    global page
    page = number_page

    url = "https://rickandmortyapi.com/api/character?page=" + number_page

    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    return render_template("characters.html", characters=dict["results"], page=page)


@app.route("/characters/nextpage")
def list_characters_next_page():
    # Implementação para listar personagens

    global page
    page = page + 1

    print(f"Page={page}")

    url = f"https://rickandmortyapi.com/api/character?page={page}"

    print(url)

    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    return render_template("characters.html", characters=dict["results"], page=page)


@app.route("/characters/previouspage")
def list_characters_previous_page():
    # Implementação para listar personagens

    global page
    page -= 1

    url = f"https://rickandmortyapi.com/api/character?page={page}"

    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    return render_template("characters.html", characters=dict["results"], page=page)


@app.route("/characters")
def list_characters():
    # Implementação para listar personagens

    global page
    page = 1

    url = "https://rickandmortyapi.com/api/character"

    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    return render_template("characters.html", characters=dict["results"], page=page)


# Endpoint para exibir perfil do personagem
@app.route("/character/<id>")
def character_profile(id):
    # Implementação para exibir perfil do personagem

    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    episodes = []

    for url_episode in dict["episode"]:
        response = urllib.request.urlopen(url_episode)
        data = response.read()
        dict_episode = json.loads(data)
        episode = {
            "id": dict_episode["id"],
            "name": dict_episode["name"],
            "episode": dict_episode["episode"],
        }
        episodes.append(episode)

    return render_template("character.html", profile=dict, episodes=episodes)


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
