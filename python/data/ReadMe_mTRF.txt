Author: Kyran Kuijpers
Date: 12-11-2021
System: Windows 10, 64-bit

ELECTIVE REPORT KYRAN
MTRF ANALYSIS

This folder contains python programmes to run mTRF analysis.

This is a step-by-step instruction that explains 
how to set up your system in order to run the code provided in this folder. 

1. Install Anaconda
https://www.anaconda.com/products/individual

2. Create a copy of the Anaconda base environment or use another suitable existing environment.
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

This code was written in Python v3.8.6 in the IDE Spyder 4.1.5. 
The environment should have the following: 
(in brackets the exact version of the packages in the environment the code was written in)
	
	- numpy (v1.20.1)
	- scipy (v1.6.0)
	- matplotlib (v3.2.0)

3. Install MNE v17.2
https://mne.tools/stable/install/mne_python.html

Note: While the scripts were written in an environment with MNE v17.2, 
on my personal system I instead open the Spyder application from another environment (which has instead MNE v22).
For some reason Anaconda can't install Spyder on my environment which has MNE v17.2.
This can easily be bypassed by opening Spyder on the MNE v22 environment and then changing the Python interpreter to 
the MNE v17.2 environment. This can be done in Spyder via the setting Tools -> Preferences -> Python interpreter ->
"Use the following Python interpreter" -> specify the path to the MNE v17.2 environment.
Remember that if you do this, to also restart the Spyder kernel (otherwise you are still working in the old environment). 

4. Contents

.
.
.

4.1. mTRF_theobeat_debugged folder

4.1.1. Scripts:

Before running ANY .py file:
- set the variable programmer to your name (usually first line after importing)
- go to the line that specifies the_folder for the current programmer 
    -> check and set the path to the folder containing the auditory stimuli.
- save the script
	
i) Original scripts:
    - preprocessing_selectedblocks_0.1-8Hz.py
    - Single_subject_analysis_mTRF_SELECT_4-8Hz_sfreq125.py

ii) Corrected scripts:
    - preprocessing_0.1-8Hz_corrected.py
    - Singlesub_analysis_mTRF_4-8Hz_corrected.py

4.1.2. Output:
I copied the output in a way that preserves the existing folder structure. 
Only example output for sham, P02 is included.
	- data_storage_variables_nerhymus
		-> csv's	
	- saved_images
		-> topo's, mTRFs

.
.
.

4.2. mTRF_envelope folder
Note: The scripts and output are based on the corrected mTRF scripts from mTRF_theobeat_debugged folder!

4.2.1. Scripts:
	- Singlesub_analysis_mTRF_4-8Hz_gammatones.py
This script uses the pickle made with the gammatone functions.
	- Singlesub_analysis_mTRF_4-8Hz_envelope.py
This script uses the pickle made for the analytical envelope.

4.2.2. Output:
I copied the output in a way that preserves the existing folder structure. 
Only example output for sham, P02 is included.
Note that these outputs are not finalized, as I used ICA's that were made from
the correct preprocessing script, which components are not yet scrutinized for bads.

	- data_storage_variables_nerhymus
		-> csv's	
	- saved_images
		-> topo's, mTRFs
