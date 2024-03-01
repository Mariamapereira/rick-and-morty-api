from flask import Flask, render_template, jsonify, request
import urllib.request, json

app = Flask(__name__)


# Endpoint para listar personagens
@app.route("/")
def root_function():
    return {
        "message": "Rick and Morty API is ready!",
        "url": "http://127.0.0.1:5000/characters",
    }


@app.route("/list")
def list_json():
    # Implementação para listar personagens

    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    return {"characters": dict["results"]}


# Endpoint para exibir lista de personagens
@app.route("/characters")
def list_characters():
    # Implementação para listar página principal de personagens
    page = request.args["page"] if len(request.args) > 0 else 1

    url = f"https://rickandmortyapi.com/api/character?page={page}"

    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    page = int(page)
    next_page = page + 1
    previous_page = page - 1

    return render_template(
        "characters.html",
        characters=dict["results"],
        page=page,
        next_page=next_page,
        previous_page=previous_page,
    )


# Endpoint para exibir perfil do personagem
@app.route("/character/<id>")
def character_profile(id):
    # Implementação para exibir perfil do personagem

    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    location_url = dict["location"]["url"]
    location_index = location_url[location_url.rfind("/") + 1 :]

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

    return render_template(
        "character.html", profile=dict, episodes=episodes, location_index=location_index
    )


# Endpoint para exibir lista de localizações
@app.route("/locations")
def list_locations():
    # Implementação para listar localizações

    page = request.args["page"] if len(request.args) > 0 else 1

    url = f"https://rickandmortyapi.com/api/location?page={page}"

    response = urllib.request.urlopen(url)
    location_data = response.read()
    dict = json.loads(location_data)

    page = int(page)
    next_page = page + 1
    previous_page = page - 1

    return render_template(
        "locations.html",
        locations=dict["results"],
        page=page,
        next_page=next_page,
        previous_page=previous_page,
    )


# Endpoint para exibir detalhes da localização
@app.route("/location/<id>")
def location_profile(id):

    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    residents = []

    for url_resident in dict["residents"]:
        print(url_resident)
        response = urllib.request.urlopen(url_resident)
        data = response.read()
        dict_residents = json.loads(data)
        resident = {
            "id": dict_residents["id"],
            "name": dict_residents["name"],
        }
        residents.append(resident)

    return render_template("location.html", location=dict, residents=residents)


# Endpoint para listar episódios
@app.route("/episodes")
def list_episodes():
    # Implementação para listar episódios
    page = request.args["page"] if len(request.args) > 0 else 1

    url = f"https://rickandmortyapi.com/api/episode?page={page}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    page = int(page)
    next_page = page + 1
    previous_page = page - 1

    return render_template(
        "episodes.html",
        episodes=dict["results"],
        page=page,
        next_page=next_page,
        previous_page=previous_page,
    )


# Endpoint para exibir perfil do episódio
@app.route("/episode/<id>")
def episode_profile(id):
    # Implementação para exibir perfil do episódio
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    characters = []

    for url_character in dict["characters"]:
        response = urllib.request.urlopen(url_character)
        data = response.read()
        dict_character = json.loads(data)
        character = {"id": dict_character["id"], "name": dict_character["name"]}
        characters.append(character)

    return render_template("episode.html", episode=dict, characters=characters)


if __name__ == "__main__":
    app.run(debug=True)
