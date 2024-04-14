def maximize_capital(N: int, C: int, gains: list[int], prices: list[int]) -> int:
    laptops = sorted(zip(gains, prices), key=lambda x: x[0] / x[1], reverse=True)

    for gain, price in laptops:
        if C >= price:
            C += gain
            N -= 1
            if N == 0:
                break
    return C



if __name__ == '__main__':
    N = 3
    C = 10
    gains = [5, 2, 8, 1, 3]
    prices = [4, 3, 10, 2, 6]
    final_capital = maximize_capital(N, C, gains, prices)
    print(f"Final capital: {final_capital}")