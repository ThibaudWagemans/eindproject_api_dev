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
      <ul>
        <li>
          <a href="#back-end-api">back-end API</a>
        </li>
        <li>
          <a href="#front-end-api">front-end</a>
        </li>
        <li>
          <a href="#postman">Postman</a>
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

- het thema van mijn prject is grafische kaarten van NVIDIA
- zoals (bijna) elk jaar is NVIDIA (team green) weer met een nieuwe reeks grafiscche kaarten uitgekomen
- het doel is een korte samenvatting te hebben van de speccificaties van de verscillende modellen en moest het zijn er ook nog toe te voegen of te verwijderen


## Methods
#GET
- ik heb 6 verschillende GET methodes
- GET GPUs: geeft de lijst van alles verschillende modellen
- Get GPUs/random: geeft een random GPU uit de lijst
- GET GPUs/ : geeft de specs van de ingegeve GPU
- GET GPUs/price/: geeft de naame en specs van de GPU die het dichtste bij de opgegeven prijs zit
- GET GPUs/memory: geeft de naame en specs van de GPU die het dichtste bij de opgegeven memory zit
- GET GPUs/memory: geeft de naame en specs van de GPU die het dichtste bij de opgegeven power zit

#POST
- hier heb ik gekozen voor een add functie, hier geef je een naam, memory, prijs en power op en deze nieuwe GPU word toegevoegd aan de lijst

#delete
- hier geef je de naam in van de GPU (uit de lijst) die je wilt verwijderen

#put
- hier geef je de naam van een GPU in waarvan je de waardes wilt aanpassen

# Algemene eisen & Documentatie (+65%) [Wat de leerling denk dat goed is gegaan]
## Algemeen

- [x] 1 API in een GitHub repository
- [x] 1 front-end in een GitHub repository
- [ ] Beschrijving van het gekozen thema, je API en je front-end + link naar hosted API, link naar front-end GitHub repository en link naar hosted front-end op GitHub README.md
- [ ] Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md
- [ ] Volledige OpenAPI docs screenshot(s) op GitHub README.md

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

- [ ] Stijlgeving op de front-end (+5%)
- [ ] Interactie van je API met een andere externe service, API of databank (+15%)
- [ ] Eigen inspiratie… (+?%)

# INFO

- <a href="https://github.com/ThibaudWagemans/basisproject_api_dev">Mijn GitHub repository voor de api</a>
- <a href="https://github.com/ThibaudWagemans/basisproject_front_end">Mijn GitHub repository voor de front-end</a>
- <a href="https://basisproject-service-thibaudwagemans.cloud.okteto.net">Mijn hosted API link</a>
- <a href="https://thibaudwagemans.github.io/basisproject_front_end/basisproject.html">Mijn front-end link</a>
