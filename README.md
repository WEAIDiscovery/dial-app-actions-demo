
# DIAL Application

To run the DIAL application locally, please follow the instructions below.

## Prerequisites

- [Poetry](https://python-poetry.org/docs/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

### Common Steps

1. **Clone the repository**
    ```sh
    git clone
    ```

2. **Install dependencies**
    ```sh
    poetry install --no-root --directory=app
    ```

3. **Create `.env.chat` file** 
    ```sh
    DIAL_API_KEY='YOUR_API_KEY' # Same as in the dial/config/config-template.json
    NEXTAUTH_SECRET='secret'
    DEFAULT_MODEL=gpt-35-turbo
    ```

4. **Create `.env.app` file** with the actual values according to [this documentation](https://github.com/epam/ai-dial-core/blob/development/README.md)

5. **Create `.env.core` file**
    ```sh
    AZURE_OPENAI_ENDPOINT='AZURE_OPENAI_ENDPOINT'
    AZURE_OPENAI_API_KEY='AZURE_OPENAI_API_KEY'

    AZURE_DEPLOYMENT_OPENAI_35=gpt-35-turbo-16k
    AZURE_DEPLOYMENT_OPENAI_4=gpt-4o
    AZURE_DEPLOYMENT_EMBEDDING=text-embedding-ada-002
    AZURE_OPENAI_API_VERSION=2024-02-01
    ```

   > **Important:** These variables are used in `/dial/config/config-template.json`. If you want to use other variables, update the `/tools/update-dial-config.sh` script accordingly.

### Running the Application

#### Without Colima

1. **Run the application**
    ```sh
    docker-compose up
    ```

#### With Colima

1. **Start Colima**
    ```sh
    colima start --arch x86_64 --memory 8 --cpu 4
    ```

2. **Run `init.sh` script**
    ```sh
    ./init.sh
    ```

3. **Run the application**
    ```sh
    docker-compose -f docker-compose-colima.yml up
    ```

4. **Wait for the application to start** (This may take some time)
    ```sh
    dial-app-1        | INFO:     Started server process [1]
    dial-app-1        | INFO:     Waiting for application startup.
    dial-app-1        | INFO:     Application startup complete.
    dial-app-1        | INFO:     Uvicorn running on http://0.0.0.0:5002 (Press CTRL+C to quit)
    ```

5. **Open the browser and go to `http://localhost:3000/`**


## Usage

1. **Open the browser and go to `http://localhost:3000/`**
2. Select the application to use and start the conversation.
3. To customize the response, find the relevant code in `app/application/dial_application.py` and update it according to your needs.

