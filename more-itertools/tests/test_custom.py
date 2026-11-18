from more_itertools import interleave, partition


def es_impar(number):
    return number % 2 != 0


def test_partition():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    pares, impares = partition(es_impar, numbers)

    pares_test, impares_test = ([2, 4, 6, 8], [1, 3, 5, 7, 9])

    assert list(pares) == pares_test
    assert list(impares) == impares_test


def test_partition_empty():
    numbers = []

    pares, impares = partition(es_impar, numbers)

    pares_test, impares_test = ([], [])

    assert list(pares) == pares_test
    assert list(impares) == impares_test


def test_partition_pred_is_none():
    values = [0, 1, False, True, '', ' ']

    false_partition, true_partition = partition(None, values)

    true_test = [1, True, ' ']
    false_test = [0, False, '']

    assert list(true_partition) == true_test
    assert list(false_partition) == false_test


def test_interleave():
    number_list_1 = [1, 2, 3]
    number_list_2 = [4, 5, 6]
    number_list_3 = [7, 8, 9]

    result_after_interleave = [1, 4, 7, 2, 5, 8, 3, 6, 9]

    interleave_results = interleave(number_list_1, number_list_2, number_list_3)

    assert list(interleave_results) == result_after_interleave


def test_interleave_different_length_lists():
    number_list_1 = [1, 2, 3]
    number_list_2 = [4, 5]

    result_after_interleave = [1, 4, 2, 5]

    interleave_results = interleave(number_list_1, number_list_2)

    assert list(interleave_results) == result_after_interleave