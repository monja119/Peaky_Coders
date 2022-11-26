let page_title = document.getElementById('page-title');
let base = document.getElementById('base');
let domain = 'http://localhost:8000/'
let temoin = false;
let nothing = 0;

function url(content_id, url, title, arg){
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        // changing content
        let content =  document.getElementById(content_id);
        content.innerHTML = this.responseText;

        // changing page info
        history.pushState({}, null, domain + url);
        page_title.innerHTML = title;
    }

    // changing status if hand
    if(url === 'about'){
        if(counter % 2 === 0){
            url = 'about/?s=True';
        }else{
            url = 'about/?s=False';
        }
        counter ++;
    }
    xhttp.open('GET', domain + url);
    xhttp.send()
}

// restoring and initializing page url
if(base == null){
    window.location.href = domain;
}

function homepage(){
    window.location.href = domain;
}
function loop(content_id, url, title, temoin){
    do {
        let xhttp = new XMLHttpRequest();
        xhttp.onload = function () {
            // changing content
            let content = document.getElementById(content_id);
            content.innerHTML = this.responseText;

            // changing page info
            history.pushState({}, null, domain + url);
            page_title.innerHTML = title;
        }
        xhttp.open('GET', domain + url);
        xhttp.send()
    } while(temoin === true);
}


