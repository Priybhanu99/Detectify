
function searchWeather(){
    fetch(`http://127.0.0.1:5000/uploader`).then(result => {
        console.log(result);
        return result.text();
    }).then(result => {
        init(result);
    }).catch( err =>{
        console.log(err)
    })
}

function init(resultFromServer){
    let detected=document.getElementById('detector');
    console.log(resultFromServer);
    detected.innerHTML='hello'+ resultFromServer;
}

searchWeather()