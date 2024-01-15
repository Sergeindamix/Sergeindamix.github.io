let pagina = 1;
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

const cargarPeliculasDesdeJson = async () => {
    try {
        const respuesta = await fetch('videos.json'); // Cambia el nombre del archivo si es necesario
        const datosJson = await respuesta.json();

        let peliculas = '';

        for (const video of datosJson) {
            const tituloSinAnio = eliminarAnio(video.name);
            const resultadosTMDB = await realizarBusquedaTMDB(tituloSinAnio);

            // Asegurémonos de que haya resultados antes de acceder a la primera película
            if (resultadosTMDB.length > 0) {
                const primeraPelicula = resultadosTMDB[0];

                peliculas += `
                    <div class="tarjeta">
                        <img class="portada" src="https://image.tmdb.org/t/p/w500/${primeraPelicula.poster_path}">
                        <h3 class="titulo">${primeraPelicula.title}</h3>
                        <p class="descripcion">${primeraPelicula.overview}</p>
                        <a href="${video.link}" target="_blank" rel="noopener noreferrer">Ver película</a>
                    </div>
                `;
            }
        }

        document.getElementById('galeria').innerHTML = peliculas;
    } catch (error) {
        console.error('Error al cargar las películas desde TMDB:', error);
    }
};

// Llamada inicial para probar la carga de películas desde el archivo JSON local
// ¡Recuerda que esta llamada se debe hacer dentro del contexto de una función asíncrona!
// await cargarPeliculasDesdeJson();


// Llamada inicial para probar la carga de películas desde el archivo JSON local
// ¡Recuerda que esta llamada se debe hacer dentro del contexto de una función asíncrona!
// await cargarPeliculasDesdeJson();
// Define una función asíncrona para iniciar tu aplicación
const iniciarApp = async () => {
    try {
        // Llama a cargarPeliculasDesdeJson al iniciar
        await cargarPeliculasDesdeJson();
    } catch (error) {
        console.error('Error al iniciar la aplicación:', error);
    }
};

// Llama a la función iniciarApp al cargar la página
iniciarApp();






  
  

// cargarPeliculas();  // Puedes comentar o eliminar este llamado si no es necesario
