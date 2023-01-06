<!--titel  -->
<div align="center">
  <h1 align="center">basisproject_api_dev</h1>

  <p align="center">
    Gemaakt door Thibaud Wagemans
    <br />
    <a href="https://thibaudwagemans.github.io/eindproject_front_end/"><strong>link live front-end»</strong></a>
    <br />
    <br />
    <a href="https://github.com/ThibaudWagemans/eindproject_front_end.git">github Front-end repo</a>
    ·
    <a href="https://basisproject-service-thibaudwagemans.cloud.okteto.net/docs">API docs (get,post,delete,put)</a>
  </p>
</div>

<!-- Inhoudstafel -->
<details>
  <summary>Inhoudstafel</summary>
  <ol>
    <li>
      <a href="#over-dit-project">Over dit project</a>
    </li>
    <li>
     <a href="#methods">methods</a>
      <ul>
        <li>
          <a href="#GET">GET</a>
        </li>
        <li>
          <a href="#POST">POST</a>
        </li>
        <li>
          <a href="#delete">delete</a>
        </li>
        <li>
          <a href="#put">put</a>
        </li>
      </ul>
    </li>
    <li>
     <a href="#algemeen">algemen eisen</a>
    </li>
    <li>
     <a href="#INFO">mijn INFO</a>
    </li>
  </ol>
</details>

<!-- Over dit project -->
## Over dit project

- het thema van mijn project is grafische kaarten van NVIDIA
- zoals (bijna) elk jaar is NVIDIA (team green) weer met een nieuwe reeks grafische kaarten uitgekomen
- het doel is een korte samenvatting te hebben van de specificaties van de verschillende modellen en moest het zijn er ook nog toe te voegen, aan te passen of     verwijderen (en de mogelijkheid te hebben een GPU te zoeken op bepaalde eigenschappen)


# Methods
## GET
- ik heb 6 verschillende GET methodes
- GET GPUs : geeft de lijst van alles verschillende modellen
- Get GPUs/random : geeft een random GPU uit de lijst
- GET GPUs/ :geeft de specs van de ingegeve GPU (naam)
- GET GPUs/price/ : geeft de naam en specs van de GPU die het dichtste bij de opgegeven prijs zit
- GET GPUs/memory/ : geeft de naam en specs van de GPU die het dichtste bij de opgegeven memory zit
- GET GPUs/power/ : geeft de naam en specs van de GPU die het dichtste bij de opgegeven power zit

## POST
- POST add/: hier heb ik gekozen voor een add functie, hier geef je een naam, memory, prijs en power op en deze nieuwe GPU word toegevoegd aan de lijst

## DELETE
- DELETE delete/: hier geef je de naam in van de GPU (uit de lijst) die je wilt verwijderen

## PUT
- PUT update/: hier geef je de naam van een GPU in waarvan je de waardes wilt aanpassen

## screenshots postman

![image](https://user-images.githubusercontent.com/57669221/202907010-beeb89f4-c04b-4045-aafa-46b8b7fa7999.png)
![image](https://user-images.githubusercontent.com/57669221/202907137-f8ac55da-affa-46cf-aef2-ed52e6eb6d03.png)
![image](https://user-images.githubusercontent.com/57669221/202907179-3205d765-de83-442d-b914-c6e453cdc841.png)
![image](https://user-images.githubusercontent.com/57669221/202907216-7110848e-a3ba-4991-8212-42990ecad09e.png)
![image](https://user-images.githubusercontent.com/57669221/202907262-b5f84c7d-90c8-4b37-8ec2-b08a5bcfb1fc.png)
![image](https://user-images.githubusercontent.com/57669221/202907282-18ef7080-056a-4507-87d9-2ed572523c85.png)
![image](https://user-images.githubusercontent.com/57669221/202907321-22e373d2-3dac-41d6-94b2-683d282268b8.png)
![image](https://user-images.githubusercontent.com/57669221/202907351-bb1ff300-21e1-451d-b2b3-747c0d2e856e.png)
![image](https://user-images.githubusercontent.com/57669221/202907413-2a8c5342-86d3-4f0d-b3ad-7dc9ec884d7d.png)


## screenshots openAPI docs

![image](https://user-images.githubusercontent.com/57669221/211047799-9a5d11f9-a5cc-457f-a756-aef474b0b9e5.png)
![image](https://user-images.githubusercontent.com/57669221/202907095-c14fb835-64fe-4762-b467-6e216b6546bd.png)
![image](https://user-images.githubusercontent.com/57669221/211047835-ecf57a35-6572-414c-a660-4b61bb2b3cc0.png)
![image](https://user-images.githubusercontent.com/57669221/211047891-8c44697d-b502-4776-b084-542021f70e1a.png)
![image](https://user-images.githubusercontent.com/57669221/211048125-b28f8063-7ba1-430e-9bf2-9d04e6936158.png)
![image](https://user-images.githubusercontent.com/57669221/211048155-cc06306c-b371-477e-9208-00abf099bf87.png)

## screenshot website


# Algemene eisen & Documentatie (+65%) [Wat de leerling denk dat goed is gegaan]
## Algemeen

- [x] 1 API in een GitHub repository
- [x] 1 front-end in een GitHub repository
- [x] Beschrijving van het gekozen thema, je API en je front-end + link naar hosted API, link naar front-end GitHub repository en link naar hosted front-end op GitHub README.md
- [x] Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md
- [x] Volledige OpenAPI docs screenshot(s) op GitHub README.md

## REST API

- [x] Minstens 2 GET endpoints 
- [x] Minstens 1 POST endpoint met class(es)
- [ ] Maximaal gebruik van validaties. Gebruik van response model wanneer aangewezen.
- [x] Logisch gebruik van path parameters, query parameters en body

## Deploying 

- [x] Docker container voor de API, welke automatisch door GitHub Actions opgebouwd wordt
- [x] Deployment van de API container op Okteto Cloud via Docker Compose

## Front-end

- [x] Een simpele front-end, minstens op basis van AlpineJS
- [x] Deployment van de front-end

## Suggesties voor bijkomende componenten

- [x] Stijlgeving op de front-end (+5%)
- [ ] Interactie van je API met een andere externe service, API of databank (+15%)
- [x] Eigen inspiratie… (+?%) (extra functies zoals put, delete en add)

# INFO

- <a href="https://github.com/ThibaudWagemans/basisproject_api_dev">Mijn GitHub repository voor de api</a>
- <a href="https://github.com/ThibaudWagemans/basisproject_front_end">Mijn GitHub repository voor de front-end</a>
- <a href="https://basisproject-service-thibaudwagemans.cloud.okteto.net">Mijn hosted API link</a>
- <a href="https://thibaudwagemans.github.io/basisproject_front_end/basisproject.html">Mijn front-end link</a>
