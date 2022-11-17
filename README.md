# EasyBlind - a quick script to automate blinding videos

## Background

This is a short blinding script designed to make a copy of mouse behavioural videos named consequtively from 1 to n and randomly assign an alias to each of them. The script will also make a `.csv` file with the original number of the video with its corresponding alias after blinding.

## Pre-requisites

### Python version and modules

To run `blinding.py` the following is required:

* Python v. 3.8+
* `shutil` module
* `pandas` module
* `random` module
* `os` module

Most of the modules should be automatically installed with the python distribution, otherwise it can be installed using `pip`.

I recommend downloading [Anaconda](https://anaconda.org/conda-forge/download) and running the script via a terminal in a [JupyterLab](https://jupyter.org/) environment.

### Video properties

The script is set up to manage up to 26 videos at once with an `.mp4` extension. The extension and number of videos accepted in one go can be modified in the script.

The videos should be named `PREFIXi.mp4`, where `PREFIX` can be any character(s), `i` is an integer between 1 and 26, and `.mp4` is the relevant video extension. The videos have to be numbered consequtively, there cannot be 1, 2, and 4 but no 3 for example.

## Running the script

The script is designed to be run from the directory that contains the unblinded videos. Copy the script into this directory, then open a terminal and navigate to the correct directory (`cd <PATH>`).

The script will ask you for the number of mouse videos in the directory, the prefix, and whether it has correctly understood the naming convention of the videos.

To run the script:

```
> python blinding.py
> Number of mice: <n>
> Video prefix: <PREFIX>
> Video naming convention is: <PREFIXn.mp4>
> Continue with blinding? [y/n] y
```

The script will output a new directory called `blinding` in the parent directory, where blinded videos and a `key.csv` containing the identity of the aliases.

## Use

The script is freely usable and modifiable, however I take no responsibility for any bugs or issues that come up. If you're happy with it consider acknowledging me though!

### Disclaimer

The script is only set up to make a basic copy of the video to rename - some metadata may be lost. The original video is left untouched.
