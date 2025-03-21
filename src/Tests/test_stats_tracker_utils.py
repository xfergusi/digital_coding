from stats_tracker_utils import most_active_log_add_input, most_active_log_analyse_top_three


def test_most_active_log_add_input():
    storage = {}
    most_active_log_add_input(storage, 'input1')
    assert storage['input1'] == 1

    most_active_log_add_input(storage, 'input1')
    assert storage['input1'] == 2

    most_active_log_add_input(storage, 'input2')
    assert storage['input2'] == 1


def test_most_active_log_analyse_top_three():
    storage = {'input1': 5, 'input2': 3, 'input3': 8, 'input4': 2}
    top_three = most_active_log_analyse_top_three(storage)
    assert top_three == [('input3', 8), ('input1', 5), ('input2', 3)]

    storage = {'input1': 1, 'input2': 1, 'input3': 1}
    top_three = most_active_log_analyse_top_three(storage)
    assert top_three == [('input1', 1), ('input2', 1), ('input3', 1)]

    storage = {'input1': 10, 'input2': 5}
    top_three = most_active_log_analyse_top_three(storage)
    assert top_three == [('input1', 10), ('input2', 5)]
