def reorderLogFiles(logs: List[str]) -> List[str]:

    letter_lists = []
    digit_lists = []

    for log in logs:

        log_splited = log.split(' ')

        if log_splited[1].isdigit():
            digit_lists.append(log)
        else:
            letter_lists.append(log_splited)

    # note: 這裡用 sort() or sorted() 都可以，但 sort() 是對原先的 list 進行排序而 sorted 是會產出一個新的 list
    # 所以需要給一個新的 variable 去承接 sorted 所產生的 list 才可以做後續的運算
    letter_lists.sort(key=lambda letter_list: (letter_list[1:], letter_list[0]))
    letter_lists = [" ".join(letter_list) for letter_list in letter_lists]

    return letter_lists + digit_lists
