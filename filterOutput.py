import os
def main():
	
	filteredOutput = open('filteredOutput.txt', 'w')
	noneFiles = open('noneOutput.txt', 'w')
	f = open('output.txt', 'r')
	
	last = None
	atual = None

	lines = f.readlines()
	for line in lines:
		if (('None' in line) or (', ,' in line)):
			noneFiles.write(line)
			continue


		last = atual
		atual = line.split(',')[1]
		prefix = 'https://Anomalo:123mudar@'
		if last != atual:
			if 'git+ssh://' in line:
				line = line.replace('git+ssh://', prefix)
	
			elif  'git+https://' in line:
				line = line.replace('git+https://', prefix)			
	
			elif 'git://' in line:
				line = line.replace('git://', prefix)

			elif 'git@github.com' in line:
				line = line.replace('git@github.com', prefix)

			
			filteredOutput.write(line)

	noneFiles.close()
	filteredOutput.close()
	clone()

def clone():
	f = open('filteredOutput.txt','r')
	lines = f.readlines()

	for line in lines:
		repo = line.split(',')[1].strip()
		try:
			os.system('cd repoFolder;git clone ' + repo)
		except Exception as e:
			print e
			pass
		





if __name__ == '__main__':
	main()
