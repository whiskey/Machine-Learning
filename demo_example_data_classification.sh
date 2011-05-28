## short demo how to use the command line parameters

echo '--- dual coordinate descent ---'
./classify.py -vc svm-cd \
	--complexity=1 --accuracy=1e-12 \
	-k poly --degree=5 \
	--training-file=./data/classification/example_data_classification \
	--test-file=./data/classification/example_data_classification.t
	
echo 
echo '--- SMO (Keerthi) ---'
./classify.py -vc svm-smo-keerthi \
	--complexity=10 --accuracy=1e-12 \
	-k rbf --gamma=10 \
	--training-file=./data/classification/example_data_classification \
	--test-file=./data/classification/example_data_classification.t