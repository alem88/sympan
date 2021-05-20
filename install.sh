pip uninstall -y sympan

python setup.py clean
python setup.py sdist bdist_wheel
python setup.py install

pip install .
