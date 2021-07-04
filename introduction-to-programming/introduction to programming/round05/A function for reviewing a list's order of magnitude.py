def is_the_list_in_order(check_list):
    ordered_list=[]+check_list
    ordered_list.sort()
    if ordered_list==check_list:
        return True
    else:
        return False


