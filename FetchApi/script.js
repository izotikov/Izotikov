function sendRequest() {
    let userTyped = document.querySelector('input').value;
    userTyped = userTyped.toLowerCase();
    userTyped = userTyped.replace(/\s/g, '+');
    let url = 'https://google-search3.p.rapidapi.com/api/v1/search/q=' + userTyped + '&num=10&lr=lang_en&hl=en&cr=US';
    fetch(url, {
        "method": "GET",
        "headers": {
            "x-user-agent": "desktop",
            "x-rapidapi-host": "google-search3.p.rapidapi.com",
            "x-rapidapi-key": "1fee90c522msh516c929d599e369p1bda98jsn2d764c96ab3b"
        }
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (json) {
            let res = document.getElementById('result');
            for (let i = 0; i< 3; i++) {
                let lnk = document.createElement('li');
                let a = document.createElement('a');
                a.textContent = json.results[i].title;
                a.href = json.results[i].link;
                lnk.append(a);
                res.append(lnk);
            }
        })
        .catch(err => {
            console.error(err);
        });
}