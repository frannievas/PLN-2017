main:
	python train.py -n 1 -o GOT -m addone
	python train.py -n 2 -o GOT2 -m addone
	python train.py -n 3 -o GOT3 -m addone
	python train.py -n 4 -o GOT4 -m addone

generate:
	python generate.py -i GOT
	python generate.py -i GOT2
	python generate.py -i GOT3
	python generate.py -i GOT4

eval:
	python eval.py -i GOT
	python eval.py -i GOT2
	python eval.py -i GOT3
	python eval.py -i GOT4
