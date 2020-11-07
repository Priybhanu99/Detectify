
function malware_detector(){
    fetch(`http://127.0.0.1:5000/uploader`).then(result => {
        // console.log(result);
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
        let flag=false;
        for(ele in data.scans){
            console.log(data.scans[ele].detected);
            var div = document.createElement("div");
            var div1 = document.createElement("div1");
            div1.innerHTML = 'Malware Found  : ';
            if(data.scans[ele].detected===true){
                if(cnt==0){
                    detected.appendChild(div1);
                }
                flag=true;
                cnt+=1;
                div.innerHTML =  cnt + ' : Malware Found : ' + data.scans[ele].result;
                detected.appendChild(div);
            }
        }
        if(flag==false){
            detected.innerHTML='NOT MALICIOUS';
        }else{
            var div1 = document.createElement("div");
            var div2 = document.createElement("div");
            var div3 = document.createElement("div");
            var div4 = document.createElement("div");
            var div5 = document.createElement("div");
            div5.innerHTML='<br />';
            detected.appendChild(div5);
            var hash= 'Hashes are : '
            div1.innerHTML= hash;
            detected.appendChild(div1);
            div2.innerHTML = '1 : Hash md5 : ' + data.md5;
            detected.appendChild(div2);
            div3.innerHTML = '2 : Hash sha1 : ' + data.sha1;
            detected.appendChild(div3);
            div4.innerHTML = '3 : Hash sha256 : ' + data.sha256;
            detected.appendChild(div4);
        }
    }else{
        detected.innerHTML='No download in progress';
    }
    
}

malware_detector()