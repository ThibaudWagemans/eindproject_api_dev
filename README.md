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
          <ul>
             <li><a href="#Get-list-all-GPUs-back-end">Get list all GPUs</li>
             <li><a href="#Get-random-GPU-back-end">Get random GPU</li>
             <li><a href="#Get-GPU-by-name-back-end">Get GPU by name</li>
             <li><a href="#Get-GPU-by-price-back-end">Get GPU by price</li>
             <li><a href="#Get-GPU-by-memory-back-end">Get GPU by memory</li>
             <li><a href="#Get-GPU-by-power-back-end">Get GPU by power</li>
             <li><a href="#post/add-GPU-back-end">post/add GPU</li>
             <li><a href="#put/update-GPU-back-end">put/update GPU</li>
             <li><a href="#delete-GPU-back-end">delete GPU</li>
          </ul>
        </li>
        <li>
          <a href="#front-end-api">front-end</a>
          <ul>
             <li><a href="#Get-list-all-GPUs">Get list all GPUs</li>
             <li><a href="#Get-random-GPU">Get random GPU</li>
             <li><a href="#Get-GPU-by-name">Get GPU by name</li>
             <li><a href="#Get-GPU-by-price">Get GPU by price</li>
             <li><a href="#Get-GPU-by-memory">Get GPU by memory</li>
             <li><a href="#Get-GPU-by-power">Get GPU by power</li>
             <li><a href="#post/add-GPU">post/add GPU</li>
             <li><a href="#put/update-GPU">put/update GPU</li>
             <li><a href="#delete-GPU">delete GPU</li>
          </ul>
        </li>
      </ul>
    </li>
    <li>
      <a href="#postman">Postman</a>
      <ul>
             <li><a href="#Get-list-all-GPUs">Get list all GPUs</li>
             <li><a href="#Get-random-GPU">Get random GPU</li>
             <li><a href="#Get-GPU-by-name">Get GPU by name</li>
             <li><a href="#Get-GPU-by-price">Get GPU by price</li>
             <li><a href="#Get-GPU-by-memory">Get GPU by memory</li>
             <li><a href="#Get-GPU-by-power">Get GPU by power</li>
             <li><a href="#post/add-GPU">post/add GPU</li>
             <li><a href="#put/update-GPU">put/update GPU</li>
             <li><a href="#delete-GPU">delete GPU</li>
          </ul>
    </li>
  </ol>
</details>


<!-- Over dit project -->
## Over dit project

Ik heb voor het thema GPUs gekozen omdat ik dit interessant vind en dat ik hier wel enkele dingen mee kon verzinnen.


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

