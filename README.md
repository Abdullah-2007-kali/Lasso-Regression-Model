# Lasso-Regression-Model
Lasso regression projeckt


---

## 📄 **شرح Lasso Regression (الانحدار مع العقوبة L1)**

### 📌 ما هو Lasso Regression؟

Lasso Regression هو نموذج انحدار خطي مطور يضيف **عقوبة (Regularization)** من نوع **L1** إلى دالة الخسارة (Loss Function).
✅ الهدف الأساسي منه هو:

* تقليل التعقيد (Complexity) في النموذج.
* **اختيار المميزات المهمة فقط** (Feature Selection) عن طريق جعل بعض الأوزان = صفر.
* معالجة مشكلة **Overfitting**.

---

### 🧮 **المعادلة الأساسية**

#### ⚪️ 1. دالة الانحدار العادية:

$$
y = b + w_1x_1 + w_2x_2 + ... + w_nx_n
$$

#### 🔴 2. دالة الخسارة العادية (MSE):

$$
\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
$$

#### 🟢 3. دالة الخسارة مع Lasso (L1 Regularization):

$$
\text{Loss}_{\text{Lasso}} = \text{MSE} + \lambda \sum_{j=1}^{n}|w_j|
$$

* $\lambda$: معامل التحكم في العقوبة (Regularization Strength).
* $|w_j|$: القيمة المطلقة للأوزان.

---

### ⚙️ **كيف تعمل L1 Regularization؟**

* **عند تحديث الأوزان** باستخدام **Gradient Descent**، يتم تعديل معادلة التحديث:

$$
w_j = w_j - \alpha \left(\frac{\partial \text{Loss}}{\partial w_j}\right)
$$

✅ مع L1:

$$
\frac{\partial \text{Loss}}{\partial w_j} = \frac{\partial \text{MSE}}{\partial w_j} + \lambda \cdot \text{sign}(w_j)
$$

* $\text{sign}(w_j)$: إشارة الوزن (موجبة أو سالبة).

---

### 🎯 **مميزات Lasso Regression**

✅ يختار المميزات المهمة فقط تلقائيًا (بعض الأوزان تصبح صفرًا).
✅ يقلل التعقيد في النماذج ذات المميزات الكثيرة.
✅ يمنع Overfitting على البيانات التدريبية.

---

### 🚨 **الفرق بين Lasso و Ridge**

|               | **Lasso (L1)**             | **Ridge (L2)**             |   |              |
| ------------- | -------------------------- | -------------------------- | - | ------------ |
| **العقوبة**   | (\sum                      | w\_j                       | ) | $\sum w_j^2$ |
| **الأوزان**   | يجبر بعض الأوزان على الصفر | يقلل الأوزان لكن لا يصفرها |   |              |
| **الاستخدام** | مناسب لاختيار المميزات     | مناسب عند وجود كل المميزات |   |              |

---

### 🖋️ **مثال برمجي (Lasso Regression من الصفر)**

```python
import numpy as np

# بيانات
x = [1, 2, 3]
y = [2, 4, 6]

# معاملات البداية
w = 0.01
b = 0
alpha = 0.1  # معدل التعلم
lmbda = 0.1  # معامل العقوبة

# التدريب
for epoch in range(100):
    total_error_w = 0
    total_error_b = 0
    for i in range(len(x)):
        y_pred = b + w * x[i]
        error = y_pred - y[i]
        total_error_w += error * x[i]
        total_error_b += error

    # حساب التدرجات
    grad_w = (2 / len(x)) * total_error_w + lmbda * np.sign(w)
    grad_b = (2 / len(x)) * total_error_b

    # تحديث المعاملات
    w -= alpha * grad_w
    b -= alpha * grad_b

    if epoch % 10 == 0:
        print(f"Epoch {epoch}: w={w:.4f}, b={b:.4f}")

print(f"\n✅ النتيجة النهائية: w={w:.4f}, b={b:.4f}")
```

---

### ✅ **الخلاصة**

* **Lasso Regression** مثالي إذا كنت تريد نموذجًا أبسط يقوم باختيار أهم المميزات فقط.
* عن طريق التحكم في $\lambda$، يمكنك تحديد مدى العقوبة المفروضة على الأوزان.

---

## 🌟 **إن أعجبك الشرح لا تنسَ وضع Star للمستودع على GitHub!**

---

### 🚀 هل تريدني:


