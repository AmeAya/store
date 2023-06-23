window.onload = function() {
    var div = document.getElementById('good_detail_div');
    var Request = new XMLHttpRequest();
    div.innerHTML = '';

    Request.onreadystatechange = function() {
        if (Request.readyState == 4) {
            var good = JSON.parse(Request.responseText)
            var nameHeader = document.createElement('h1');
            nameHeader.innerHTML = good.name;
            div.appendChild(nameHeader);
        }
    }

    var url = 'http://127.0.0.1:8000/good?' + window.location.search.substring(1);
    Request.open('get', url, true);
    Request.send(null);
}