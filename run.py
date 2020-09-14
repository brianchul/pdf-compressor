import os
import subprocess
from time import sleep
import glob

pdfIn = ""
pdfOut = ""
def detectPDF():
    for filepath in glob.glob(os.path.join(pdfIn, '*.pdf')):
        filenameType = filepath.split("/")[-1]
        filename = filenameType.split(".")[0]
        cmd = "ps2pdf "
        cmd += filepath
        cmd += " "
	cmd += pdfOut
        cmd += filename
        cmd += "_compress.pdf"

        deleteCmd = "rm " + filepath

        cmd += " && " + deleteCmd
        print("compressed", filepath)
        subprocess.Popen(cmd, shell=True)

while(1):
    detectPDF()
    sleep(10)
