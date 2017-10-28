# Finding Nemo

### Author: Isaac Hong Wong (iwong@uoregon.edu)

This is a web app that displays some sushi restaurants around the city of Eugene, OR.

Setup:
1) Copy credentials-skel.ini into sushi/credentials.ini, and fill out the necessary information
2) Copy secrets-skel.py into sushi/secrets.py, and fill out the developer key. A key can be obtained from https://www.mapbox.com/studio/account/tokens/
3) Run: 
```
make install
. env/bin/activate
make start
```

4) To stop the server:
```
make stop
```