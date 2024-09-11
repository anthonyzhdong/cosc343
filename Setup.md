# Setting up Python Environment for COSC343/AIML402

This README provides instructions on how to set up VSCode and a Python virtual environment to mirror the Owheo lab setup for COSC343/AIML402 courses. This setup can be done on Windows, macOS, or Linux.

## Prerequisites

- Anaconda (for managing virtual Python environments)
- Visual Studio Code (VSCode)

## Installation Steps

### 1. Install Anaconda

1. Download Anaconda from [https://www.anaconda.com/download/success](https://www.anaconda.com/download/success)
2. Follow the installation instructions for your operating system

Anaconda is free and provides the means of creating Python environments that do not interfere with your system's default Python installation.

### 2. Create a Virtual Python Environment

After installing Anaconda, create a virtual Python environment named `cosc343`. This environment will be used for both COSC343 and AIML402 courses.

Open a terminal (Anaconda prompt on Windows) and run the following commands:

```bash
conda create --name cosc343 python=3.11
conda activate cosc343
pip install numpy matplotlib pygame tensorflow tensorflow-datasets scikit-learn scikit-image scipy python-ev3dev2 pandas readchar
```

### 3. Install Visual Studio Code (VSCode)

1. Download VSCode from [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
2. Follow the installation instructions for your operating system

## Running Labs

To run the labs:

1. Open your project in VSCode
2. Follow the instructions in Lab 1 and Lab 2 for opening a Python project in VSCode
3. Point VSCode to the Python interpreter from the `cosc343` environment

You should now be ready to run the labs for COSC343/AIML402.