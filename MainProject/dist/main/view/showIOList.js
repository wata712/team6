const outputElement = document.getElementById('output_csv');
var dataPath;
// dataPath = eel.sendIOcsvName()();

eel.expose(getIOcsvName)
function getIOcsvName(csvName){
    dataPath = csvName
}

eel.expose(getCsvData)
function getCsvData(dataPath) {
    const request = new XMLHttpRequest();
    request.addEventListener('load', (event) => {
        const response = event.target.responseText;
        convertArray(response);
    });
    console.log(dataPath);
    request.open('GET', dataPath, true);
    request.send();
}

function convertArray(data) {
    const dataArray = [];
    const dataString = data.split('n');
    for (let i = 0; i < dataString.length; i++) {
        dataAraString[i].split(',');
    }
    let insertElement = '';
    dataArray.forEach((element) => {
        insertElement += '<tr>';
        element.forEach((childElement) => {
            insertElement += `<td>${childElement}</td>`
        });
        insertElement += '</tr>';
    });
    outputElement.innerHTML = insertElement;
}

getCsvData('IOcsvName');

