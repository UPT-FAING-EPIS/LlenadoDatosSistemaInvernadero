# Generar los reportes:
Despues de activar el venv y instalar los requirements:
## Cucumber:
```bash
behave --format=json.pretty -o report.json
```
Luego behave2cucumber para generar el cucumber.json
```bash
python -m behave2cucumber -i report.json -o cucumber.json
```
Descargar npm para usar cucumber-html-reporter:
```bash
npm install cucumber-html-reporter
```
Generar el html:
```bash
node -e "var reporter = require('cucumber-html-reporter');reporter.generate({theme: 'bootstrap', jsonFile: 'cucumber.json', output: 'cucumber_report.html', reportSuiteAsScenarios: true, scenarioTimestamp: true, launchReport: true});"
```
![image](https://github.com/UPT-FAING-EPIS/LlenadoDatosSistemaInvernadero/assets/102818449/6bec3432-0c39-44f9-b3df-e412903238ba)

## Unittests:
Para unittest:
```bash
pytest --cov=./ --cov-config=.coveragerc --cov-report=html --html=report.html
```
![image](https://github.com/UPT-FAING-EPIS/LlenadoDatosSistemaInvernadero/assets/102818449/edb5226a-bb3b-4d7f-bfc9-97d88518cbeb)

