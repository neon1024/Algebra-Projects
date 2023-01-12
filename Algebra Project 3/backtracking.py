"""
    Scumpu Ioan Robert 916
"""


def on_the_right_path(k):
    return True


def is_solution(k, solution_length):
    if k == solution_length:
        return True

    return False


def append_solution(solution, all_solutions):
    all_solutions.append(solution)


def bkt(k, solution, solution_length, values, all_solutions):

    if k > solution_length:
        return

    for i in range(len(values)):

        solution[k] = values[i]

        if on_the_right_path(k):
            if is_solution(k, solution_length):
                append_solution(solution[:], all_solutions)
            else:
                bkt(k+1, solution[:], solution_length, values, all_solutions)


def generate_vectors(n):
    solution = []

    for i in range(n):
        solution.append(None)

    values = [0, 1]

    all_solutions = []

    bkt(0, solution[:], n-1, values, all_solutions)

    return all_solutions
