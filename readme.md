### Результати

- **DFS (пошук в глибину)**:
  - Шлях від "Akademmistechko" до "Teremky": `['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut', 'Vokzalna', 'Universytet', 'Teatralna', 'Zoloti Vorota', 'Palats Sportu', 'Klovska', 'Pecherska', 'Druzhby Narodiv', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky', 'Kharkivska', 'Vyrlytsia', 'Boryspilska', 'Chervony Khutir']`
- **BFS (пошук в ширину)**:
  - Шлях від "Akademmistechko" до "Teremky: `['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut', 'Vokzalna', 'Universytet', 'Teatralna', 'Zoloti Vorota', 'Palats Sportu', 'Klovska', 'Pecherska', 'Druzhby Narodiv', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky', 'Kharkivska', 'Vyrlytsia', 'Boryspilska', 'Chervony Khutir', 'Boryspilska', 'Kharkivska', 'Pozniaky', 'Osokorky', 'Slavutych', 'Vydubychi', 'Druzhby Narodiv', 'Pecherska', 'Klovska', 'Palats Sportu', 'Zoloti Vorota', 'Teatralna', 'Universytet', 'Vokzalna', 'Politekhnichnyi Instytut', 'Shuliavska', 'Beresteiska', 'Nyvky', 'Sviatoshyn', 'Zhytomyrska', 'Akademmistechko']`

### Порівняння результатів

- **DFS (пошук в глибину)**:
  - Алгоритм DFS знаходить шлях, йдучи в глибину по кожному маршруту до кінцевої станції. Він обирає перший знайдений шлях, який може бути довшим за кількістю кроків.
  - **Результат**: `['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut', 'Vokzalna', 'Universytet', 'Teatralna', 'Zoloti Vorota', 'Palats Sportu', 'Klovska', 'Pecherska', 'Druzhby Narodiv', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky', 'Kharkivska', 'Vyrlytsia', 'Boryspilska', 'Chervony Khutir']`
- **BFS (пошук в ширину)**:
  - Алгоритм BFS знаходить шлях, проходячи всі сусідні вершини на поточному рівні перед переходом на наступний рівень. Він забезпечує найкоротший шлях за кількістю кроків.
  - **Результат**: `['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut', 'Vokzalna', 'Universytet', 'Teatralna', 'Zoloti Vorota', 'Palats Sportu', 'Klovska', 'Pecherska', 'Druzhby Narodiv', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky', 'Kharkivska', 'Vyrlytsia', 'Boryspilska', 'Chervony Khutir']`

### Висновки

- **DFS**:

  - Може знайти більш глибокий шлях, оскільки алгоритм йде в глибину по першому знайденому маршруту. Це може призвести до довших шляхів, особливо якщо граф має багато гілок.
  - У нашому випадку DFS знайшов шлях, який включає більше вершин, ніж BFS.

- **BFS**:
  - Завжди знаходить найкоротший шлях у сенсі кількості ребер, оскільки перевіряє всі сусідні вузли перед переходом на наступний рівень.
  - У нашому випадку BFS знайшов найкоротший шлях за кількістю кроків, який є більш оптимальним у порівнянні з результатом DFS.

Обидва алгоритми мають свої переваги та недоліки, і вибір алгоритму залежить від конкретного застосування та вимог до пошуку шляхів у графі.
