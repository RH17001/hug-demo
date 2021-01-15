//el metodo fetch nos permite hacer una llamada a una api en este caso a nuestra api con hug
//en la linea 4 transformamos nuestra respuesta a un formato json y posteriormente cargamos
//el calendario 
fetch('http://0.0.0.0:8000/selectAll')
    .then(response => response.json())
    .then(data => {
        $('#calendar').evoCalendar({
            'language': 'es',
            'todayHighlight': true,
            'theme': 'Royal Navy',
            'calendarEvents': data
        });
    });



function openLoginForm() {
    document.body.classList.add("showLoginForm");
}
function closeLoginForm() {
    document.body.classList.remove("showLoginForm");
}

function guardar() {
    let nombre = document.getElementById('nombre').value;
    let tipo = document.getElementById('tipo').value;
    let descripcion = document.getElementById('descripcion').value;
    let fecha = crearFecha($('#calendar').evoCalendar('getActiveDate'));
    //codigo para consumir la api
}



function eliminar() {

}


function crearFecha(fecha) {
    let months = ['January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    let datos = fecha.split('/');
    return months[datos[0] - 1] + " " + + datos[1] + ", " + datos[2];
}