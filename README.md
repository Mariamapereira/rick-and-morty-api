# Projeto Rick & Morty Guide

Desenvolvimento de API, utilizando Flask, que faz o consumo da API de terceiros Rick and Morty API, e apresenta para o usuário de forma mais amigável e organizada.

**API de terceiro utilizada:** https://rickandmortyapi.com/api/<br>
Endpoints consultadas: **/character, /location, /episode**


## Funcionalidades:


*   Listar personagens
*   Listar localizações
*   Listar episódios
*   Perfil de personagem
*   Detalhes da localização
*   Detalhes do episódio


<br>

## Organização da Squad

Foi criado o repositório no GitHub, ao qual foi atrelado um Project Kanban, onde foram disponibilizadas as Issues, que foram escolhidas pelos membros da equipe para desenvolvimento e pull request.

Repositório: https://github.com/pestanafj/rick-and-morty-api/

Também foram realizadas reuniões organizacionais pelo Discord, onde ficou decidido coletivamente as representantes para a apresentação

## Listar personagens

``/characters``

Retorna página apresentando cards com a fotos e nomes dos personagens da série

#### Listar personagens por página

``/characters/page/<page>``
## Listar Episódios
``/episodes``

Retorna página apresentando cards com os episódios da série

#### Listar Episódios por Página
``/episodes/page/<page>``

## Listar Localizações
``/locations``
Retorna página apresentando cards com as localizações da série

#### Listar Localizações por Página
``/locations/page/<page>``

## Perfil do Personagem
``/character/<id>``

Retorna página apresentando o perfil do personagem, contendo as informações de nome, espécie, status (vivo ou morto), origem, local de residência e episódios em que aparece.

## Detalhes do Episódio
``/episode/<id>``

Retorna página apresentando detalhes do episódio, contendo as informações de nome, código, data da exibição e personagens que aparecem nele.

## Detalhes da Localização
``/location/<id>``

Retorna página apresentando detalhes da localização, contendo as informações de nome, tipo, dimensão e residentes.


