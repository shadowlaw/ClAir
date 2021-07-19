# ClAir
ClAir, a decision support system that will use actionable environmental and civil data to drive decision making pertaining to public spaces to include parks, roadways, bus or taxi parks and government owned property. 

## Setup Steps
1. Clone the repository using the below command.
```shell
git clone git@github.com:shadowlaw/ClAir.git
```

2. Change your current working directory to the project root directory.
```shell
cd ClAir
```

3. Copy .env.example to .env using the below command and change the environment variables as needed.   
   Note: If using a sqlite database, make sure use the absolute path.
```shell
cp .env.example .env
```

4. create a virtual environment for the project in the project root directory and install the project requirements 

**Create virtual environment**
```shell
pip install virtualenv
virtualenv venv
```

**Activate virtual environment**
```shell
# windows using git bash
source venv/Scripts/activate

# windows cmd
venv/Scripts/activate

# linux
source venv/bin/activate
```
**Installing requirements**
```shell
pip install -r requirements.txt
```

5. Create the database tables using the below command
```shell
python flask-migrate.py db upgrade
```

6. Initialize the database
```shell
python intialize_db.py
```

## Running the project
To run the project, use the below command in a terminal with the activated virtual environment.
```shell
python run.py
```