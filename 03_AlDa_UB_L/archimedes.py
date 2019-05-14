from math import sqrt, trunc


def archimedes1(k, output=True):
    """Implementation of archimedes algorithm to calculate pi using subtraction."""
    # startvalues for square formatted as (n, inner_side_length, outer_side_length)
    sides = [(4, sqrt(2), 2)]
    for i in range(k):
        n, s_n, t_n = sides[-1]
        sides.append((2*n, sqrt(2-sqrt(4-s_n**2)), 2*(sqrt(4+t_n**2)-2)/t_n))
        if output:
            n, s_n, t_n = sides[-1]
            print('n = {val1}, n/2*s_n = {val2}, n/2*t_n = {val3}, n/2*(t_n - s_n) = {val4}'.format(
                val1=n, val2=n*s_n/2, val3=n*t_n/2, val4=n/2*(s_n-t_n)))
    return sides


# archimedes1(20)


def archimedes2(k, output=True):
    """Implementation of archimedes algorithm to calculate pi using addition."""
    # startvalues for square formatted as (n, inner_side_length, outer_side_length)
    sides = [(4, sqrt(2), 2)]
    for i in range(k):
        n, s_n, t_n = sides[-1]
        sides.append((2 * n, s_n/sqrt(2+sqrt(4-s_n**2)), 2*t_n/(sqrt(4 + t_n ** 2)+2)))
        if output:
            n, s_n, t_n = sides[-1]
            print('n = {val1}, n/2*s_n = {val2}, n/2*t_n = {val3}, n/2*(t_n - s_n) = {val4}'.format(
                val1=n, val2=n * s_n / 2, val3=n * t_n / 2, val4=n / 2 * (s_n - t_n)))
    return sides


# archimedes2(100)


def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return trunc(stepper * number) / stepper


def archimedes_test1(k=20, digits=10):
    """Test for archimedes functions, default amount of duplications 20."""
    sides = archimedes1(k, False)
    for i in range(2, k):
        n, s_n, t_n = sides[i]
        t_n_test = 2 * s_n / sqrt(4 - s_n**2)
        # truncate to 8 decimal places
        t_n = truncate(t_n, digits)
        t_n_test = truncate(t_n_test, digits)
        assert t_n == t_n_test, 'archimedes1, n = ' + str(n)


def archimedes_test2(k=20, digits = 10):
    """Test for archimedes functions, default amount of duplications 20."""
    sides = archimedes2(k, False)
    for i in range(1, k):
        n, s_n, t_n = sides[i]
        t_n_test = 2 * s_n / sqrt(4 - s_n**2)
        # truncate to 8 decimal places
        t_n = truncate(t_n, digits)
        t_n_test = truncate(t_n_test, digits)
        assert t_n == t_n_test, 'archimedes2, n = ' + str(n)


def archimedes_test(d=10):
    archimedes_test2(digits=d)
    archimedes_test1(digits=d)


archimedes_test()
