# 👽 Projeto Rick & Morty Guide 👽

Desenvolvimento de API, utilizando Flask, que faz o consumo da API de terceiros Rick and Morty API, e apresenta para o usuário de forma mais amigável e organizada.

**API de terceiro utilizada:** https://rickandmortyapi.com/api/<br>
Endpoints consultadas: **/character, /location, /episode**


## ⚙️ Funcionalidades:


*   Listar personagens
*   Listar localizações
*   Listar episódios
*   Perfil de personagem
*   Detalhes da localização
*   Detalhes do episódio


<br><br>

## Organização da Squad

Foi criado o repositório no GitHub, ao qual foi atrelado um Project Kanban, onde foram disponibilizadas as Issues, que foram escolhidas pelos membros da equipe para desenvolvimento e pull request.

Repositório: https://github.com/pestanafj/rick-and-morty-api/

Também foram realizadas reuniões organizacionais pelo Discord, onde ficou decidido coletivamente as representantes para a apresentação
<br><br>

### Listar personagens
Rota: ``/characters``

Retorna página apresentando cards com a fotos e nomes dos personagens da série

#### Listar personagens por página

Rota: ``/characters/page/<page>``
<br><br>
### Listar Episódios
Rota: ``/episodes``

Retorna página apresentando cards com os episódios da série

#### Listar Episódios por Página
Rota: ``/episodes/page/<page>``
<br><br>
### Listar Localizações
Rota: ``/locations``
Retorna página apresentando cards com as localizações da série

#### Listar Localizações por Página
Rota: ``/locations/page/<page>``
<br><br>
### Perfil do Personagem
Rota: ``/character/<id>``

Retorna página apresentando o perfil do personagem, contendo as informações de nome, espécie, status (vivo ou morto), origem, local de residência e episódios em que aparece.
<br><br>
### Detalhes do Episódio
Rota: ``/episode/<id>``

Retorna página apresentando detalhes do episódio, contendo as informações de nome, código, data da exibição e personagens que aparecem nele.
<br><br>
### Detalhes da Localização
Rota: ``/location/<id>``

Retorna página apresentando detalhes da localização, contendo as informações de nome, tipo, dimensão e residentes.

<br><br>
## 👩🏻‍💻 Autoras
API criada em Fevereiro de 2024 durante Bootcamp WomakersCode Backend Python + Django
#### Squad Katherine Johnson
- Fernanda Pestana
- Amanda Paul
- Gleyce Alves
- Juliana Carvalho
- Heloísa Santos
- Carolina Mendes
- Lais Victoria
- Jataiza Barboza
- Maiara Santos
- Nicolle Sturzbecher
- Mariama Nascimento 



