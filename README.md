<!--titel  -->
<div align="center">
  <h1 align="center">basisproject_api_dev</h1>

  <p align="center">
    Gemaakt door Thibaud Wagemans
    <br />
    <a href="https://thibaudwagemans.github.io/eindproject_front_end/"><strong>link live front-end»</strong></a>
    <br />
    <br />
    <a href="https://github.com/ThibaudWagemans/eindproject_front_end">github Front-end repo</a>
    ·
    <a href="https://eindproject-service-thibaudwagemans.cloud.okteto.net/docs">API docs (get,post,delete,put)</a>
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
- ik heb 9 verschillende GET methodes
- GET / : geeft een test terug met "hello world"
- GET GPUs : geeft de lijst van alles verschillende modellen
- Get GPUs/random : geeft een random GPU uit de lijst
- GET GPU :geeft de specs van de ingegeve GPU (name)
- GET GPUs/price/ : geeft de naam en specs van de GPU die het dichtste bij de opgegeven prijs zit
- GET GPUs/memory/ : geeft de naam en specs van de GPU die het dichtste bij de opgegeven memory zit
- GET GPUs/power/ : geeft de naam en specs van de GPU die het dichtste bij de opgegeven power zit
- GET /users : geeft een lijst van alle users
- GET /releaseDates : geeft een lijst van alle releasedates

## POST
- POST /GPUs: hier heb ik gekozen voor een add functie, hier geef je een naam, memory, prijs en power op en deze nieuwe GPU word toegevoegd aan de lijst
- POST /createusers : hier voeg ik een user (met password) toe aan de tabel users
- POST /token : hier maak ik een acces token aan
- POST /createReleaseDate : hier voeg ik een naam van een gpu en de releasedate in de tabel releasedates

## DELETE
- DELETE delete_GPU/: hier geef je de naam in van de GPU (uit de lijst) die je wilt verwijderen
- DELETE /delete_user : verwijderd de ingegeven user (name)
- DELETE /delete_releaseDate/ : verwijderd de ingegeven releasedate

## PUT
- PUT update_GPU/: hier geef je de naam van een GPU in waarvan je de waardes wilt aanpassen

## screenshots postman

![image](https://user-images.githubusercontent.com/57669221/211053493-11fecef7-90a6-4c34-8ac0-ae4f5f0bedbb.png)
![image](https://user-images.githubusercontent.com/57669221/211048994-7babb1ec-e528-46bb-845d-51252a1ae95a.png)
![image](https://user-images.githubusercontent.com/57669221/211048934-bf49b8f9-31c9-4442-84c7-91b7ea1c90e4.png)
![image](https://user-images.githubusercontent.com/57669221/211053666-69afdd1c-0004-429f-8ce6-896f479457c4.png)
![image](https://user-images.githubusercontent.com/57669221/211049060-9a284c34-3b4e-4135-83e7-388666eb9321.png)
![image](https://user-images.githubusercontent.com/57669221/211049277-b782ad05-c24f-4fff-a159-5046f012b8ce.png)
![image](https://user-images.githubusercontent.com/57669221/211049595-056b6aa3-c2a8-4d03-8e31-706d829f5db7.png)
![image](https://user-images.githubusercontent.com/57669221/211049699-0c0c38e0-5321-4bd1-8583-35c1603e6f5b.png)
![image](https://user-images.githubusercontent.com/57669221/211049811-1a388b90-b638-47a6-a7e1-105a9effee14.png)
![image](https://user-images.githubusercontent.com/57669221/211051701-c984cfc4-6689-4b25-8066-0ab13024c77b.png)
![image](https://user-images.githubusercontent.com/57669221/211051938-e6b64908-ef1c-4ff1-8e17-e6de18eb4fa7.png)
![image](https://user-images.githubusercontent.com/57669221/211052120-c36918ab-b31e-42c8-8de5-0d4be4ccb710.png)
![image](https://user-images.githubusercontent.com/57669221/211052271-225a0e0d-0533-4afd-9243-33752cd8aab3.png)
![image](https://user-images.githubusercontent.com/57669221/211052454-83539a8a-0dff-4d26-9772-fedc642fcaf9.png)
![image](https://user-images.githubusercontent.com/57669221/211052646-f0d7d4c9-b491-4f9b-a3ca-2906f8c09d6a.png)
![image](https://user-images.githubusercontent.com/57669221/211052729-3253b4f4-6ae4-43d7-8fd4-ef66dce69d5f.png)
![image](https://user-images.githubusercontent.com/57669221/211052878-9a8c41b1-e384-4b35-8124-4e276a30708e.png)



## screenshots openAPI docs

![image](https://user-images.githubusercontent.com/57669221/211047799-9a5d11f9-a5cc-457f-a756-aef474b0b9e5.png)
![image](https://user-images.githubusercontent.com/57669221/202907095-c14fb835-64fe-4762-b467-6e216b6546bd.png)
![image](https://user-images.githubusercontent.com/57669221/211047835-ecf57a35-6572-414c-a660-4b61bb2b3cc0.png)
![image](https://user-images.githubusercontent.com/57669221/211047891-8c44697d-b502-4776-b084-542021f70e1a.png)
![image](https://user-images.githubusercontent.com/57669221/211048125-b28f8063-7ba1-430e-9bf2-9d04e6936158.png)
![image](https://user-images.githubusercontent.com/57669221/211048155-cc06306c-b371-477e-9208-00abf099bf87.png)

## screenshot website


# INFO

- <a href="https://github.com/ThibaudWagemans/eindproject_api_dev">Mijn GitHub repository voor de api</a>
- <a href="https://github.com/ThibaudWagemans/eindproject_front_end">Mijn GitHub repository voor de front-end</a>
- <a href="https://eindproject-service-thibaudwagemans.cloud.okteto.net/">Mijn hosted API link</a>
- <a href="https://thibaudwagemans.github.io/eindproject_front_end/">Mijn front-end link</a>
