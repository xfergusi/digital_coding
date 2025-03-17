def most_active_log_add_input(storage, input):
    if storage.get(input):
        storage[input] = storage.get(input) + 1 
    else:
        storage[input] = 1

def most_active_log_analyse_top_three(storage):
    # Get the top three items sorted by value in descending order
    top_three = sorted(storage.items(), key=lambda item: item[1], reverse=True)[:3]
    return top_three