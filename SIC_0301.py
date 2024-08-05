import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

## Binomial
n = 10
p = 0.5

print("tính xác suất của việc có chính xác k thành công trong n lần thử, với xác suất thành công trong mỗi lần thử là p:", st.binom.pmf(5, n, p))
print("tính giá trị phân vị cho xác suất q trong phân phối nhị phân:", st.binom.ppf(0.3, n, p))
print("tính xác suất tích lũy của việc có tối đa k thành công trong n lần thử:", st.binom.cdf(5, n, p))
print(st.binom.cdf(7, n, p) - st.binom.cdf(2, n, p))

x = np.arange(0, 11)
plt.scatter(x, st.binom.pmf(x, n, p), color='red')
plt.show()


## poisson
lambda_ = 2

print("tính xác suất của việc có chính xác k sự kiện xảy ra trong phân phối Poisson với tham số lambda_:", st.poisson.pmf(2, lambda_))
print("tính giá trị phân vị cho xác suất q trong phân phối Poisson:", st.poisson.ppf(0.5, lambda_))
print("tính xác suất tích lũy của việc có tối đa k sự kiện xảy ra trong phân phối Poisson:", st.poisson.cdf(5, lambda_))
print(st.poisson.cdf(7, lambda_) - st.poisson.cdf(2, lambda_))

x = np.arange(0, 11)
plt.scatter(x, st.poisson.pmf(x, lambda_), color='green')
plt.show()
