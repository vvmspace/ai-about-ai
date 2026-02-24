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
    Вход в dynamic programming (динамическое программирование) через простую рекуррентную модель.
13. **[12. Reverse Linked List: разворот структуры под контролем инварианта](./12_reverse_linked_list_invariant_control_ru.md)**  
    Проверка аккуратности мутаций структуры.
14. **[13. Top K Frequent Elements: куча против bucket-подхода](./13_top_k_frequent_elements_heap_bucket_ru.md)**  
    Trade-off между асимптотикой и константами.
15. **[14. Number of Islands: поиск в глубину и поиск в ширину на сетке без хаоса](./14_number_of_islands_dfs_bfs_grid_ru.md)**  
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
27. **[26. Insert Interval: аккуратная вставка без повторного хаоса](./26_insert_interval_merge_window_ru.md)**  
    Линейное слияние с чётким разделением на префикс, окно и хвост.
28. **[27. Non-overlapping Intervals: жадность, которая действительно доказуема](./27_non_overlapping_intervals_greedy_min_removals_ru.md)**  
    Выбор по раннему окончанию как прямой путь к минимуму удалений.
29. **[28. Meeting Rooms II: минимальное число комнат как контроль пиков](./28_meeting_rooms_ii_min_heap_timeline_ru.md)**  
    Min-heap показывает пиковую параллельность без лишних конструкций.
30. **[29. Course Schedule: цикл зависимостей и границы выполнимости](./29_course_schedule_cycle_detection_graph_ru.md)**  
    Графовая проверка того, выполним ли план вообще.
31. **[30. Pacific Atlantic Water Flow: думать от границ, а не от каждой клетки](./30_pacific_atlantic_reverse_flow_ru.md)**  
    Два обхода от океанов дают ответ без повторного перебора всех стартов.
32. **[31. Coin Change: минимум монет через динамическое программирование без самообмана](./31_coin_change_dp_min_coins_ru.md)**  
    Системный переход по состояниям вместо ненадёжной жадности.
33. **[32. Combination Sum: backtracking, который не уходит в хаос](./32_combination_sum_backtracking_cuts_ru.md)**  
    Дерево решений с дисциплиной отсечений и контролем пути.
34. **[33. Word Break: границы строки и проверка выполнимости через динамическое программирование](./33_word_break_dp_dictionary_boundary_ru.md)**  
    Проверка достижимости конца строки через валидные точки разреза.
35. **[34. Longest Increasing Subsequence: от квадратичного решения к логарифмическому ускорению](./34_longest_increasing_subsequence_quadratic_and_binary_search_ru.md)**  
    Показываем эволюцию от базовой модели к ускорению через бинарный поиск.
36. **[35. House Robber: выбор с конфликтом соседей через динамическое программирование](./35_house_robber_dynamic_programming_choices_ru.md)**  
    Классический переход «взять или пропустить» без потери оптимальности.
37. **[36. Decode Ways: декодирование строки как проверка аккуратности переходов](./36_decode_ways_dynamic_programming_string_ru.md)**  
    Строгая работа с одиночными и парными переходами по символам.
38. **[37. Unique Paths: одна сетка, две строгие модели решения](./37_unique_paths_combinatorics_and_dynamic_programming_ru.md)**  
    Сравнение комбинаторики и динамического программирования на одном примере.
39. **[38. Jump Game: жадность и достижимость](./38_jump_game_greedy_reachability_ru.md)**  
    Маленькая задача с сильным собеседовательным сигналом.
40. **[39. Gas Station: круговой маршрут и баланс](./39_gas_station_circular_balance_ru.md)**  
    Хороший пример доказуемой жадной стратегии.
41. **[40. Maximum Product Subarray: максимум и минимум одновременно](./40_maximum_product_subarray_max_min_tracking_ru.md)**  
    Наглядный кейс на инварианты при отрицательных числах.
42. **[41. Find Minimum in Rotated Sorted Array: ещё один поворот бинарного поиска](./41_find_minimum_in_rotated_sorted_array_binary_pivot_ru.md)**  
    Тренируем мышление по монотонности.
43. **[42. Rotting Oranges: поиск в ширину по слоям времени](./42_rotting_oranges_bfs_time_layers_ru.md)**  
    Модель «распространения сигнала» в сетях и очередях.
44. **[43. K Closest Points to Origin: quickselect против heap](./43_k_closest_points_heap_vs_quickselect_ru.md)**  
    Как выбирать алгоритм под размер данных.
45. **[44. Serialize and Deserialize Binary Tree: контракт формата данных](./44_serialize_deserialize_binary_tree_format_contract_ru.md)**  
    Это уже про инженерный дизайн, а не только алгоритмы.
46. **[45. Least Recently Used Cache: hash map + двусвязный список](./45_lru_cache_hashmap_doubly_linked_list_ru.md)**  
    Самая знаменитая системная мини-задача на интервью.
47. **46. Median of Two Sorted Arrays: сложность как цель**  
    Плотная задача на бинарный поиск по разбиению.
48. **47. Regular Expression Matching: тяжёлый кейс динамического программирования**  
    Тренировка устойчивости и точности формализации.
49. **48. Word Ladder: кратчайший путь в неявном графе**  
    Поиск в ширину и генерация соседей для строковых состояний.
50. **49. Alien Dictionary: топологическая сортировка «чужого» алфавита**  
    Финал с полноценной графовой моделью порядка.

## Источник задач

- [LeetCode Top Interview Questions](https://leetcode.com/problem-list/top-interview-questions/)
