<!DOCTYPE html>
<html>
<head>
    <title>Parseador y Reproductor de Videos</title>
</head>
<body>
    <h1>Parseador y Reproductor de Videos</h1>
    <label for="clipboardInput">Pega el contenido del portapapeles aquí:</label>
    <br>
    <textarea id="clipboardInput" rows="10" cols="50" onclick="pasteClipboardData()"></textarea>
    <br>
    <button id="parseButton">Analizar y Descargar</button>

    <br><br>

    <label for="videoSelect">Selecciona un video:</label>
    <select id="videoSelect">
        <option value="">Selecciona un video</option>
    </select>
    <br>
    <button id="playButton">Reproducir</button>

    <script>
        // Función para pegar el contenido del portapapeles en el campo de entrada de texto
        function pasteClipboardData() {
            const clipboardInput = document.getElementById('clipboardInput');
            navigator.clipboard.readText()
                .then((text) => {
                    clipboardInput.value = text;
                })
                .catch((error) => {
                    console.log('No se pudo acceder al portapapeles.');
                });
        }

        // Función para descargar un archivo
        function downloadFile(filename, content) {
            const blob = new Blob([content], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
            URL.revokeObjectURL(url);
        }
        
        // Función para manejar el contenido del portapapeles
        function handleClipboardText(text) {
            try {
                const clipboardData = JSON.parse(text);
                if (clipboardData.links && Array.isArray(clipboardData.links)) {
                    const linksJSON = JSON.stringify(clipboardData, null, 2);
                    downloadFile('links.json', linksJSON);

                    // Llenar la lista desplegable con los enlaces
                    const videoSelect = document.getElementById('videoSelect');
                    videoSelect.innerHTML = '<option value="">Selecciona un video</option>';
                    clipboardData.links.forEach((link) => {
                        videoSelect.innerHTML += `
                            <option value="${link.url}">Video (${link.server}) - ${link.quality}</option>
                        `;
                    });
                } else {
                    alert('El contenido del portapapeles no coincide con la estructura esperada.');
                }
            } catch (error) {
                alert('El contenido del portapapeles no es un objeto JSON válido.');
            }
        }

        // Función que se ejecuta al hacer clic en el botón "Analizar y Descargar"
        function parseClipboard() {
            const clipboardInput = document.getElementById('clipboardInput');
            const text = clipboardInput.value;
            handleClipboardText(text);
        }

        // Función para reproducir el video seleccionado en una nueva ventana
        function playVideo() {
            const selectedUrl = videoSelect.value;
            if (selectedUrl) {
                window.open(selectedUrl, '_blank');
            } else {
                alert('Selecciona un video para reproducir.');
            }
        }

        // Agregar listeners para los botones
        const parseButton = document.getElementById('parseButton');
        parseButton.addEventListener('click', parseClipboard);

        const playButton = document.getElementById('playButton');
        playButton.addEventListener('click', playVideo);
    </script>
</body>
</html>
