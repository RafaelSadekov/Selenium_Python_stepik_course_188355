# Selenium на Python - Задания курса

Добро пожаловать в мой репозиторий с выполненными заданиями курса [**Selenium на Python**](https://stepik.org/course/188355/info) от Алексея Коледачкина на платформе Stepik.

## Цель курса

Создать прочнейший фундамент из практических навыков для успешного старта в карьере QA Automation инженера.

## Для выполненныя задания

### 1.1 Создание виртуального окружения


Виртуальное окружение нужно для изоляции проекта, чтобы все устанавливаемые библиотеки использовались только в рамках текущего проекта и не было конфликтов с другими зависимостями.

**Шаги:**

1. **Создание виртуального окружения:**

    ```bash
    python3 -m venv venv
    ```

    В результате в директории проекта появится папка `venv`.

2. **Активация окружения:**

    - **Mac OS / Linux:**

        ```bash
        source venv/bin/activate
        ```

    - **Windows PowerShell:**

        ```powershell
        venv/Scripts/activate.ps1
        ```

    В результате в терминале вы увидите префикс с названием окружения.

**Важно:** Окружение работает в рамках текущей сессии окна терминала. Если вы закроете терминал, необходимо будет активировать окружение снова. Для удаления окружения деактивируйте его командой:

```bash
deactivate
```

### Установка Selenium и зависимостей

После создания и активации виртуального окружения необходимо установить все зависимости (библиотеки) для начала работы.

1. **Установка Selenium:**

    ```bash
    pip3 install selenium
    ```

2. **Дополнительная установка библиотеки `packaging` (при необходимости):**

    ```bash
    pip3 install packaging
    ```

3. **Установка `webdriver-manager`:**

    ```bash
    pip3 install webdriver-manager
    ```

## Технологии и Инструменты

- **Python** — язык программирования для автоматизации.
- **Selenium WebDriver** — инструмент для автоматизации веб-браузеров.
- **Virtualenv** — для управления виртуальными окружениями.
- **Git & GitHub** — системы контроля версий и хостинг для проектов.

## Контакты

- 📧 Email: [rafaelsadekov@gmail.com](mailto:rafaelsadekov@gmail.com)
- [![Stepik](https://img.shields.io/badge/Stepik-434AEB?style=for-the-badge&logo=stepik&logoColor=white)](https://stepik.org/users/433225242/profile)
- [![Hexlet](https://img.shields.io/badge/Hexlet-2D3748?style=for-the-badge&logo=hexlet&logoColor=white)](https://ru.hexlet.io/u/rafaelsadekov)
