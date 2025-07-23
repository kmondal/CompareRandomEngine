# CompareRandomEngine
Comparing different random engines from Python, NumPy, and C++ mt19937 using same random seed.

## Compilation
To compile the cpp program, first run
```
g++ -o mt19937 random.cpp
```
This will generate the executable `mt19937` which is to be plugged into `compare_random.py`.

## Usage
To have the comparison between default `random` module of Python and NumPy `random` module, run
```
python usingNumPy.py
```
It will ask for a random seed. Once you provide the seed, it will print 10 random numbers and check whether two sets are same or not.
Sample output:
```
Enter the random seed: 42

Python random module output:
[2746317213, 1181241943, 958682846, 3163119785, 1812140441, 127978094, 939042955, 2340505846, 946785248, 2530876844]

C++ mt19937-like output via NumPy:
[2327846034, 3904886566, 2661450408, 1733955692, 246401338, 3249250296, 3487099619, 1498159427, 3694075699, 3512848995]

Do the sequences match? No
```

To have the comparison between C++ `mt19937` and default `random` module from Python, run:
```
python3 compare_random.py
```
It will ask for a random seed. Once you provide the seed, it will print 10 random numbers and check whether two sets are same or not.
Sample output:
```
Enter the random seed: 42

Python random module output:
[2746317213, 1181241943, 958682846, 3163119785, 1812140441, 127978094, 939042955, 2340505846, 946785248, 2530876844]

C++ mt19937 output:
[1608637542, 3421126067, 4083286876, 787846414, 3143890026, 3348747335, 2571218620, 2563451924, 670094950, 1914837113]

Do the sequences match? No
```

