To run the DIAL application locally please follow the further instructions

### Prerequisites
- [poetry](https://python-poetry.org/docs/)
- [docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)


### Installation
1. Clone the repository
```sh
git clone
```

2. Install dependencies
```sh
poetry install --no-root
```

3. Update `dial/config/config.json` with the actual values according to [this documentation](https://github.com/epam/ai-dial-core/blob/development/README.md)

4. Create `.env.chat` file with the following content
```sh
DIAL_API_KEY='YOUR_API_KEY' # should be the same as in the config.json
NEXTAUTH_SECRET='secret'
```

5. Create `.env.app` file with all required for your application variables

6. Create `.env.core` file with all required for your DIAL core variables
```sh
AZURE_OPENAI_ENDPOINT='AZURE_OPENAI_ENDPOINT'
AZURE_OPENAI_API_KEY='AZURE_OPENAI_API_KEY'

AZURE_DEPLOYMENT_OPENAI_35=gpt-35-turbo-16k
AZURE_DEPLOYMENT_OPENAI_4=gpt-4o
AZURE_DEPLOYMENT_EMBEDDING=text-embedding-ada-002
AZURE_OPENAI_API_VERSION=2024-02-01
```

Important:
These variables are used in /dial/config/config-template.json.
If you want to use another variable(s), update accordingly /tools/update-dial-config.sh script.

7. Run the application
```sh
docker-compose up
```


### Usage
Open the browser and go to `http://localhost:3000/`
Select the application to use and start the conversation

To customize response find the relevant code in `app/application/dial_application.py` and update it according to your needs
