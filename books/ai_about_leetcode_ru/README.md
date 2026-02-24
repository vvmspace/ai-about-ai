# AI about LeetCode RU — Оглавление

Практическая книга из 50 глав по самым популярным задачам LeetCode: от базовых паттернов до уверенного интервью-мышления.
Каждая глава даёт теорию, рабочую эвристику, короткий пример ответа на интервью и прикладной мостик к реальным задачам в продакшене.

## Главы

1. **[00. Two Sum: задача, на которой видно всё](./00_two_sum_the_most_famous_start_ru.md)**  
   Учимся мгновенно выбирать между brute force и hash map и объяснять это языком бизнеса.
2. **[01. Valid Parentheses: стек без магии](./01_valid_parentheses_stack_sanity_ru.md)**  
   Почему правильная модель состояния важнее «запоминания решения».
3. **[02. Merge Two Sorted Lists: линейное слияние как базовый рефлекс](./02_merge_two_sorted_lists_linear_merge_ru.md)**  
   Одна из самых частых проверок на аккуратность указателей и краевых случаев.
4. **[03. Best Time to Buy and Sell Stock: одно прохождение, один минимум](./03_best_time_to_buy_and_sell_stock_one_pass_ru.md)**  
   Простой проход показывает, умеете ли вы держать инвариант.
5. **[04. Contains Duplicate: хеш-таблица как фильтр шума](./04_contains_duplicate_hashset_signal_ru.md)**  
   Короткая задача на скорость мышления и оценку сложности.
6. **[05. Maximum Subarray: когда локальный выбор работает глобально](./05_maximum_subarray_kadane_signal_ru.md)**  
   Классика Kadane и практика объяснения динамики без формул ради формул.
7. **[06. Product of Array Except Self: префиксы и постфиксы без деления](./06_product_of_array_except_self_prefix_postfix_ru.md)**  
   Тест на понимание памяти и аккуратность проходов.
8. **[07. Valid Anagram: частоты против сортировки](./07_valid_anagram_frequency_models_ru.md)**  
   Выбор оптимального подхода под ограничения входа.
9. **[08. Binary Search: дисциплина границ](./08_binary_search_boundary_discipline_ru.md)**  
   Половина ошибок на интервью — в условиях left/right.
10. **[09. Linked List Cycle: медленный и быстрый указатели](./09_linked_list_cycle_floyd_two_pointers_ru.md)**  
    Floyd-подход как универсальный паттерн обнаружения цикла.
11. **[10. Group Anagrams: канонический ключ для группировки](./10_group_anagrams_canonical_key_ru.md)**  
    Как строить стабильные ключи для группировки в реальных сервисах.
12. **[11. Climbing Stairs: минимальная динамика без тумана](./11_climbing_stairs_minimal_dp_ru.md)**  
    Вход в DP через простую рекуррентную модель.
13. **[12. Reverse Linked List: разворот структуры под контролем инварианта](./12_reverse_linked_list_invariant_control_ru.md)**  
    Проверка аккуратности мутаций структуры.
14. **[13. Top K Frequent Elements: куча против bucket-подхода](./13_top_k_frequent_elements_heap_bucket_ru.md)**  
    Trade-off между асимптотикой и константами.
15. **[14. Number of Islands: DFS/BFS на сетке без хаоса](./14_number_of_islands_dfs_bfs_grid_ru.md)**  
    Как правильно моделировать обход двумерного мира.
16. **[15. Invert Binary Tree: рекурсия без лишней драмы](./15_invert_binary_tree_recursion_confidence_ru.md)**  
    Базовая задача на понимание обхода дерева.
17. **[16. Lowest Common Ancestor of BST: использовать порядок, а не силу](./16_lca_bst_order_property_ru.md)**  
    Используем свойства BST вместо полного обхода.
18. **[17. Implement Queue using Stacks: амортизированная стоимость](./17_queue_using_stacks_amortized_cost_ru.md)**  
    Проверка глубины понимания абстракций.
19. **[18. Kth Smallest Element in a BST: inorder как отсортированный поток](./18_kth_smallest_bst_inorder_stream_ru.md)**  
    Связка теории дерева и практики ранней остановки.
20. **[19. Ransom Note: частотный бюджет без паники](./19_ransom_note_frequency_budget_ru.md)**  
    Простой кейс на контроль ресурсов и читаемость.
21. **[20. 3Sum: сортировка, два указателя и контроль дублей](./20_3sum_two_pointers_dedup_ru.md)**  
    Первая серьёзная задача на устранение дублей.
22. **[21. Longest Substring Without Repeating Characters: скользящее окно под контролем](./21_longest_substring_sliding_window_ru.md)**  
    Один из главных паттернов строковых задач.
23. **[22. Container With Most Water: два указателя и строгая логика шага](./22_container_with_most_water_two_pointers_ru.md)**  
    Почему сдвиг меньшей стены — не эвристика, а логика.
24. **[23. Search in Rotated Sorted Array: бинарный поиск в сломанном порядке](./23_search_rotated_sorted_array_binary_logic_ru.md)**  
    Интервью-проверка на спокойствие в нестандартных условиях.
25. **[24. Trapping Rain Water: одна задача, три инженерные модели](./24_trapping_rain_water_three_models_ru.md)**  
    Одна задача — три валидные стратегии.
26. **[25. Merge Intervals: сортировка интервалов как рабочий рефлекс backend](./25_merge_intervals_sort_and_sweep_ru.md)**  
    Типовая операция для расписаний, биллинга и аналитики.
27. **26. Insert Interval: аккуратная вставка слиянием**  
    Вариант «merge intervals» с дополнительными условиями.
28. **27. Non-overlapping Intervals: жадность на минимизацию удалений**  
    Ключ к задаче — правильный критерий выбора.
29. **28. Meeting Rooms II: минимальное число комнат**  
    Классическая задача на очереди приоритетов.
30. **29. Course Schedule: граф и цикл зависимостей**  
    Прямой мост к реальным dependency-графам.
31. **30. Pacific Atlantic Water Flow: граф на матрице от обратного**  
    Как экономить обход, стартуя от границ.
32. **31. Coin Change: минимум монет через DP**  
    Задача на правильную инициализацию невозможных состояний.
33. **32. Combination Sum: backtracking с отсечениями**  
    Учимся контролировать дерево перебора.
34. **33. Word Break: DP на строке с словарём**  
    Частый паттерн для валидации текстовых потоков.
35. **34. Longest Increasing Subsequence: O(n²) и O(n log n)**  
    Отличный сюжет для разговора про эволюцию решения.
36. **35. House Robber: DP с выбором брать/пропускать**  
    Базовый шаблон локального конфликта решений.
37. **36. Decode Ways: DP на строковом декодировании**  
    Проверка внимательности к нулям и двузначным случаям.
38. **37. Unique Paths: комбинаторика и DP**  
    Две модели решения одной задачи.
39. **38. Jump Game: жадность и достижимость**  
    Маленькая задача с сильным собеседовательным сигналом.
40. **39. Gas Station: круговой маршрут и баланс**  
    Хороший пример доказуемой жадной стратегии.
41. **40. Maximum Product Subarray: максимум и минимум одновременно**  
    Наглядный кейс на инварианты при отрицательных числах.
42. **41. Find Minimum in Rotated Sorted Array: ещё один поворот бинарного поиска**  
    Тренируем мышление по монотонности.
43. **42. Rotting Oranges: BFS по слоям времени**  
    Модель «распространения сигнала» в сетях и очередях.
44. **43. K Closest Points to Origin: quickselect против heap**  
    Как выбирать алгоритм под размер данных.
45. **44. Serialize and Deserialize Binary Tree: контракт формата данных**  
    Это уже про инженерный дизайн, а не только алгоритмы.
46. **45. LRU Cache: hash map + двусвязный список**  
    Самая знаменитая системная мини-задача на интервью.
47. **46. Median of Two Sorted Arrays: сложность как цель**  
    Плотная задача на бинарный поиск по разбиению.
48. **47. Regular Expression Matching: тяжёлый DP-кейс**  
    Тренировка устойчивости и точности формализации.
49. **48. Word Ladder: кратчайший путь в неявном графе**  
    BFS и генерация соседей для строковых состояний.
50. **49. Alien Dictionary: топологическая сортировка «чужого» алфавита**  
    Финал с полноценной графовой моделью порядка.

## Источник задач

- [LeetCode Top Interview Questions](https://leetcode.com/problem-list/top-interview-questions/)
