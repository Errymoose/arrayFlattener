from flattener import arrayFlattener


def test_answer():
    flattener = arrayFlattener()

    array = [[1,2,[]],4]
    flattened = flattener.flatten(array)
    print(flattened)
    assert flattened == [1,2,4]