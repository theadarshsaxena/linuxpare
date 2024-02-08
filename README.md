# PAM Manager!


# Ways to run the app

## SSH Tunnel setup to run the app (Recommended)
ssh -L 5000:localhost:5000 -o "ServerAliveInterval 60" -o "ServerAliveCountMax 120" -i <your-key> <host>

## setup flask

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py