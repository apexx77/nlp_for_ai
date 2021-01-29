import sys


f1 = open(sys.argv[1])
count = 0
true = 0
false = 0
sentences = 0
for line in f1:
	if line == "\n" or line.split()==[] :
		sentences += 1
		continue
	count = count + 1
	x = line.strip().split()
	if(x[-1]==x[-2]) :
		true = true+1
	else :
		 false = false + 1

accuracy = 100.0*true/count

print("Correctly Tagged Words: ", true)
print("Incorrectly Tagged Words: ", false)
print("Total Words: ", count)
print("Total Sentences: ", sentences)
print("Accuracy: ", accuracy)
	
