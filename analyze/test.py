import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 生成一組符合標準常態分布的隨機數
data = np.random.normal(loc=0, scale=1, size=1000)

# 創建Q-Q圖
fig = sm.qqplot(data, line='45')
plt.title("Q-Q Plot for Normal Distribution")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
for num in data:
    print(num)
plt.show()