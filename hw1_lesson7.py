
from typing import List

class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Недопустимое значение")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"несовместимый тип объекта")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Матирицы разных размеров")
        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])

if __name__ == '__main__':
    matrix1 = Matrix([[5, 6], [7, 3]])
    print(matrix1, '\n')

    matrix2 = Matrix([[50, 20], [40, 70]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)
