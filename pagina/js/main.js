var id = null;

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

$('#calendar').on('selectEvent', function (event, activeEvent) {
    openLoginForm();
    id = activeEvent['id'];
    document.getElementById('boton').firstChild.data = 'Eliminar';
    document.getElementById('nombre').value = activeEvent['name'];
    document.getElementById('tipo').value = activeEvent['type'];
    document.getElementById('descripcion').value = activeEvent['description'];
});

function openLoginForm() {
    document.body.classList.add("showLoginForm");
}

function cerrar() {
    document.body.classList.remove("showLoginForm");
    document.getElementById('boton').firstChild.data = 'Cancelar';
    document.getElementById('nombre').value = '';
    document.getElementById('tipo').value = '';
    document.getElementById('descripcion').value = '';
    id = null;
}

function closeLoginForm() {
    document.body.classList.remove("showLoginForm");
    document.getElementById('boton').firstChild.data = 'Cancelar';
    document.getElementById('nombre').value = '';
    document.getElementById('tipo').value = '';
    document.getElementById('descripcion').value = '';
    console.log(id);
    if (id != null) {
        //eliminar registros
        let data = new FormData();
        let idd = id
        data.append('id', id)
        let request = new Request('http://0.0.0.0:8000/delete', {
            method: 'DELETE',
            body: data,
            headers: new Headers()
        });

        fetch(request).then(function(){
            $('#calendar').evoCalendar('removeCalendarEvent', idd);
            cerrar()
        });
    }
    id = null;
}

function guardar() {
    //obtener datos del formulario
    let idd = new Date().toString();
    let nombre = document.getElementById('nombre').value;
    let tipo = document.getElementById('tipo').value;
    let descripcion = document.getElementById('descripcion').value;
    let fecha = crearFecha($('#calendar').evoCalendar('getActiveDate'));
    //codigo para consumir la api

    //preparamos nuestros datos
    let data = new FormData()
    data.append('id', idd);
    data.append('date', fecha);
    data.append('name', nombre);
    data.append('description', descripcion);
    data.append('type', tipo);

    //preparamos la peticion
    let request = new Request('http://0.0.0.0:8000/insert', {
        method: 'POST',
        body: data,
        headers: new Headers()
    });

    //ejecutamos nuestra peticion
    fetch(request).then(function () {
        //agregamos nuestro evento al calendario
        $('#calendar').evoCalendar('addCalendarEvent', {
            id: idd,
            name: nombre,
            description: descripcion,
            date: fecha,
            type: tipo
        });
        cerrar()
    });

}

function crearFecha(fecha) {
    let months = ['January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    let datos = fecha.split('/');
    return months[datos[0] - 1] + " " + + datos[1] + ", " + datos[2];
}