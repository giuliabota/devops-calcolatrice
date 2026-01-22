# README

Questo codice contiene una semplice calcolatrice che esegue operazioni di:
- somma tra due numeri
- sottrazione tra due numeri
- moltiplicazione tra due numeri

Include anche test unitari per verificare il corretto funzionamento della funzione di somma.

## Requisiti

- Creare un ambiente virtuale
    - python3 -m venv .venv
    - rm -rf .venv
    - uv venv

- Attivare l'ambiente virtuale
    - source .venv/bin/activate     (Linux/Mac)
    - .venv\Scripts\activate    (Windows)

- Verifica che l'interprete sia quello giusto
    - which python  (Linux/Mac)
    - where python  (Windows)

- Installare le dipendenze
    - pip install pytest

    - pip install -r requirements.txt
    - uv pip compile requirements.in -o requirements.txt
    - source .venv/bin/activate && uv pip install -r docker/local/requirements.txt

## Esecuzione normale

python3 calcolatrice.py

## Esecuzione dei test

pytest test_calcolatrice.py

## Github upload

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/XXX/devops-calcolatrice.git
git push -u origin main
Docker build
docker build -f Dockerfile -t devops-calcolatrice:local .
docker run --rm -it devops-calcolatrice:local

## Docker Hub upload

Crea un repository su Docker Hub
Esempio: docker.io/<DOCKERHUB_USERNAME>/devops-calcolatrice

## Fare build immagine

giuliabota è il mio username su Docker Hub = <DOCKERHUB_USERNAME>

docker build -f Dockerfile -t  giuliabota/devops-calcolatrice:manuale .
.
## Fare il push dell'immagine

docker push giuliabota/devops-calcolatrice:manuale
Aggiungi i secret su GitHub
Nel repo GitHub → Settings → Secrets and variables → Actions → New repository secret

DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
👉 token generato da Docker Hub (Account Settings → Access Token)




