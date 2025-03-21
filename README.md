# CERN_HSF_Task

# Particle Analysis with Jupyter Notebook

## Overview
This project analyzes particle data using `pyhepmc` and `matplotlib`, with interactive visualization using `ipywidgets`. The goal is to filter electrons and muons based on their pseudorapidity (|η|) and plot their transverse momentum (pT).

---

## Setup Instructions

### 1. Create & Activate a Virtual Environment

#### Mac/Linux

```sh
python3 -m venv myenv  
source myenv/bin/activate
```

#### Windows (Command Prompt)
```
python -m venv myenv  
myenv\Scripts\activate  
```

### 2. Install Required Packages

Once the virtual environment is activated, install the necessary dependencies:

```sh
pip install pyhepmc matplotlib ipywidgets numpy
```

3. Start Jupyter Notebook

To launch Jupyter Notebook, run:

```sh 
jupyter notebook 
```
Then open the corresponding .ipynb file and execute the cells.

--- 

Task 2a Plot Sceernshot : 

<img width="803" alt="image" src="https://github.com/user-attachments/assets/78adbb4b-64d5-4fa3-9ea3-6edc97b043e2" />

Cumulative Histogram : 

<img width="2152" alt="image" src="https://github.com/user-attachments/assets/66d5a1f0-cc28-49ed-88e6-e262dcc42058" />


Task 2b Plot Screenshot : 

<img width="1120" alt="image" src="https://github.com/user-attachments/assets/aac525f5-0006-4937-9b4d-1dfaebe1c350" />

--- 

### From this experience of using HepMC files, how do you think MC data should best be provided for open data analysis, and why?

It should be provided in a well-documented format with accessible tools like interactive Jupyter notebooks for analysis can significantly lower the entry barrier for students and non-experts. 

### Brief Reflection on the Task

Working with HepMC data for the first time was an insightful experience. Setting up the environment and parsing the event file was a bit tricky , but once the data was loaded, the task became straightforward. And the transition from a simple python script to an interactive Jupyter notebook highlighted the advantages of visualization and interactive tools, making it easier to explore and interpret the data.

This was my first time using Jupyter and other data visualization tools, and I found the experience both insightful. Overall, it has been one of the most engaging and valuable learning experiences I have had.

 
