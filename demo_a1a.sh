
echo '--- SMO (Keerthi) ---'
./classify.py -vc svm-smo-keerthi \
	--complexity=100 --accuracy=1e-12 \
	-k rbf --gamma=10 \
	--training-file=./data/classification/a1a \
	--test-file=./data/classification/a1a.t