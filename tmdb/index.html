const btnAnterior = document.getElementById('btnAnterior');
const btnSiguiente = document.getElementById('btnSiguiente');

btnSiguiente.addEventListener('click', () => {
	if(pagina < 1000){
		pagina += 1;
		cargarPeliculas();
	}
});

btnAnterior.addEventListener('click', () => {
	if(pagina > 1){
		pagina -= 1;
		cargarPeliculas();
	}
});

const cargarPeliculas = async() => {
	try {
		const respuesta = await fetch(`https://api.themoviedb.org/3/movie/popular?api_key=192e0b9821564f26f52949758ea3c473&language=es-MX&page=${pagina}`);
	
		console.log(respuesta);

		// Si la respuesta es correcta
		if(respuesta.status === 200){
			const datos = await respuesta.json();
			
			let peliculas = '';
			datos.results.forEach(pelicula => {
				peliculas += `
					<div class="pelicula">
						<img class="poster" src="https://image.tmdb.org/t/p/w500/${pelicula.poster_path}">
						<h3 class="titulo">${pelicula.title}</h3>
					</div>
				`;
			});

			document.getElementById('contenedor').innerHTML = peliculas;

		} else if(respuesta.status === 401){
			console.log('Pusiste la llave mal');
		} else if(respuesta.status === 404){
			console.log('La pelicula que buscas no existe');
		} else {
			console.log('Hubo un error y no sabemos que paso');
		}

	} catch(error){
		console.log(error);
	}

}


  
const realizarBusquedaTMDB = async (titulo) => {
    try {
        const respuesta = await axios.get(`https://api.themoviedb.org/3/search/movie`, {
            params: {
                api_key: '62ef27a2db165131317f8ee3fedb705b',
                language: 'es-ES',
                query: titulo
            }
        });

        if (respuesta.status === 200) {
            return respuesta.data.results; // Devolvemos solo los resultados
        } else {
            throw new Error(`Error en la búsqueda de TMDB para ${titulo}. Estado: ${respuesta.status}`);
        }

    } catch (error) {
        throw error;
    }
};

const eliminarAnio = (titulo) => {
    // Utilizamos una expresión regular para eliminar el año entre paréntesis
    return titulo.replace(/\(\d{4}\)/g, '').trim();
};

// Variable para controlar la página actual
let pagina = 1;
const peliculasPorPagina = 20;

// Variable para verificar si ya se están cargando más películas
let cargando = false;

// Función para cargar películas desde el archivo JSON
const cargarPeliculasDesdeJson = async () => {
    try {
        const respuesta = await fetch('https://sergeindamix.github.io/filmore/videos.json');
        const datosJson = await respuesta.json();

        // Función para cargar tarjetas de películas en el contenedor
        const cargarTarjetas = async (inicio, fin) => {
            for (let i = inicio; i < fin; i++) {
                if (i >= datosJson.length) {
                    break;
                }

                const video = datosJson[i];
                const tituloSinAnio = eliminarAnio(video.name);
                const resultadosTMDB = await realizarBusquedaTMDB(tituloSinAnio);

                if (resultadosTMDB.length > 0) {
                    const primeraPelicula = resultadosTMDB[0];

                    // Crea el HTML para la tarjeta de la película
                    const tarjetaHTML = `
                        <div class="pelicula">
                            <img class="poster" src="https://image.tmdb.org/t/p/w500/${primeraPelicula.poster_path}">
                            <h3 class="titulo">${primeraPelicula.title}</h3>
                            <p class="descripcion">${primeraPelicula.overview}</p>
                            <a href="${video.link}" target="_blank" rel="noopener noreferrer">Ver película</a>
                        </div>
                    `;

                    // Agrega la tarjeta al contenedor
                    document.getElementById('contenedor').insertAdjacentHTML('beforeend', tarjetaHTML);
                }
            }
        };

        // Llamada inicial para cargar las primeras 20 películas
        await cargarTarjetas(0, peliculasPorPagina);

        // Agrega el observador de scroll
        window.addEventListener('scroll', async () => {
            // Si ya se están cargando más películas o no hay más que cargar, sal del evento
            if (cargando || pagina * peliculasPorPagina >= datosJson.length) {
                return;
            }

            // Si el usuario ha llegado al final del documento
            if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
                // Indica que se está cargando más películas para evitar solicitudes concurrentes
                cargando = true;

                // Incrementa la página y carga las siguientes 20 películas
                pagina++;
                const inicio = (pagina - 1) * peliculasPorPagina;
                const fin = pagina * peliculasPorPagina;

                // Carga las siguientes películas
                await cargarTarjetas(inicio, fin);

                // Actualiza el estado de carga
                cargando = false;
            }
        });
    } catch (error) {
        console.error('Error al cargar las películas desde TMDB:', error);
    }
};

// Llamada inicial para cargar las primeras 20 películas
cargarPeliculasDesdeJson();
