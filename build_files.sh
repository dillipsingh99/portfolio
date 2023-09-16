# echo "BUILD START"
pip install --root-user-action=ignore
pip install -r requirements.txt
python3.9 manage.py collectstatic
# echo "BUILD END"