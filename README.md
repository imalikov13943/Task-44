# Task-44

## Объяснение задания

Мы используем цикл, чтобы создать новые столбцы и заполненить их бинарными значениями.

<img width="455" alt="Screenshot 2024-04-06 at 17 05 48" src="https://github.com/imalikov13943/Task-44/assets/102352450/00ff8d59-1883-4450-8954-eab3c903793a">

**categories = set(data['whoAmI']):** Эта строка создает множество уникальных категорий, присутствующих в столбце 'whoAmI' DataFrame data.

**one_hot_data = pd.DataFrame():** Эта строка создает пустой DataFrame one_hot_data, который будет хранить закодированные в формате "one-hot" значения.

**for category in categories:
    one_hot_data[category] = (data['whoAmI'] == category).astype(int)**

Это цикл, который перебирает каждую уникальную категорию. Внутри цикла, для каждой категории добавляется новый столбец в DataFrame one_hot_data. Этот новый столбец содержит бинарные значения, где 1 указывает на наличие категории в столбце 'whoAmI' исходного DataFrame data, а 0 указывает на отсутствие.


### Ответ
<img width="169" alt="Screenshot 2024-04-06 at 17 13 14" src="https://github.com/imalikov13943/Task-44/assets/102352450/eb0674d5-c66f-448e-b57c-745c40832ec2">


