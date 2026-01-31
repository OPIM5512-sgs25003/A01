# A01 by OPIM5512-sgs25003

# A01 – GitHub Basics

This repository contains the solution for Assignment A01 (GitHub Basics).

## Purpose
The goal of this assignment is to practice:
- Creating a GitHub repository
- Working with branches (dev → main)
- Committing and pushing code
- Opening and merging pull requests

## Contents
- `src/boxplot.py` – Python script that generates a boxplot of median house values from the California housing dataset  
- `california_housing_train.csv` – Dataset used for the analysis  
- `figs/boxplot.png` – Generated boxplot figure  
- `requirements.txt` – Python dependencies required to run the script  

## How to Run

1. Create and activate a virtual environment:
```bash
py -3.12 -m venv .venv
.\.venv\Scripts\activate

## Install dependencies

pip install -r requirements.txt

## Run the script

python src/boxplot.py

The output figure will be saved to:

figs/boxplot.png



