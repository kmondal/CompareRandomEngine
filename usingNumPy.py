import random
import numpy as np

def generate_python_random(seed):
    random.seed(seed)
    return [random.randint(0, 2**32 - 1) for _ in range(10)]

def generate_cpp_mt19937_like(seed):
    # Using numpy's MT19937 engine
    bit_gen = np.random.MT19937(seed)
    rng = np.random.Generator(bit_gen)
    return [rng.integers(0, 2**32, dtype=np.uint32) for _ in range(10)]

def main():
    seed = int(input("Enter the random seed: "))

    py_randoms = generate_python_random(seed)
    cpp_like_randoms = generate_cpp_mt19937_like(seed)

    print("\nPython random module output:")
    print(py_randoms)

    print("\nC++ mt19937-like output via NumPy:")
    print(cpp_like_randoms)

    match = py_randoms == cpp_like_randoms
    print("\nDo the sequences match?", "Yes" if match else "No")

if __name__ == "__main__":
    main()
