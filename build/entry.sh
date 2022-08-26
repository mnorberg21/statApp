
#!/bin/bash

flask db init
flask db migrate
flask db upgrade

python3 backend/serve.py
