LINE = ============================

all: train eval_20

# Train all the models
train: train_flat train_rbranch train_lbranch

train_flat:
	python train.py -m flat -o flat

train_rbranch:
	python train.py -m rbranch -o rbranch

train_lbranch:
	python train.py -m lbranch -o lbranch

eval:
	python eval.py -i flat
	python eval.py -i rbranch
	python eval.py -i lbranch

# Sentences with length <= 20 for the README
eval_20:
	@echo $(LINE)
	@echo "Model: Flat"
	@time -p python eval.py -i flat -m 20
	@echo $(LINE)
	@echo "Model: Rbranch"
	@time -p python eval.py -i rbranch -m 20
	@echo $(LINE)
	@echo "Model: Lbranch"
	@time -p python eval.py -i lbranch -m 20
	@echo $(LINE)

clean:
	rm flat rbranch lbranch
