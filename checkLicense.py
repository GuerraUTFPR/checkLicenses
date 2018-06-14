import os
import subprocess
import re
import shutil
from progressbar import ProgressBar




def getLastRepository(file):
	
	for line in file:
		
		package = line.split(',')
		packageName = package[0].strip()
		repositoryLink = package[1].strip()
		qtdLicenses = package[2].strip()
		aux = ''

		if repositoryLink != aux and repositoryLink != "None":
			#result.write(line)
			#result.write(repostoryLink)
			
			cloneRepository2(repositoryLink)
			aux = repositoryLink

	result.close()


def cloneRepository2(urlRepository):
	notFoundRepo = []

	newUrlRepository = re.sub('.*://', 'https://Anomalo:123mudar@', urlRepository)
	newUrlRepository = urlRepository.replace('git+ssh://git@github', 'https://Anomalo:123mudar@')
	#newUrlRepository = urlRepository.replace('https://', 'https://Anomalo:123mudar@')
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print newUrlRepository
	print "-------------"
	
	print '\n'
	#print "======================================================================"
	#print urlRepository
	#print "======================================================================"
	try:
		subprocess.check_output("cd repoFolder; git clone " + newUrlRepository, shell=True)

	except Exception as e:
		pass
		


def cloneRepository(urlRepository, licenseCount):
	notFoundRepo = []

	newUrlRepository = re.sub('.*://', 'https://Anomalo:123mudar@', urlRepository)
	newUrlRepository = re.sub('git+ssh://git@github', 'https://Anomalo:123mudar@', urlRepository)
	
	print '\n'
	print "======================================================================"
	print urlRepository
	print "======================================================================"
	try:
		subprocess.check_output("git clone " + newUrlRepository + " repoFolder" , shell=True)
		licenses = foundLicense()
		pass

	except Exception as e:
		if os.path.isdir("repoFolder"):
			shutil.rmtree('repoFolder', ignore_errors=False, onerror=None)
		
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

#	try:
#		shutil.rmtree('repoFolder', ignore_errors=False, onerror=None)
#	except Exception as err:
#		pass

	getLastRepository(file)
	
	#foundLicense()

	file.close()
	

