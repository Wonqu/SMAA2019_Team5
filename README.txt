To fastText

$ git clone https://github.com/facebookresearch/fastText.git
$ cd fastText
$ sudo pip install .
$ # or :
$ sudo python setup.py install


General Notes

gc .\cooking.stackexchange.txt -head 12404 > cooking.train
gc .\cooking.stackexchange.txt -tail 3000 > cooking.valid 

Linux commands

head -n 18000 SMAA2019_Team5/data/out/spook_to_fasttext.csv > spook.train
tail -n 1579 SMAA2019_Team5/data/out/spook_to_fasttext.csv > spook.valid
./fasttext supervised -input spook.train -output model_spook
./fasttext test model_spook.bin spook.valid
./fasttext supervised -input spook.train -output model_spook2 -lr 0.5 -epoch 25 -wordNgrams 2 -bucket 200000 -dim 50 -loss one-vs-all
./fasttext test model_spook2.bin spook.valid

Single use

./fasttext predict-prob model_spook2.bin - -1 0.5
For I am Iranon, who was a Prince in Aira.


After more data:

head -n 3000 SMAA2019_Team5/data/out/spook_to_fasttext.csv > spook.valid
tail -n 22958 SMAA2019_Team5/data/out/spook_to_fasttext.csv > spook.train
./fasttext supervised -input spook.train -output model_spook
./fasttext test model_spook.bin spook.valid

With additional vector:

./fasttext supervised -input spook.train -output model_spook -dim 300 -pretrainedVectors wiki-news-300d-1M-subword.vec

With additional parameters:

./fasttext supervised -input spook.train -output model_spook \
-dim 300 -pretrainedVectors wiki-news-300d-1M-subword.vec \
-epoch 25 -wordNgrams 2 -loss hs -lr 0.5
;




LSTM setup

1. Go to https://nlp.stanford.edu/projects/glove/ and download glove.6B.zip
2. Unzip and copy glove.6B.100d.txt into project's dir
4. pip install -r requirements.txt
3. python lovecraftian_LSTM.py 