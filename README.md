## Heroku
[[https://heroku.com/deploy?template=https://github.com/erickrribeiro/chatbot/tree/master][file:https://www.herokucdn.com/deploy/button.svg]]

# Requirement
```
pip install PyPDF2
pip install rasa

```

## Start telegram
rasa run --port 5001 --credentials credentials.yml --endpoints endpoints.yml --debug
