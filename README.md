# Parallel and Serial implemetation of AES Algorithm

In this repository, the AES-128 algorithm has been implemented in both a serial and a parallel fashion. The implementation includes the key-generation from a given 16-bit encryption key, as well as the encryption process. 

The implementation compares the advantages of using Numpy and Numba libraries against using only python.

The Parallel algorithm uses Numba library for parallelising and vectorizing the functions and uses Numpy to handle the data efficiently.

The Serial algorithm does not use any library and runs in a serial order.

## Built using-

- [Numpy](https://numpy.org)
- [Numba](https://numba.pydata.org)
- [Pandas](https://pandas.pydata.org)

## Setting up the Environment

To set up the sources, pre-requisites include-

- Python 3.6 or above
- Dependencies from requirements.txt

First, clone this repository onto your system. Then, create a virtual environment:

```
cd path/to/folder
virtualenv venv -p python3.6   //or any other name and version
source venv/bin/activate
```

Now, install the python dependencies from requirements.txt:
```
pip install -r requirements.txt
```

Next, you can add your virtual environment to Jupyter by typing:
```
pip install --user ipykernel
python -m ipykernel install --user --name=venv
```

This should print the following:
```
Installed kernelspec venv in /home/user/.local/share/jupyter/kernels/venv
```

That's it!! While opening the files in Jupyter or Jupyter notebook, choose the saved kernel name (here "venv") instead of python or python3.
