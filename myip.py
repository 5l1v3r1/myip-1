import os,cgi,cgitb 

cgitb.enable()
html="""<!DOCTYPE html>
<html>
    <body>
        <script type="application/javascript"> function getIP(json) { document.write(json.ip); } </script>
        <script type="application/javascript"src="https://api.ipify.org?format=jsonp&callback=getIP"></script>
    </body>
</html>"""

print(html)
os.system("touch file.png")
