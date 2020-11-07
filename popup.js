
function searchWeather(){
    fetch(`http://127.0.0.1:5000/uploader`).then(result => {
        console.log(result);
        return result.json();
    }).then(result => {
        init(result);
    }).catch( err =>{
        console.log(err)
    })
}

function init(data){
    let detected=document.getElementById('detector');
    console.log(data);
    // detected.innerHTML='Not malicious';
    if(data!==null){
        console.log(data.scans);
        var cnt=0;
        for(ele in data.scans){
            console.log(data.scans[ele].detected);
            var div = document.createElement("div");
            // div.innerHTML = 'Malware Found  : ';
            if(data.scans[ele].detected===true){
                cnt+=1;
                div.innerHTML =  cnt + ': Malware Found : ' + data.scans[ele].result;
                detected.appendChild(div);
            }
        }
    }else{
        detected.innerHTML='No new file detected';
    }
    
}

searchWeather()