# Linear Algebra Visualizer

A Python script that visualizes core linear algebra operations such as vector addition, scalar scaling, cross products, and linear transformations in interactive 3D plots.

## Problem

Linear algebra operations like vector addition or cross products are often easier to understand visually than through equations alone. This project renders vectors and their transformations in 3D space, making the geometric meaning behind the math immediately visible.

## What It Does
Plots two base vectors (v and u) in 3D space
Optionally shows vector addition (v + u), placing one vector at the tip of the other to visualize the resulting sum
Optionally shows scalar scaling (2v), demonstrating how multiplying a vector by a scalar stretches it
Optionally shows the cross product (v × u), the vector perpendicular to both inputs
Optionally shows a linear transformation applied to a vector via matrix multiplication (A·v)

Each operation can be toggled independently using boolean flags at the top of the script (SHOW_ADDITION, SHOW_SCALING, SHOW_CROSS, SHOW_TRANSFORM), so you can isolate and study one concept at a time.

## Tools Used
Python
NumPy (vector math: addition, cross product, matrix multiplication)
Matplotlib (3D plotting via mpl_toolkits.mplot3d)
## How to Run It
Install dependencies: pip install numpy matplotlib
Set the SHOW_* flags at the top of the script to True/False for the operations you want to visualize
Run the script: python <filename>.py
An interactive 3D plot window will open showing the selected vectors and operations
