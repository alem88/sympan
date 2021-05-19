pip uninstall -y sympan

python setup.py clean
python setup.py build
python setup.py install

pip install .
