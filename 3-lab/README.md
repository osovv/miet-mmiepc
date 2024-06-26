### Контрольные вопросы

1. **Протокол HTTPS. Применение.**

   - HTTPS (HyperText Transfer Protocol Secure) — это расширение HTTP, использующее шифрование для повышения безопасности передачи данных между клиентом и сервером. Применяется для защиты данных в веб-сайтах, особенно в тех, которые обрабатывают чувствительную информацию, такую как личные данные, финансовые транзакции и логины. Используется на многих популярных платформах, таких как электронные платежные системы, социальные сети и почтовые сервисы.

2. **Протокол HTTPS. Безопасность.**

   - Безопасность HTTPS обеспечивается с помощью криптографического протокола SSL/TLS, который шифрует данные, передаваемые между клиентом и сервером. Это делает данные недоступными для перехвата и расшифровки посторонними лицами. Протокол использует асимметричное шифрование для обмена ключами и симметричное шифрование для защиты данных. TLS также обеспечивает аутентификацию сервера с помощью цифровых сертификатов, гарантируя, что клиент соединяется с доверенным сервером.

3. **Протокол HTTPS. Сертификаты и их виды.**

   - Цифровой сертификат — это электронный документ, подтверждающий подлинность сервера и его право использовать определенное доменное имя. Виды сертификатов:
     - **Domain Validation (DV)**: Проверка домена, подтверждает только владение доменом.
     - **Organization Validation (OV)**: Проверка организации, содержит информацию о юридическом лице.
     - **Extended Validation (EV)**: Расширенная проверка, включает детальную информацию о компании, наиболее надежный тип.
     - **Single Certificate**: Сертификат для одного домена.
     - **Multi-Domain Certificate**: Сертификат для нескольких доменов.
     - **Wildcard Certificate**: Сертификат для домена и всех его поддоменов.

4. **Протокол TLS. Используемые алгоритмы.**

   - TLS (Transport Layer Security) использует следующие алгоритмы:
     - **Асимметричное шифрование**: RSA, Diffie-Hellman, DSA, ECDSA для обмена ключами и аутентификации.
     - **Симметричное шифрование**: RC4, IDEA, Triple DES, SEED, Camellia, AES для защиты данных.
     - **Хэш-функции**: MD5, SHA-1, SHA-256, SHA-384 для проверки целостности данных и создания аутентификационных кодов сообщений.

5. **Что такое хэш-функция? Когда она является криптографически стойкой?**

   - Хэш-функция — это функция, которая преобразует входные данные произвольной длины в выходную строку фиксированной длины (хэш). Криптографически стойкая хэш-функция должна удовлетворять следующим требованиям:
     - **Необратимость**: Невозможно восстановить исходные данные по хэшу.
     - **Устойчивость к коллизиям**: Невозможно найти два разных входных значения, которые дают одинаковый хэш.
     - **Свойство лавинного эффекта**: Малое изменение во входных данных должно значительно изменять хэш.

6. **Что такое лавинный эффект?**

   - Лавинный эффект — это свойство криптографических алгоритмов, при котором малое изменение входных данных (например, изменение одного бита) приводит к значительному изменению выходных данных (хэша). Это свойство важно для обеспечения безопасности, так как затрудняет предсказание изменений в хэше на основе изменений в исходных данных.

7. **Алгоритм MD5.**

   - MD5 (Message Digest Algorithm 5) — криптографическая хэш-функция, разработанная Рональдом Ривестом в 1991 году, генерирующая 128-битный хэш. Используется для проверки целостности данных и создания цифровых подписей. В настоящее время считается устаревшим и небезопасным из-за возможности нахождения коллизий (двух различных входов с одинаковым хэшем).

8. **Семейство алгоритмов SHA.**
   - Семейство алгоритмов SHA (Secure Hash Algorithms) включает несколько версий, разработанных Агентством национальной безопасности США (NSA):
     - **SHA-1**: Генерирует 160-битный хэш, используется в SSL/TLS, но уже считается небезопасным.
     - **SHA-2**: Включает алгоритмы SHA-224, SHA-256, SHA-384 и SHA-512, обеспечивающие более высокую криптографическую стойкость по сравнению с SHA-1. Используются в современных системах для цифровых подписей, сертификатов и аутентификации данных.

Ответы на эти вопросы должны дать вам хорошее понимание основ защиты информации в интернете, роли и важности протоколов HTTPS и TLS, а также понимание криптографических хэш-функций и их свойств.
