Notes:<br/>
Images picked from https://retroarch.org<br/>
Color palette extracted from https://www.color-hex.com/color-palette/21486 and https://nhfournier.es<br/>

Si he d'afegir una nova caracteristica als jocs de cartes, he de modificar-ho a models.py, a views.py (WikiList) i a wiki.html (la taula).


## Local Setup
` git clone git@github.com:wiseshell-net/wiseshell.net.git`<br/>
`cd wiseshell.net`<br/>
`python3 -m venv venv`<br/>
`source venv/bin/activate`<br/>
`pip3 install -r requirements.txt`<br/>
`python3 manage.py makemigrations`<br/>
`python3 manage.py migrate`<br/>
`python3 manage.py runserver`<br/>

Obre el navegador a http://127.0.0.1:8000 per accedir a la web.
