<!DOCTYPE html>
<html>
<head>
  <title>Reproducir Playlist de YouTube</title>
</head>
<body>

  <video id="videoPlayer" controls></video>

  <script>
    // URL de la playlist
    const playlistUrl = 'https://www.youtube.com/playlist?list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG';
    
    // ID de los primeros 3 videos
    const videoIds = ['123456', '234567', '345678']; 
    
    let currentVideoIndex = 0;
    
    // Carga el primer video en el reproductor
    loadVideo(videoIds[currentVideoIndex]); 

    // Reproduce el siguiente video cuando termina el actual
    videoPlayer.onended = playNextVideo;

    function playNextVideo() {
      currentVideoIndex++;
      loadVideo(videoIds[currentVideoIndex]);
    }

    function loadVideo(videoId) {
      // Carga el video desde YouTube
      const videoUrl = 'https://www.youtube.com/watch?v=' + videoId;

      // Actualiza el reproductor con el nuevo video
      videoPlayer.src = videoUrl; 
      videoPlayer.play();

      // Elimina el primer video de la lista
      videoIds.shift();

      // Agrega un nuevo video al final de la lista
      fetch(playlistUrl)
        .then(response => response.json())
        .then(data => {
          const nextVideoId = data.items[2].snippet.resourceId.videoId;
          videoIds.push(nextVideoId);
        });
    }
  </script>

</body>
</html>