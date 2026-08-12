# Modelling Predator-Prey Population Dynamics

This repository contains an individual-based model, programmed in Python, simulating predator-prey population dynamics. Prey and predator animals take random walks on a rectangular spatial grid and interact when they land on the same grid space. Prey reproduce and predators die probabilistically every turn.

`report.pdf` walks through the derivation of the model, and analyses results from runs.

## Use

There are three Marimo notebooks that facilitate conducting of experiments, visualising outputs, and comparing different results.

### Initial Setup

First download a copy of the code. This can be done in two ways:

1. Running `git clone https://github.com/benjchez/Predator-Prey-Population-Dynamics.git` in your terminal, or by
2. Pressing the green **Code** button in GitHub, then in the dropdown pressing **Download ZIP**, and then unzipping the download.

Once downloaded, enter the downloaded folder on your terminal.

This repository uses **uv** to manage the Python environment. Instructions to install **uv** can be found here: [UV Installation](https://docs.astral.sh/uv/getting-started/installation/).

Once **uv** has been installed, run `uv sync` in the command line to sync the python environment. This makes sure that the correct Python packages are installed to run the code.

### Using the Notebooks

Once we have synced the environment, we can open the three notebooks by running these commands in the command line:
- `uv run marimo run IBM/marimo-run.py` - opens a notebook for running an experiment using the individual-based model,
- `uv run marimo run IBM/marimo-visualise.py` - opens a notebook for visualising the results of an experiment, and
- `uv run marimo run IBM/marimo-compare.py` - opens a notebook for comparing results from multiple experiments.

To conduct an experiment, open the first notebook, choose some parameters and press **run**. Once the results have been computed, it will say **Experiment Finished** at the bottom of the notebook. We can then view the results in the second notebook by choosing the folder and name that the experiment was saved under. The notebook displays different figures and pieces of information about the experiment we ran.

After, we can go back to the run notebook and try different parameters to see their output.

The comparison notebook can be used for comparing two runs together or multiple runs if we tick the run-multiple tick box in the run notebook.

## Exploring the Code

The code for the individual-based model can be found in the `IBM/` directory.
- The designed flow of the system is to first decide on the parameters for an experiment run, run it, do post-experiment analysis, and then save the experiment and analysis data. This data can either be passed or extracted from file to be displayed in different forms.
  - The parameters for an experiment run are contained in three dataclasses:
    - `ExperimentOptions` defined in `ExperimentOptions.py` holding high-level settings,
    - `GridOptions` defined in `GridOptions.py` containing options about grid setup and turn behaviour, and
    - `AnimalParameters` defined in `AnimalParameters.py` setting probabilities that relate to animals' death and reproduction events.
  - The `Experimenter` class defined in `Experimenter.py` has methods to run experiments and is initialised with the above parameters being passed to it
    - `run_experiment` is its primary method, which returns `ExperimentData`, a class defined in `ExperimentData.py` containing the results of the run.
  - The `Analyser` class defined in `Analyser.py` is initialised by passing in the `ExperimentData` and contains methods to analyse the results of the run.
    - Its primary method `analyse` returns `AnalysisData`, a class defined in `AnalysisData.py`.
  - `EnAData`, defined in `EnAData.py` is constructed by passing in `ExperimentData` and `AnalysisData`
    - It contains a `to_files` method and `from_files` classmethod to save and extract data from disk respectively
    - `FiledExperimentData` defined in `ExperimentData.py`, and `FiledAnalysisData` defined in `AnalysisData.py`, provide info and useful methods for filed data. The two classes can be combined into `FiledEnAData`.
  - The `DisplayAnalysis` class defined in `DisplayAnalysis.py` provides methods to display the results of an experiment and is initialised by passing in `FiledEnAData`.
