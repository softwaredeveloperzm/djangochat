const input = document.getElementById('search');
const result = document.getElementById('results');

const addHtmlDomElement = (element, html) => {
    element.innerHTML = html;
}

const fetchResult = value => {
    if(value){
        const url = `/fetch_users/${value}/`;
        fetch(url, {
            method: "GET"
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            let html = '';

            for (let d of data){
                html += `<li class="list-group-item">

                   <a href="/user/${d.username}/">${d.username}</a>




                         </li>`;
                addHtmlDomElement(result, html);
            }
        })
        .catch(err => {
            console.log(err);
        });
    } else {
        addHtmlDomElement(result, '');
    }
}


input.onkeyup = () => fetchResult(input.value);
