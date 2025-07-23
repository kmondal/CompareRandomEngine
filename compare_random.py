import random
import subprocess

def generate_python_random(seed):
    random.seed(seed)
    return [random.randint(0, 2**32 - 1) for _ in range(10)]

def generate_cpp_random(seed):
    try:
        result = subprocess.run(
            ["./mt19937", str(seed)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout.strip()
        return [int(num) for num in output.split()]
    except subprocess.CalledProcessError as e:
        print("Error calling C++ program:", e.stderr)
        return []

def main():
    seed = int(input("Enter the random seed: "))

    py_randoms = generate_python_random(seed)
    cpp_randoms = generate_cpp_random(seed)

    print("\nPython random module output:")
    print(py_randoms)

    print("\nC++ mt19937 output:")
    print(cpp_randoms)

    match = py_randoms == cpp_randoms
    print("\nDo the sequences match?", "Yes" if match else "No")

if __name__ == "__main__":
    main()
