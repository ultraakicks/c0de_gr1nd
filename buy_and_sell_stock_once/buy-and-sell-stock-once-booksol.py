"""Min-Max Algorithm

 Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def buy_and_sell_stock_once(self, prices):
        min_price_so_far, max_profit = float('inf'), 0.0
        for price in prices:
            max_profit_sell_today = price - min_price_so_far
            max_profit = max(max_profit, max_profit_sell_today)
            min_price_so_far = min(min_price_so_far, price)
        return max_profit
    
def main():
    s = Solution()
    test_cases = [
        [0.5, 0.3, 0.5, 0.5, 0.2],
        [0.3, 0.5, 0.2, 0.5, 0.8, 0.8, 0.1, 0.4],
        [0.8, 1.6, 1.9, 0.5, 0.9, 0.7, 1.7, 0.9, 0.7, 1.6, 2.0, 0.8, 0.5, 0.2, 0.8, 1.7, 0.5, 0.5, 1.0, 0.5],
        [17.3, 22.3, 23.0, 19.5, 8.2, 5.9, 22.8, 17.3, 27.6, 29.4, 12.8, 11.1, 2.1, 15.0, 0.6, 32.2, 32.4, 9.0, 8.4, 11.4, 2.6, 25.6, 12.6, 35.8, 24.3, 18.3, 28.4, 19.1, 9.6, 13.1, 18.3, 13.9, 24.4, 18.1, 10.1, 24.2, 15.0, 13.1, 27.5, 30.0, 36.0, 9.3, 30.3, 30.0, 8.2, 3.4, 25.6, 29.2, 7.6, 36.2, 6.0, 2.5, 9.1, 2.5, 32.2, 26.5, 4.4, 15.4, 0.1, 6.6, 11.5, 26.4, 31.1, 27.8, 8.8, 17.1, 8.7, 7.3, 4.5, 36.3, 28.1, 10.6, 24.0, 3.5, 12.4, 3.0, 18.8, 18.7, 14.0, 21.1, 3.9, 28.5, 11.8, 30.3, 25.6, 33.0, 34.6, 30.5, 15.1, 27.6, 9.9, 20.8, 22.5, 14.1, 31.1, 27.4, 25.5, 24.4, 30.4, 17.4, 25.8, 27.5, 34.0, 29.1, 6.1, 8.5, 33.3, 33.7, 32.0, 34.7, 17.8, 3.6, 3.6, 9.7, 13.0, 11.8, 21.3, 15.7, 12.2, 4.7, 35.4, 2.6, 17.7, 0.1, 26.9, 7.8, 34.5, 11.1, 4.3, 22.1, 18.3, 16.3, 23.6, 26.7, 2.0, 6.7, 11.2, 10.8, 36.5, 21.3, 17.6, 3.6, 27.6, 5.8, 12.6, 10.0, 18.8, 0.3, 35.2, 29.3, 17.0, 8.5, 31.2, 13.1, 36.3, 35.1, 10.3, 18.6, 11.4, 13.7, 32.3, 11.1, 15.9, 35.3, 20.8, 26.2, 17.6, 15.9, 29.8, 1.5, 28.5, 18.3, 29.5, 32.4, 34.5, 10.9, 24.4, 21.7, 24.5, 8.4, 24.4, 10.9, 6.3, 27.1, 8.5, 4.3, 27.4, 9.3, 8.1, 23.9, 30.8, 29.8, 12.3, 22.4, 10.8, 22.8, 1.2, 16.3, 16.3, 20.1, 13.3, 14.1, 19.7, 35.6, 7.8, 13.1, 8.2, 3.2, 9.9, 15.1, 8.7, 29.1, 24.6, 11.9, 27.8, 9.9, 10.7, 22.8, 14.6, 20.5, 18.4, 19.7, 34.8, 19.5, 16.4, 11.0, 7.5, 8.2, 22.6, 28.4, 13.4, 21.0, 9.0, 4.2, 26.0, 1.8, 12.2, 32.3, 34.6, 9.5, 19.2, 36.3, 5.9, 26.9, 33.2, 19.7, 3.6, 10.5, 2.5, 3.6, 3.1, 13.4, 16.0, 14.7, 12.9, 2.9, 5.7, 29.1, 23.9, 1.5, 12.2, 36.4, 24.3, 0.2, 27.7, 25.1, 13.4, 2.4, 13.1, 32.3, 28.1, 31.4, 21.6, 36.5, 27.3, 27.4, 18.3, 25.2, 15.3, 13.1, 11.4, 33.4, 34.0, 18.1, 9.4, 9.4, 28.3, 13.0, 5.0, 15.0, 28.0, 27.8, 10.3, 17.9, 35.9, 4.3, 30.0, 3.7, 33.8, 1.7, 7.2, 6.3, 22.4, 10.5, 19.0, 26.1, 16.3, 6.3, 20.5, 3.2, 11.1, 20.4, 1.8, 34.3, 18.1, 30.3, 14.4, 26.6, 2.1, 10.5, 24.5, 3.7, 22.8, 18.5, 22.0, 22.3, 0.3, 29.4, 8.4, 4.6, 25.3, 15.9, 27.0, 5.2, 10.1, 26.7, 15.2, 15.3, 16.8, 15.3, 32.0, 8.8, 32.6, 25.8, 30.4, 5.4, 20.9, 28.1, 31.8, 9.7, 16.3, 31.5, 33.5, 17.8, 11.8, 8.3, 14.2, 4.2, 15.9, 19.6, 34.3, 34.7, 10.9, 21.4, 31.8],
        [15.2, 20.7, 12.9, 14.0, 20.7, 2.4, 11.9, 21.2, 24.6, 25.7, 15.9, 14.8, 23.0, 7.1, 1.0, 5.5, 13.2, 21.1, 19.7, 0.8, 17.5, 21.8, 21.9, 4.4, 18.1, 5.1, 12.3, 17.4, 16.3, 20.4, 20.5, 16.1, 13.2, 0.8, 26.6, 17.6, 12.0, 2.7, 5.9, 12.7, 22.9, 12.8, 11.9, 25.8, 13.4, 18.3, 1.1, 7.8, 4.1, 7.6, 10.2, 5.8, 7.1, 22.6, 7.8, 23.7, 15.6, 8.3, 0.9, 3.3, 25.7, 12.8, 24.3, 10.6, 17.7, 25.9, 21.0, 3.5, 2.7, 21.7, 17.2, 26.0, 14.7, 21.4, 8.7, 8.9, 21.1, 13.9, 22.2, 10.7, 6.1, 19.7, 9.6, 24.8, 6.5, 25.1, 20.3, 9.1, 20.5, 8.8, 6.7, 12.1, 23.4, 16.7, 20.5, 23.4, 25.4, 20.9, 26.4, 23.5, 24.4, 8.8, 12.8, 13.7, 11.2, 7.5, 23.3, 23.7, 24.8, 25.0, 26.5, 10.1, 7.2, 9.2, 25.0, 22.2, 18.7, 16.1, 19.1, 26.8, 25.0, 20.6, 15.1, 25.2, 18.1, 11.2, 4.3, 0.1, 7.4, 6.1, 23.2, 6.9, 26.8, 14.4, 9.6, 1.8, 2.4, 8.9, 11.7, 23.9, 13.3, 26.6, 2.3, 12.5, 15.0, 16.9, 21.8, 2.5, 6.8, 18.7, 4.1, 7.0, 19.7, 24.2, 1.7, 23.0, 13.7, 17.4, 14.8, 20.1, 18.5, 24.0, 6.7, 10.7, 8.1, 4.3, 22.6, 24.6, 9.9, 8.7, 22.4, 14.2, 12.6, 0.4, 20.3, 9.3, 23.4, 24.0, 4.5, 19.4, 22.2, 25.6, 21.4, 14.5, 14.9, 20.5, 8.2, 4.3, 8.0, 5.7, 17.7, 0.4, 17.3, 20.0, 18.3, 15.0, 6.4, 13.9, 3.5, 22.1, 5.1, 13.7, 26.1, 8.7, 7.7, 0.7, 24.8, 19.6, 12.0, 6.0, 19.6, 1.3, 21.8, 7.5, 10.9, 12.5, 0.9, 0.6, 15.3, 22.4, 5.9, 17.2, 16.8, 22.0, 13.9, 6.8, 22.5, 19.8, 17.2, 4.2, 20.1, 24.3, 24.0, 0.5, 19.9, 10.6, 23.1, 11.5, 5.6, 10.1, 8.1, 13.0, 18.6, 5.2, 24.1, 16.7, 11.5, 8.0, 4.4, 5.5, 3.0, 0.5, 6.4, 11.0, 16.7, 22.6, 20.9, 3.1, 19.3, 14.6, 17.9, 5.6, 16.9, 11.5, 3.4, 8.3, 13.8, 7.2]
        ]
    for prices in test_cases:
        max_profit = s.buy_and_sell_stock_once(prices)
        print(f'Prices = {prices}')
        print(f'Max Profit = {max_profit}\n')

if __name__ == '__main__':
    main()