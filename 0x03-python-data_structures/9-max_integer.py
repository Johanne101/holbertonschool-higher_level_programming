#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Function finds the biggest int/number (n_value) in list,
    and returns the max int value (m_value)
    """
    if len(my_list) == 0:
        return None

    else:
        m_value = my_list[0]

        for n_value in my_list:
            if n_value > m_value:
                m_value = n_value
        return m_value
