# Лабораторная работа № 4.
**1.1:** : Написать функцию two_sum, которая возвращает кортеж из двух индексов элементов списка lst, таких что сумма элементов по этим индексам равна переменной target, Элемент по индексу может быть
выбран лишь единожды, значения в списке могут повторяться. Если в
списке встречается больше чем два индекса, подходящих под условие
- вернуть наименьшие из всех. Элементы находятся в списке в произвольном порядке. Алгоритм на двух циклах, сложность O(n^2).

**Результат:**

![Лабораторная работа 4. Задание 1.1](https://github.com/jamanuriyeva/Programming-3-sem/blob/943a9dce873f17dd53ce42a03107e3b17ace93b3/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%964/images/res41.png)

Программа выводит кортеж из двух индексов, которые указывают на числа, сумма которых равна выбранному числу
---

**1.2:** Усовершенствуйте предыдущую задачу ??, добавив функцию two_sum_hashed(lst, target) так, чтобы сложность алгоритма была ниже: O(n) или O(n · log(n)).

**Результат:**

![Лабораторная работа 4. Задание 1.2](https://github.com/jamanuriyeva/Programming-3-sem/blob/943a9dce873f17dd53ce42a03107e3b17ace93b3/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%964/images/res412.png)

В код добавлена функция two_sum_hashed(lst, target), благодаря которой программа запоминает предыдущие результаты и уже намного бытрее может выполнять задачу
---

**1.3:** Усовершенствуйте предыдущую задачу 1.2, добавив функцию , которая возвращает все наборы индексов, удовлетворяющих условию
суммы target.

**Результат:**

![Лабораторная работа 4. Задание 1.3](https://github.com/jamanuriyeva/Programming-3-sem/blob/01fd195d72dae7ea4e1338eb103ca85d1591f976/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%964/images/res413.png)

Теперь программа выводит все наборы индексов, которые удовлетворяют заданному условию
---

**1.4:** Усовершенствуйте предыдущую задачу 1.2, добавив функцию , которая возвращает все наборы индексов, удовлетворяющих условию
суммы target.

**Результат:**

![Лабораторная работа 4. Задание 1.4](https://github.com/jamanuriyeva/Programming-3-sem/blob/01fd195d72dae7ea4e1338eb103ca85d1591f976/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%964/images/res414.png)

Реализация с помощью мемоизации и рекурсии вычисление чисел Фибоначчи
---

**2.1:** Отправка почты через smtplib.

**Результат:**

![Лабораторная работа 4. Задание 2.1](https://github.com/jamanuriyeva/Programming-3-sem/blob/01fd195d72dae7ea4e1338eb103ca85d1591f976/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%964/images/res421.png)

Перед тем как приступить к выполнению этого задания было необходимо создать пароль для внешних приложений. Так как я использовала почту mail.ru, я перешла на их сайт и без труда получила необходимый пароль. На указанную почту прило письмо с сообщением, которое я написала в программе.
---

**2.2:** Парсинг сайта погоды (wheather HTML parsing) на google.com и/или на простом сайте wttrin с помощью BeautifulSoup (v4).

**Результат:**

![Лабораторная работа 4. Задание 2.2](https://github.com/jamanuriyeva/Programming-3-sem/blob/01fd195d72dae7ea4e1338eb103ca85d1591f976/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%964/images/res422.png)

Чтобы программа выводила необходимые данные, нужно было, чтобы программа разделила эти данные от всего, что написано на сайте. 
---

**2.3:** С помощью бибилиотеки matplotlib вывести два окна с графиками
функций по личному выбору. В одном окне два графика двух разных
функций. В другом окне - один график ещё одной функции.

**Результат:**

![Лабораторная работа 4. Задание 2.3](https://github.com/jamanuriyeva/Programming-3-sem/blob/01fd195d72dae7ea4e1338eb103ca85d1591f976/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%E2%84%964/images/res423.png)

Программа выводит два окна, где на первом изображено два графика функций x^2 и tg(x), а на втором окне один график функции 3*cos(2*x)



