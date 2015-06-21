import sys
from sklearn.linear_model import LogisticRegression, LinearRegression

def main():
	print("training data file1: " + str(sys.argv[1]))
	file = open(str(sys.argv[1]))
	"""
	IMPORTANT: Change this variable too change target attribute 
	"""
	#extract training data
	data = [[]]
	for line in file:
		line = line.strip("\r\n")
		data.append(line.split(','))
	file.close()
	data.remove([])
	attributes = data[0]
	print(attributes)
	data.remove(attributes)
	attributes.remove(attributes[len(attributes)-1])
	expected = []
	i = 0
	for entry in data:
		expect = int(entry[0])
		if i == 0:
			length = len(entry) - 1
		expected.append(expect)
		del entry[0]
		entry = np.array(entry, dtype=float)
		i = i+1
	expected = np.array(expected, dtype=float)
	data = np.array(data, dtype=float)
	#data = [[1,0,1,1,0],[0,0,1,1,1],[1,1,1,0,0]]
	gp = LogisticRegression()
	gp.fit(data, expected)
	#gpSummary = GPassist.summarizeByClass(data)
	# Instanciate a GP model
	data = [[]]
	print("test data file: " + str(sys.argv[2]))
	file = open(str(sys.argv[2]))
	for line in file:
		line = line.strip("\r\n")
		data.append(line.split(','))
	data.remove([])
	attributes = data[0]
	data.remove(attributes)
	attributes.remove(attributes[0])
	expected = []
	i = 0
	correct = 0
	for entry in data:
		expect = int(entry[len(entry)-1])
		if i == 0:
			length = len(entry) - 1
		expected.append(expect)
		entry.pop()
		i = i + 1
		entry = np.array(entry, dtype=float)
		print(gp.predict(entry))
		if result == expect:
			correct = correct + 1
	accuracy = float(correct)/i * 100
	print (str(accuracy) + "% correctly identified")
		
if __name__ == '__main__':
	main()