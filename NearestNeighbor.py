import numpy as np
def calculate_euclidean_distance(testInstance, trainInstance, length):
	distance = 0
	for x in range(length):
		distance += (testInstance[x] - trainInstance[x])**2
	return distance**0.5
def k_nearest_neighbors(data, predict, k=5):
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = calculate_euclidean_distance(features, predict, len(predict))
            distances.append([euclidean_distance,group])
    votes = [i[1] for i in sorted(distances)[:k]]

    vote_counter = {}
    for feature in votes:
        if feature in vote_counter:
            vote_counter[feature] += 1
        else:
            vote_counter[feature] = 1
    voting_result = sorted(vote_counter.iteritems(), key=lambda tup: tup[1],reverse = True)
    return voting_result[0][0]

train_data = np.genfromtxt("iris-training-data.csv", dtype=None, delimiter=',')
test_data = np.genfromtxt("iris-testing-data.csv", dtype=None, delimiter=',')

train_features = np.genfromtxt("iris-training-data.csv", dtype=float, delimiter=',', skip_header=0,usecols=(0,1,2,3))
test_features =np.genfromtxt("iris-testing-data.csv", dtype=float, delimiter=',', skip_header=0,usecols=(0,1,2,3))

train_set = {'Iris-setosa':[],'Iris-versicolor':[],'Iris-virginica':[] }
test_set = {'Iris-setosa':[],'Iris-versicolor':[],'Iris-virginica':[] }
counter = 0

for x in range(len(train_data)):
    for key,value in train_set.iteritems():
        if key == train_data[x][-1]:
            train_set[key].append(train_features[x])

for x in range(len(test_data)):
    for key,value in test_set.iteritems():
        if key == test_data[x][-1]:
            test_set[key].append(test_features[x])

correct = 0.0
total = 0.0
counter = 1

print '#, Predicted, Actual'
for group in test_set:
    for data in test_set[group]:
        vote = k_nearest_neighbors(train_set, data, k=1)
        print counter,vote,group
        counter +=1
        if group == vote:
            correct += 1
        total += 1

accuracy = correct/total * 100.0
print 'Accuracy: ' + repr(accuracy) + '%'
