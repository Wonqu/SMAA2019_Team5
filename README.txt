To fastText

$ git clone https://github.com/facebookresearch/fastText.git
$ cd fastText
$ sudo pip install .
$ # or :
$ sudo python setup.py install


Notes

gc .\cooking.stackexchange.txt -head 12404 > cooking.train
gc .\cooking.stackexchange.txt -tail 3000 > cooking.valid 