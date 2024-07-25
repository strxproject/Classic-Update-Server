# Classic-Update-Server
This is the update server for Classic 7. Here's how it works.
### Changelogs
The Flask server looks into the file called `changelog.txt` if you do a `http://127.0.0.1:5000/getchangelog`.

You can pair this with `/getversion` which checks a file called `version.txt` for the version number.