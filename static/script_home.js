window.onload = function() {
    var Request = new XMLHttpRequest();
    var select = document.getElementById('select-categories');

    Request.onreadystatechange = function() {
        if (Request.readyState == 4) {
            var categories = JSON.parse(Request.responseText);
            for (var category of categories) {
                var option = document.createElement("option");
                option.text = category.name;
                option.value = category.id;
                select.add(option, null);
            }
        }
    }

    var url = 'http://127.0.0.1:8000/categories';
    Request.open('get', url, true);
    Request.send(null);
}

function loadGoods() {
    var Request = new XMLHttpRequest();
    var div = document.getElementById('div_goods');
    div.innerHTML = '';

    Request.onreadystatechange = function() {
        if (Request.readyState == 4) {
            for (var good of JSON.parse(Request.responseText)) {
                var p = document.createElement("p");
                p.textContent = good.name;
                div.appendChild(p);
            }
        }
    }

    var select = document.getElementById('select-categories');
    var url = 'http://127.0.0.1:8000/goodsByCategory?category=' + select.value;
    Request.open('get', url, true);
    Request.send(null);
}
