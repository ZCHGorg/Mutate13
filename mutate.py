import random
import ast
import time

def mutate_code(code, mutation_rate):
    mutated_code = code.copy()
    for i in range(len(mutated_code)):
        if random.random() < mutation_rate:
            mutated_code[i] = generate_random_line()
    return mutated_code

def generate_random_line():
    # Define a list of valid Python statements and expressions
    possible_lines = [
        "x = x + 1",
        "y = y * 2",
        "print('Hello, world!')",
        "if condition:",
        "for item in collection:"
        # ... add more valid lines ...
    ]
    return random.choice(possible_lines)

def is_valid_python(code):
    try:
        ast.parse("\n".join(code))
        return True
    except SyntaxError:
        return False

def main():
    initial_code = [
        "x = 0",
        "y = 1",
        "for i in range(10):",
        "    print(i)"
    ]
    mutation_rate = 0.2
    num_mutations = 10
    num_iterations = 5

    print("Initial Code:")
    for line in initial_code:
        print(line)

    for iteration in range(num_iterations):
        print(f"\nIteration {iteration + 1}:\n")
        mutated_code = initial_code
        for i in range(num_mutations):
            mutated_code = mutate_code(mutated_code, mutation_rate)
            while not is_valid_python(mutated_code):
                mutated_code = mutate_code(mutated_code, mutation_rate)
            print(f"Mutation {i + 1}:")
            for line in mutated_code:
                print(line)
            time.sleep(1)  # Add a delay to observe changes

if __name__ == "__main__":
    main()
