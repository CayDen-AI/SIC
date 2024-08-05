import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

## uniform
a = 2000
b = 5000
base = b - a

print("mật độ xác suất của một giá trị x trong phân phối đều với khoảng từ a đến b:", st.uniform.pdf(4500, a, base))
print("giá trị phân vị trong phân phối đều:")
print(st.uniform.ppf(0.5, a, base))
print(st.uniform.ppf(0.01, a, base))
print(st.uniform.ppf(0.99, a, base))
print("P(a <= x <= 2500):", st.uniform.cdf(3500, a, base))
print("P(2500 <= x <=3000):", st.uniform.cdf(3000, a, base) - st.uniform.cdf(2500, a, base))

x = np.linspace(1000, 6000, 1000)
plt.plot(x, st.uniform.pdf(x, a, base), color='red')
plt.show()

## normal
mu = 5
sigma = 2

print("mật độ xác suất của giá trị x trong phân phối chuẩn với trung bình loc và độ lệch chuẩn scale:",
      st.norm.pdf(0, loc=mu, scale=sigma))
print("giá trị phân vị cho xác suất q trong phân phối chuẩn với trung bình loc và độ lệch chuẩn scale:")
print(st.norm.ppf(0.5, loc=mu, scale=sigma))
print(st.norm.ppf(0.01, loc=mu, scale=sigma))
print(st.norm.ppf(0.99, loc=mu, scale=sigma))
print("P(x <= 5):", st.norm.cdf(5, loc=mu, scale=sigma))
print("P(3 <= x <= 7):", st.norm.cdf(7, loc=mu, scale=sigma) - st.norm.cdf(3, loc=mu, scale=sigma))
print("P(-1 <= x <= 11)", st.norm.cdf(11, loc=mu, scale=sigma) - st.norm.cdf(-1, loc=mu, scale=sigma))

x = np.linspace(-10, +10, 1000)
mu = 0
sigma = 2
plt.plot(x, st.norm.pdf(x, loc=mu, scale=sigma), color='red')
plt.show()

x = np.linspace(-10, +10, 1000)
sigma = 2
mu_1 = -1
mu_2 = 0
mu_3 = +1
plt.plot(x, st.norm.pdf(x, loc=mu_1, scale=sigma), color='red')
plt.plot(x, st.norm.pdf(x, loc=mu_2, scale=sigma), color='green')
plt.plot(x, st.norm.pdf(x, loc=mu_3, scale=sigma), color='blue')
plt.show()
