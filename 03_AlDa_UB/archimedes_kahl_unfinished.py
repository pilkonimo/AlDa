from math import sqrt


def archimedes1(k, output=True):
    """Implementation of archimedes algorithm to calculate pi using subtraction."""
    # startvalues for square formatted as (n, inner_side_length, outer_side_length)
    sides = [(4, sqrt(2), 2)]
    for i in range(k-1):
        n, s_n, t_n = sides[-1]
        sides.append((2*n, sqrt(2-sqrt(4-s_n**2)), 2*(sqrt(4+t_n**2)-2)/t_n))
        if output:
            n, s_n, t_n = sides[-1]
            print('n = {val1}, n/2*s_n = {val2}, n/2*t_n = {val3}, n/2*(t_n - s_n) = {val4}'.format(
                val1=n, val2=n*s_n/2, val3=n*t_n/2, val4=n/2*(s_n-t_n)))
    return sides


# archimedes1(50)


def archimedes2(k, output=True):
    """Implementation of archimedes algorithm to calculate pi using addition."""
    # startvalues for square formatted as (n, inner_side_length, outer_side_length)
    sides = [(4, sqrt(2), 2)]
    for i in range(k - 1):
        n, s_n, t_n = sides[-1]
        sides.append((2 * n, s_n/sqrt(2+sqrt(4-s_n**2)), 2*t_n/(sqrt(4 + t_n ** 2)+2)))
        if output:
            n, s_n, t_n = sides[-1]
            print('n = {val1}, n/2*s_n = {val2}, n/2*t_n = {val3}, n/2*(t_n - s_n) = {val4}'.format(
                val1=n, val2=n * s_n / 2, val3=n * t_n / 2, val4=n / 2 * (s_n - t_n)))
    return sides


# archimedes2(100)



def archimedes_test(k=100):
    """Test for archimedes functions, default duplication 100."""
    for i in range(2, 100):
        sides_1, sides_2 = archimedes1(i, False), archimedes2(i, False)
        n_1, s_n_1, t_n_1 = sides_1[-1]
        n_2, s_n_2, t_n_2 = sides_2[-1]
        t_n_test = 2 * s_n_2 / sqrt(4 - s_n_2 ** 2)
        assert t_n_2 == t_n_test, 'archimedes2, n = ' + str(n_2)
        assert t_n_1 == t_n_test, 'archimedes1, n = ' + str(n_1)


archimedes_test()
