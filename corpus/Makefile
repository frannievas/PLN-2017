RR = ../languagemodeling/scripts/
# Cantidad de oraciones
N = 10

main:
	python $(RR)train.py -n 1 -o GOT -m addone
	python $(RR)train.py -n 2 -o GOT2 -m addone
	python $(RR)train.py -n 3 -o GOT3 -m addone
	python $(RR)train.py -n 4 -o GOT4 -m addone

generate:
	python $(RR)generate.py -i GOT  -n $(N)
	python $(RR)generate.py -i GOT2 -n $(N)
	python $(RR)generate.py -i GOT3 -n $(N)
	python $(RR)generate.py -i GOT4 -n $(N)

eval:
	python $(RR)eval.py -i GOT
	python $(RR)eval.py -i GOT2
	python $(RR)eval.py -i GOT3
	python $(RR)eval.py -i GOT4

inter:
	python $(RR)train.py -n 2 -o GOT2 -m inter

interaddone:
	python $(RR)train.py -n 2 -o GOT2 -m interaddone
