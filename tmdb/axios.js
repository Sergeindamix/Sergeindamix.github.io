let peliculas = '';
let pagina = 1;

// Función para realizar la búsqueda del título
async function buscarTitulo() {
    // Obtener el valor de la caja de texto
    var titulo = document.getElementById("searchInput").value;
    // Realizar la acción de búsqueda con el título
    // Puedes agregar aquí la lógica específica para tu aplicación
    // alert("Realizando búsqueda del título: " + titulo);
    peliculas = '';
    // Llamar a la función obtenerPeliculas con el título
    await obtenerPeliculas(titulo);
    await cargarGaleria();
}

// Función para obtener películas
const obtenerPeliculas = async (titulo) => {
    try {
        const respuesta = await axios.get(`https://api.themoviedb.org/3/search/movie`, {
            params: {
                api_key: '62ef27a2db165131317f8ee3fedb705b',
                language: 'es-ES',
                query: titulo
            }
        });

        // Si la respuesta es correcta
		if(respuesta.status === 200){	
			respuesta.data.results.forEach(pelicula => {
				peliculas += `
                    <div class="tarjeta">
                        <img class="portada" src="https://image.tmdb.org/t/p/w500/${pelicula.poster_path}">
                        <h3 class="titulo">${pelicula.title}</h3>
                        <p class="descripcion">${pelicula.overview}</p>
                    </div>
                `;
            });

            

			document.getElementById('galeria').innerHTML = peliculas;

			
		} else if(respuesta.status === 401){
			console.log('Pusiste la llave mal');
		} else if(respuesta.status === 404){
			console.log('La pelicula que buscas no existe');
		} else {
            throw new Error(`Error en la búsqueda de TMDB para ${titulo}. Estado: ${respuesta.status}`);
        }
    } catch (error) {
        console.log(error);
    }
}

async function cargarGaleria() {
    try {
        const respuesta = await fetch('resultadosTMDB.json');
        const datos = await respuesta.json();

        datos.forEach((pelicula) => {
            const tarjeta = document.createElement('div');
            tarjeta.classList.add('tarjeta');

            tarjeta.innerHTML = `
                <img class="portada" src="${pelicula.portada}" alt="Portada">
                <div class="titulo">${pelicula.titulo}</div>                        
            `;

            if (pelicula.detalles !== null) {
                tarjeta.innerHTML += `<p class="descripcion">${pelicula.detalles.overview}</p>`;
            }

            document.getElementById('galeria').appendChild(tarjeta);
        });
    } catch (error) {
        console.error('Error al cargar el JSON:', error);
    }
}

//window.onload = cargarGaleria;
