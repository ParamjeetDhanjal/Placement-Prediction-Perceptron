# Placement Prediction using Perceptron

A simple perceptron model implemented from scratch in Python to predict student placement based on CGPA and IQ.

## Features
- Train a perceptron manually (row-by-row updates)  
- Predict placement (Yes/No) for a new student  
- Visualize CGPA vs placement:
  - Green dots: Placed  
  - Red dots: Not Placed  
  - Blue dot: Predicted student  

## How to Run
1. Place your dataset as `placement.csv` in the project folder. Example:

CGPA,IQ,Placed  
8.5,120,Yes  
7.0,100,No  
9.0,130,Yes  

2. Run the script: `python perceptron_placement.py`  
3. Enter CGPA and IQ when prompted  
4. See predicted placement and a plot of CGPA vs placement  

## How it Works
- Initialize weights and bias  
- For each student: compute
- Apply step function: output 0 or 1  
- Update weights and bias
- Repeat for all students and epochs  
- Use trained weights to predict new students  

## Author
Paramjeet Dhanjal
