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
## Unittests:
Para unittest:
```bash
pytest --cov=./ --cov-config=.coveragerc --cov-report=html --html=report.html
```
output:
  html_document:
    includes:
      body: report.html
