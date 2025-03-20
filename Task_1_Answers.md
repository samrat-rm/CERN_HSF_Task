### 1. What are the advantages of using Jupyter notebooks for analysing and visualising particle physics data?

Jupyter Notebook is most commonly used for high-energy and particle physics 
#### Unique features :  
- Unlike R studio it supports multiple language which RStudio, Spyder and Plain Python/c++ scripts can't do 
- It has remote access and cloud capability, without needing local installation 
- It is browser based and very easy have remote access 
- It can handle large Data sets better than RStudio by parallel DASK computing. 
- It is best suited for High Energy Physics tools integration 
- Interactive Execution and Inline Visualisation allows us to debugging in real-time and best for data analysis. 
##### **Interactive Execution** and Inline Visualisation 

- You can run code **one cell at a time**, see the output, modify it, and rerun it.
- Unlike traditional scripts where you run everything at once, Jupyter allows **step-by-step execution**
- Basically, Jupyter lets you **incrementally build** your program without restarting everything.
- You can display **graphs, charts, and images directly in the notebook** without opening a separate window.

#### When not to use Jupyter notebook for Particle Physics : 
- When advanced statistics and visualisation is need we can use RStudio
- Difficult to work with Git Version Control because Jupyter notebooks are stored in **JSON format**, which makes them hard to **merge in Git**.
- For small teams  and quick analysis Jupyter is great but for large collaborations (like ATLAS, CMS) tools like ROOT, Git, and workflow tools are better suited.
- Jupyter Notebook lacks Structured Project Management because large HEP collaborations (e.g., ATLAS, CMS) need well-organized pipeline, not scattered notebooks.
- If the objective is to collaborate with multiple teams and publication-ready reports like conference papers and experimental documentation. 


--- 

### 2. Describe the difference between real collider data and Monte Carlo simulated events. Why are both important in physics research?

MC simulation tells us how particles should behave based on known physics (QCD, electroweak theory). It is generated using physics models like PYTHIA, HERWIG, MadGraph, etc.

It tells us what to expect from a experiment before the experiment happens like prediction based on past experiments data. Which helps us optimize experiments 

Real collider data is the actual collision data that comes from detectors. It is used to test theories and find new particles. 

Comparison between real and MC simulation is used to correct models and improve simulation model precision.  

Challenges of MC Simulation : 
These simulation models rely on approximation and must be validated with real experiment data. 

--- 

### 3. Explain the importance of reducing barriers to open-data analysis for non-experts and students 

Reducing the barriers will help students engage and get hands on experience with real scientific data which will promote innovation and interest in students. 

As a student not from a physics background. I tried to explore opendata.cern.ch and I was overwhelmed by the complexity and lack of context. I believe the most import part of open data analysis is to have documents that are very beginner friendly and hands on experience in data visualisation and data analysis tools like Jupiter , RStudio, etc. 