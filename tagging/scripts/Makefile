ROOT = ../../corpus

train_tagg:
	python train.py -m mlhmm -n 1 -o ml
	python train.py -m mlhmm -n 2 -o ml2
	python train.py -m mlhmm -n 3 -o ml3
	python train.py -m mlhmm -n 4 -o ml4

eval:
	python eval.py -i ml
	python eval.py -i ml2
	python eval.py -i ml3
	python eval.py -i ml4

clean:
	rm ml ml2 ml3
