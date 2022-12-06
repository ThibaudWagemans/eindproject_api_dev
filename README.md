<!--titel  -->
<div align="center">
  <h1 align="center">basisproject_api_dev</h1>

  <p align="center">
    Gemaakt door Thibaud Wagemans
    <br />
    <a href="https://thibaudwagemans.github.io/basisproject_front_end/basisproject.html"><strong>link live front-end»</strong></a>
    <br />
    <br />
    <a href="https://github.com/ThibaudWagemans/basisproject_front_end">github Front-end repo</a>
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

![image](https://user-images.githubusercontent.com/57669221/202906070-31ac84d5-94e6-4df2-a485-7cfaef0b2e17.png)
![image](https://user-images.githubusercontent.com/57669221/202906250-b18034c3-97ac-434a-8063-46a412333067.png)
![image](https://user-images.githubusercontent.com/57669221/202906280-019872a6-9885-4c8d-9bbc-cc0e49b57199.png)
![image](https://user-images.githubusercontent.com/57669221/202906305-4e670bb9-910c-428e-bc8d-0a2f8ab9762a.png)
![image](https://user-images.githubusercontent.com/57669221/202906343-0d745782-907b-4d4e-b0d6-1e255991a3ce.png)
![image](https://user-images.githubusercontent.com/57669221/202906389-c21ba7f4-2ed3-414e-afeb-20d9878e5eeb.png)
![image](https://user-images.githubusercontent.com/57669221/202906784-4e42ecfa-09e0-413e-9420-afc0373a5121.png)
![image](https://user-images.githubusercontent.com/57669221/202906772-b2b118d9-6058-40bf-bc29-f7ed367b1626.png)
![image](https://user-images.githubusercontent.com/57669221/202906840-b5bc3b17-cad6-43c8-9cc1-9f8ab5d1772c.png)
![image](https://user-images.githubusercontent.com/57669221/202906859-d3789912-e2d6-47f2-a692-37cc8a2138ad.png)
![image](https://user-images.githubusercontent.com/57669221/202906902-bd6ed202-6c49-4637-9f43-ed49709b248c.png)

## screenshot website

![image](https://user-images.githubusercontent.com/57669221/202907095-c14fb835-64fe-4762-b467-6e216b6546bd.png)




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
