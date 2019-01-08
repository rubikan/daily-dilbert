# daily-dilbert

Small script to scrape the latest dilbert comic and send it via email

## Installation

To use this script you need Python and pipenv installed.

```bash
git clone https://github.com/Rubikan/daily-dilbert
cd daily-dilbert
pipenv install
cp example-config.json config.json
```

In the newly copied config.json file you can configure the mailserver and a list of recipients. The script assumes SMTP-over-SSL, everything else hasn't been tested and probably won't work.

Run the script via

```bash
pipenv run python daily-dilbert.py
```