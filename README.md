# Modelling Predator-Prey Population Dynamics

This repository contains an individual-based model, programmed in Python, simulating predator-prey population dynamics. Prey and predator animals take random walks on a rectangular spatial grid and interact when they land on the same grid space. Prey reproduce and predators die probabilistically every turn.

`report.pdf` walks through the derivation of the model, and analyses results from runs.

## Use

There are three Marimo notebooks that facilitate conducting of experiments, visualising outputs, and comparing different results.

### Initial Setup

First download a copy of the code. This can be done in two ways:

1. Running `git clone https://github.com/benjchez/Predator-Prey-Population-Dynamics.git` in your terminal, or by
2. Pressing the green **code** button in GitHub, then in the dropdown pressing **Download Zip**, and then unzipping the download.

Once downloaded, enter the downloaded folder on your terminal.

This repository uses **uv** to manage the Python enviroment. Instructions to install **uv** can be found here: [UV Installation](https://docs.astral.sh/uv/getting-started/installation/).

Once **uv** has been installed, run `uv sync` in the command line to sync the python environment. This makes sure that the correct Python packages are installed to run the code.

### Using the Notebooks

Once we have synced the enviroment, we can open the three notebooks by running these commands in the command line:
- `uv run marimo run IBM/marimo-run.py` - opens a notebook for running an experiment using the individual-based model,
- `uv run marimo run IBM/marimo-visualise.py` - opens a notebook for visualising the results of an experiment, and
- `uv run marimo run IBM/marimo-compare.py` - opens a notebook for comparing results from multiple experiments.

To conduct an experiment, open the first notebook, choose some parameters and press **run**. Once the results have been computed, it will say **Experiment Finished** at the bottom of the notebook. We can then view the results in the second notebook by choosing the folder and name that the experiment was saved under. The notebook displays different figures and pieces of information about the experiment we ran.

After, we can go back to the run notebook and try different parameters to see their output.

The comparison notebook can be used for comparing two runs together or multiple runs if we tick the run-multiple tick box in the run notebook.

### Exploring the Code

The code for the IBM can be found in the **IBM/** directory.
