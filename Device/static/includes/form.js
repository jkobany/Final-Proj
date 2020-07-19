
$('#Ensured_by').click(function () {
    $.ajax({
        'async': false,
        'global': false,
        'url': "/static/data.json",
        'dataType': "json",
        'success': function (data) {

            for (var x = 0; x < data.length; x++) {
                var el = document.createElement('option');
                el.setAttribute('value', data[x]['NAME']);
                el.innerHTML = data[x]['NAME'];
                $("#Ensured_by").append(el);
            }
        },
        'error': function (data) { alert(data) }
    });
});
