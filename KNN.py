import numpy as np

def calculate_euclidean_distance(testData, trainData, length):
	distance = 0
	for x in range(length):
		distance += (testData[x] - trainData[x])**2
	return distance**0.5

def knn(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = calculate_euclidean_distance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))

	distances = sorted(distances, key=lambda tup: tup[1])

	neighbors = []
	for x in range(k):
	    neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1

	sortedVotes = sorted(classVotes.iteritems(), key=lambda tup: tup[1],reverse = True)
	return sortedVotes[0][0]

def main():
	# prepare data
	trainingSet=[]
	testSet=[]

        trainingSet = np.genfromtxt("iris-training-data.csv", dtype=None, delimiter=',', skip_header=0)
	testSet = np.genfromtxt("iris-testing-data.csv", dtype=None, delimiter=',', skip_header=0)

        print len(trainingSet)
	# generate predictions
	predictions=[]
	k = 5
	counter = 0
	print ('#, True, Predicted')
	for x in range(len(testSet)):
	    neighbors = knn(trainingSet, testSet[x], k)
	    result = getResponse(neighbors)
	    predictions.append(result)
	    counter += 1
	    print counter, testSet[x][-1],result
	correct = 0
	for x in range(len(testSet)):
	    if testSet[x][-1] == predictions[x]:
	        correct += 1
	accuracy = correct/float(len(testSet)) * 100.0
	print 'Accuracy: ' + repr(accuracy) + '%'

main()
