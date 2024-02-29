from flask import Flask, render_template, jsonify
import urllib.request, json

page = 1

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


# Endpoint para exibir lista de personagens
@app.route("/characters/page/<page>")
def list_characters_page(page):
    # Implementação para listar página principal de personagens

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


# Endpoint para exibir lista de personagens
@app.route("/characters")
def list_characters():
    # Implementação para listar página principal de personagens
    return list_characters_page(1)


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
@app.route("/locations/page/<page>")
def list_locations_page(page):
    # Implementação para listar próxima página de localizações

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


# Endpoint para exibir lista de localizações
@app.route("/locations")
def list_locations():
    # Implementação para listar localizações
    return list_locations_page(1)


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
@app.route("/episodes/page/<page>")
def list_episodes_page(page):
    # Implementação para listar episódios

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


# Endpoint para listar episódios
@app.route("/episodes")
def list_episodes():
    # Implementação para listar episódios
    return list_episodes_page(1)


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
