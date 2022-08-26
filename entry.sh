
#!/bin/bash

flask db init
flask db migrate
flask db upgrade

python3 server/serve.py
