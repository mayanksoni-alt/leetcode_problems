int maxProfit(int* prices, int pricesSize) {
    int buy = prices[0];
    int maxProfitValue = 0;

    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] < buy) {
            buy = prices[i];
        }

        int sell = prices[i] - buy;

        if (sell > maxProfitValue) {
            maxProfitValue = sell;
        }
    }

    return maxProfitValue;
}