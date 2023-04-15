function readJSONFile(file, callback) {
  let xhr = new XMLHttpRequest();
  xhr.overrideMimeType("application/json");
  xhr.open('GET', file, true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == "200") {
      callback(JSON.parse(xhr.responseText));
    }
  };
  xhr.send(null);
}
function writeJSONFile(file, data) {
  let xhr = new XMLHttpRequest();
  xhr.open('POST', file, true);
  xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
  xhr.send(JSON.stringify(data));
}
updateButton.addEventListener('click', () => {
  let videoLink = videoLinkInput.value;
  let videoId = getVideoIdFromLink(videoLink);

  if (videoId) {
    readJSONFile('videos.json', function(data) {
      let videos = data.videos;
      let exists = videos.some(function(video) {
        return video.id === videoId;
      });

      if (!exists) {
        videos.push({id: videoId});
        writeJSONFile('videos.json', data);
      }

      player.loadVideoById(videoId);
      errorMessage.style.display = 'none';
    });
  } else {
    errorMessage.style.display = 'block';
  }
});
