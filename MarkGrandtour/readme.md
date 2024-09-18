To avoid CORS issues, you must run from a web server. 
For local needs, easiest is likely:  
cd D:\Sandbox\git\(YADA)\MarkGrandtour  
python -m http.server  
index.html is then found using:  
http://localhost:8000/index.html#  

VS Code Live Server is perfectfully good for testing locally.
For testing for another device on the same network:
1. allow the port (e.g. 5500) through the firewall
2. check that the 2 devices are using the same SSID
