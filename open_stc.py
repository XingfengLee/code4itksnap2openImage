import os,sys
import subprocess
import glob
from multiprocessing import Pool

def run_command(command):
    subprocess.Popen(command, shell=True)

def run_itksnap(gFile1,gFile2,sFile1,sFile2,aFile):
    print(subject)
    oStr1 = ' itksnap -g ' + gFile1 +  ' -o ' + gFile2 + ' ' + aFile
    print(oStr1)

    oStr2 = ' itksnap -g ' + gFile2 +  ' -o ' + gFile1 + ' ' + aFile
    print(oStr2)

    pool = Pool()
    pool.map(run_command, [oStr1])

    process = subprocess.Popen([oStr2],shell=True)
    process.wait()


path1  = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) <= 2: # start from the beginning 
    
    i = 0; 
    for subject_dir in sorted(glob.glob(os.path.join(os.path.dirname(__file__), path1, "*"))):

        ppart   = subject_dir.split('/') 
        subject = str(ppart[len(ppart)-1])
        subID   = subject.split('_')
        pID     = subID[0]

        gFile1 =  './'+ subject + '/' +pID + '_T2w.nii.gz'
        sFile1 =  './'+ subject + '/' +pID +'_T2w*_seg.nii.gz'

        gFile2 =  './'+ subject + '/' +pID +'_DW.nii.gz'
        sFile2 =  './'+ subject + '/' +pID +'_DW*_seg.nii.gz'
        aFile  =  './'+ subject + '/' +pID +'_ADC.nii.gz'

        if os.path.isdir(subject_dir) and pID[0:3] == 'STC': # show only STL files
            if len(sys.argv)== 1:
                run_itksnap(gFile1,gFile2,sFile1,sFile2,aFile)

            elif len(sys.argv) == 2: # start from the specified file
                caseID = str(sys.argv[1])
                # print(caseID)
                # print(pID)
              
                if not caseID : # no input arg parameters
                    run_itksnap(gFile1,gFile2,sFile1,sFile2,aFile)
                else: # have input parameters
                    if i == 0:
                        print('start to read case : ' + caseID+ ' , then load the rest STC files in the folder.')
                    if str(pID) == caseID or i> 0:
                        run_itksnap(gFile1,gFile2,sFile1,sFile2,aFile)
                        i = 1;
else:
    print('please input only 2 parameters')

