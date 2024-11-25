def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_two_digit_primes():
    two_digit_primes = []
    for num in range(10, 100):
        if is_prime(num):
            two_digit_primes.append(num)
    return two_digit_primes


two_digit_primes = find_two_digit_primes()
print("Two-digit prime numbers:", two_digit_primes)