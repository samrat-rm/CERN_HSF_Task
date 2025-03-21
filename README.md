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

HepMc is the most widely used fromat but I think it should be available in all the format for beginners to see, interact and to help understand the difference between them. Also a short "getting started with HepMC data using Python" guide would have helped me a lot.

I struggled a lot while trying to install dependencies like pyhepmc, matplotlib, ipywidgets etc. It would be really helpful if there was a cobra environment YAML for easy installation and maybe homebrew support. Pre-configured environments (Docker, Conda) can be very useful for beginners to avoid dependency issues. 


 
