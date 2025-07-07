import numpy as np

x = [1, 2, 3]
y = [2, 4, 6]

w = 0.01  # بداية صغيرة لتفادي مشكلة sign(0)
b = 0
a = 0.1   # معدل التعلم
l = 0.1   # معامل العقوبة L1

for epoch in range(100):  # عدد أكبر من التكرارات
    total_error_w = 0
    total_error_b = 0

    for i in range(len(x)):
        y_p = b + w * x[i]
        error = y_p - y[i]
        total_error_w += error * x[i]
        total_error_b += error

    # حساب التدرجات
    gd_w = (2 / len(x)) * total_error_w + l * np.sign(w)  # L1 Regularization
    gd_b = (2 / len(x)) * total_error_b

    # تحديث المعاملات
    w -= a * gd_w
    b -= a * gd_b

    if epoch % 10 == 0:
        print(f"Epoch {epoch}: w={w:.4f}, b={b:.4f}")

print(f"\n✅ Final result: w={w:.4f}, b={b:.4f}")
