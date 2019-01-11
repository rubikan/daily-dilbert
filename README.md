# daily-dilbert

Small script to scrape the latest dilbert comic and send it via email or post it to a discord webhook

## Installation

To use this script you need Python and pipenv installed.

```bash
git clone https://github.com/Rubikan/daily-dilbert
cd daily-dilbert
pipenv install
cp example-config.json config.json
```

In the newly copied config.json file you can configure the mailserver including the recipients or the discord webhook. If you only want to use one of these, just omit the other section altogether.
The script assumes SMTP-over-SSL for mails, everything else hasn't been tested and probably won't work. Gmail is a good candidate, and was used in the testing process.

Run the script via

```bash
pipenv run python daily-dilbert.py
```