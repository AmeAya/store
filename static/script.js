function checkLogin() {
    var loginInput = document.getElementById('login');

    var Request = new XMLHttpRequest();

    Request.onreadystatechange = function() {
        if (Request.readyState == 4) {
            var response = JSON.parse(Request.responseText);
            alert(response.isAvailable);
        }
    }

    var url = 'http://127.0.0.1:8000/check?login=' + loginInput.value;
    Request.open('get', url, true);
    Request.send(null);
}