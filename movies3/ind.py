import os

# Directorio donde se encuentran los archivos HTML
html_directory = './'

# Obtener la lista de archivos HTML en la raíz
html_files = [f for f in os.listdir(html_directory) if f.endswith('.html')]
html_files.sort()  # Ordenar la lista alfabéticamente

# Crear el contenido del archivo "index.html"
html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.navbar-container {
  width: 100%;
  overflow: auto;
}

.navbar {
  background-color: #333;
  text-align: center;
  white-space: nowrap;
  display: inline-block;
}

.navbar a {
  color: #f2f2f2;
  text-decoration: none;
  padding: 10px 15px;
  display: inline-block;
}

.navbar a:hover {
  background: #ddd;
  color: black;
}

.navbar a.active {
  background-color: #007BFF;
  color: white;
}

.page-content {
  padding: 20px;
  text-align: center;
}
</style>
<script>
function scrollLinks(direction) {
    const navbar = document.querySelector('.navbar-container');
    const scrollAmount = direction === 'left' ? -100 : 100;
    navbar.scrollLeft += scrollAmount;
}

function markActiveLink(event) {
    const links = document.querySelectorAll('.navbar a');
    links.forEach((link) => {
        link.classList.remove('active');
    });
    event.target.classList.add('active');
}
</script>
</head>
<body>

<div class="navbar-container">
  <div class="navbar">
"""

# Mostrar enlaces en un carrusel
for i in range(1, len(html_files) + 1):
    link = f'<a href="{html_files[i-1]}" target="page-frame">{i}</a>'
    html_content += link

# Cerrar el contenido de la barra de navegación
html_content += """
  </div>
</div>
<div class="page-content">
    <iframe name="page-frame" src="page_1.html" width="100%" height="600px"></iframe>
</div>
<div class="fixed-buttons">
    <button onclick="scrollLinks('left')">◄</button>
    <button onclick="scrollLinks('right')">►</button>
</div>
<script>
const links = document.querySelectorAll('.navbar a');
links.forEach((link) => {
    link.addEventListener('click', markActiveLink);
});
</script>
</body>
</html>
"""

# Guardar el archivo "index.html" en el raíz
index_filename = 'index.html'
with open(os.path.join(html_directory, index_filename), 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f"File list index generated as {index_filename}.")
