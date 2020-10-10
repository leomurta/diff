import argparse


def read(filename):
    with open(filename) as f:
        return [None] + f.read().split('\n')


def lcs(seq1, seq2):
    matrix = [[0 for i in range(len(seq2))] for j in range(len(seq1))]

    for i in range(1, len(seq1)):
        for j in range(1, len(seq2)):
            e1 = seq1[i]
            e2 = seq2[j]

            if e1 == e2:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

    return matrix


def write(seq1, seq2, matrix):
    RESET = '\33[0m'  # Reset style
    ADD = '\33[32m'  # green
    DEL = '\33[9;31m'  # striked out, red

    i = len(seq1) - 1
    j = len(seq2) - 1
    diff = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and seq1[i] == seq2[j]:
            diff.append(seq1[i])
            i, j = i-1, j-1
        elif i > 0 and (j == 0 or matrix[i][j-1] < matrix[i-1][j]):
            diff.append(DEL + seq1[i] + RESET)
            i -= 1
        else:
            diff.append(ADD + seq2[j] + RESET)
            j -= 1

    print('\n'.join(reversed(diff)))


def main():
    parser = argparse.ArgumentParser(description='Compares two files.')
    parser.add_argument('file1', help='name of the first file')
    parser.add_argument('file2', help='name of the second file')
    args = parser.parse_args()

    seq1 = read(args.file1)
    seq2 = read(args.file2)
    matrix = lcs(seq1, seq2)
    write(seq1, seq2, matrix)


if __name__ == "__main__":
    main()
