"""

    Scumpu Ioan Robert 916

"""


from backtracking import generate_vectors


def generate_bases(vectors):

    dimension = len(vectors)

    # for vector1 in vectors:
    #     basis = [vector1]
    #
    #     for vector2 in vectors:
    #         if vector1 != vector2:
    #             basis.append(vector2)
    #
    #             print(basis)
    #
    #             basis.remove(vector2)
    for vector1 in vectors:
        basis = [vector1]

        for vector2 in vectors:
            if vector1 != vector2:
                basis.append(vector2)

                if dimension > 2:

                    for vector3 in vectors:
                        if vector3 != vector2 and vector3 != vector1:
                            basis.append(vector3)

                            if dimension > 3:

                                for vector4 in vectors:
                                    if vector4 != vector3 and vector4 != vector2 and vector4 != vector1:
                                        basis.append(vector4)

                                        print(basis)

                                        basis.remove(vector4)
                            else:
                                print(basis)
                                basis.remove(vector3)
                else:
                    print(basis)
                    basis.remove(vector2)


def main():

    print("Author: Scumpu Ioan Robert 916")

    n = int(input("n: "))

    vectors = generate_vectors(n)

    number_of_basis = (len(vectors) - 2) * (len(vectors) - 1)

    print(f"Number of basis: {number_of_basis}")

    generate_bases(vectors[1:][:])


if __name__ == "__main__":
    main()
