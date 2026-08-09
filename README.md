# IPL Match API

A Flask-based REST API for exploring Indian Premier League match records from a CSV dataset.

## Overview

This project loads IPL match data from `ipl-matches.csv` and exposes endpoints to:

- List all teams in the dataset
- Compare two teams head-to-head
- Get the overall record for a single team

## Tech Stack

- Python
- Flask
- Pandas
- NumPy

## Project Structure

```text
.
|-- app.py
|-- ipl.py
|-- ipl-matches.csv
|-- calculation.ipynb
|-- README.md
`-- .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/prajapatisuraj17/IPL-Match-API.git
cd IPL-Match-API
```

Install dependencies:

```bash
pip install flask pandas numpy
```

## Run The API

```bash
python app.py
```

The API will run locally at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Returns a simple home response |
| GET | `/api/teams` | Returns all IPL teams |
| GET | `/api/teamvteam?team1=<team>&team2=<team>` | Returns head-to-head records between two teams |
| GET | `/api/allrecoed?team=<team>` | Returns the full record for one team |

## Example Requests

Get all teams:

```text
http://127.0.0.1:5000/api/teams
```

Compare two teams:

```text
http://127.0.0.1:5000/api/teamvteam?team1=Mumbai Indians&team2=Chennai Super Kings
```

Get one team's full record:

```text
http://127.0.0.1:5000/api/allrecoed?team=Mumbai Indians
```

## Notes

The endpoint `/api/allrecoed` follows the current route name used in `app.py`.
