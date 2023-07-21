def get_categories():
    default_categories = ['транспорт', 'проживание', 'питание', 'развлечения', 'покупки', 'другое']
    print("Выберите опции:")
    print("1. Стандартные категории")
    print("2. Создать свои категории")
    choice = int(input("Введите номер выбранной опции: "))
    if choice == 1:
        return default_categories
    elif choice == 2:
        num_categories = int(input("Введите количество своих категорий: "))
        custom_categories = []
        for i in range(num_categories):
            category = input(f"Введите название категории {i + 1}: ")
            custom_categories.append(category)
        return custom_categories
    else:
        print("Неверный выбор. Выберите 1 или 2.")
        return get_categories()


def main():
    print("Калькулятор расходов на путешествие")
    print("---------------------------------")

    categories = get_categories()

    # Создаем словарь для хранения стоимости по каждой категории расходов
    expenses = {}

    # Вводим стоимость расходов для каждой категории
    for category in categories:
        expense = float(input(f"Введите стоимость в категории '{category}': "))
        expenses[category] = expense

    # Вычисляем общую сумму расходов
    total_expenses = sum(expenses.values())

    # Выводим результат
    print("---------------------------------")
    print("Результат:")
    for category, expense in expenses.items():
        print(f"{category.capitalize()}: {expense} руб.")
    print(f"Общая сумма расходов: {total_expenses} руб.")

    # Предлагаем пользователю выбор
    print("---------------------------------")
    choice = input("Хотите продолжить? (да/нет): ").lower()
    if choice == 'да':
        main()
    else:
        print("Спасибо за использование калькулятора расходов на путешествие!")


if __name__ == "__main__":
    main()