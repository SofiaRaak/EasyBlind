"""
This module is for automating blinding of behavioural videos of mice,
where the naming convention follows "PREFIXi.mp4", where PREFIX is
a string (e.g. MOUSE in video named MOUSE1.mp4) and i is a number between
2 and 26. NB! Prefix is case sensitive!

To use, copy the module into the folder with the videos to be blinded
and run from the terminal as follows:

> python blinded.py
> Number of mice: 15
> Video prefix: MOUSE
> Video naming convention is: MOUSE1.mp4
> Continue with blinging? [y/n] y

As the script runs, a new directory called "blinded" will be created in
the root directory with copies of the videos that have now been blinded.
There will also be a .csv file containing the key called "key".

Make sure the following modules are installed:

sys
shutil
os
pandas
random
"""

#import required modules
import shutil
import os
import pandas as pd
from random import shuffle

#query user for number of mice, video prefix:
num_mice = int(input("Number of mice: "))
vid_prefix = input("Video prefix: ")

#check names OK:
example_name = str(vid_prefix) + str(1) + ".mp4"
print("Video naming convention is: " + example_name)
names_OK = input("Continue with blinding? [y/n]")

while names_OK.lower() == "y":
    #list of aliases
    blinded = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', \
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', \
               'u', 'v', 'w', 'x', 'y', 'z']
    
    #subset and randomise blinded based on number of mice
    random_blind = blinded[:num_mice]
    shuffle(random_blind)
    
    #make new directory to hold blinded videos, key
    if not os.path.exists("./blinded"): #checks if folder exists
        os.mkdir(r'./blinded')
    
    #copy and rename files to blinded folder:
    for i in range(num_mice):
        orig_path = str(vid_prefix)+str(i+1)+".mp4"
        blinded_path = "blinded/"+str(vid_prefix)+str(random_blind[i])+".mp4"
        shutil.copy(orig_path, blinded_path)
        
    #create key
    orig_id = list(range(1, num_mice + 1))
    blinded_id = []
    for i in range(num_mice):
        blinded_id.append(random_blind[i])
    
    #export key
    data = {"orig_id": orig_id, "blinded_id": blinded_id}
    key = pd.DataFrame(data = data)
    key.to_csv('blinded/key.csv', index=False)
    
    #exit loop
    break