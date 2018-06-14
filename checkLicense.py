import os
import subprocess
import re
import shutil
from progressbar import ProgressBar




def getLastRepository(file):
	result = open('NewOutput.txt', 'w')
	pbar = ProgressBar()
	
	aux = ""
	for line in file:
		
		package = line.split(',')
		packageName = package[0].strip()
		repositoryLink = package[1].strip()
		qtdLicenses = package[2].strip()


		if repositoryLink != aux and repositoryLink != "None":
			#result.write(line)
			#result.write(repostoryLink)
			cloneRepository(repositoryLink, qtdLicenses)
			aux = repositoryLink

	result.close()





def cloneRepository(urlRepository, licenseCount):
	notFoundRepo = []

	newUrlRepository = re.sub('.*://', 'https://Anomalo:123mudar@', urlRepository)
	print '\n'
	print "======================================================================"
	print urlRepository
	print "======================================================================"
	try:
		subprocess.check_output("git clone " + newUrlRepository + " repoFolder" , shell=True)
		licenses = foundLicense()
		pass
	except Exception as e:
		notFoundRepo.append(urlRepository)
		return

	if str(licenses) != str(licenseCount):
		print "Inconsistencia > {} != {}".format(licenses, licenseCount)
	else:
		print "OK!"
	# Deleta o repositorio
	shutil.rmtree('repoFolder', ignore_errors=False, onerror=None)


def foundLicense():
	count = 0
	pbar = ProgressBar()

	for root, directories, filenames in os.walk('./repoFolder'):
		for filename in filenames:
			#print filenames
			fullFilePath = os.path.join(root,filename) 
			if not os.path.isfile( fullFilePath ):
				continue
			#print fullFilePath

			try:
				result = subprocess.check_output("ninka " + fullFilePath, shell=True)
			except Exception as e:
				print "ERRO NINKA   " + e
			

			if 'NONE' not in result:
				resultSplited = result.split(";")
					
				if resultSplited[2] is not '0':
					print "** License file found! **"
					print "License: " + resultSplited[1]
					print "FileName: " + resultSplited[0] + "\r"
					count = count + 1
	print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
	print "** Total License Files found: " + str(count) + " **"
	print "======================================================================"
	print '\n'
	return str(count)

if __name__ == '__main__':
	try:
		file = open('output.txt', 'r')
	except Exception as e:
		print "Erro para abrir o arquivo.\n" + e

	try:
		shutil.rmtree('repoFolder', ignore_errors=False, onerror=None)
	except Exception as err:
		pass

	getLastRepository(file)
	
	#foundLicense()

	file.close()
	

