from urllib.request import urlopen
import sys

ip_address = urlopen("https://ipinfo.io/ip").read().decode('utf-8')

with open("index.html", "w") as f:
  f.write(f'''
<iframe src="https://{ip_address}:5000" title="Flask App" id="flask_app"></iframe>
<script>
let elem = document.getElementById("flask_app");
elem.setAttribute("width", window.innerWidth);
elem.setAttribute("height", window.innerHeight);
</script>
  ''')
