# UV — Швейцарский Нож Python-разработчика

UV — современный универсальный инструмент для Python-разработки, который объединяет в себе функциональность множества классических утилит и решает большинство проблем управления зависимостями и средой разработки. Созданный на Rust и разработанный командой Astral (авторами Ruff), UV обеспечивает высокую производительность и универсальность.

## Что такое UV и почему его стоит использовать

UV (Universal Virtualenv) — это высокопроизводительный инструмент для Python-разработчиков, объединяющий функциональность нескольких других инструментов:

* Управление пакетами (`pip`, `pip-tools`)
* Управление виртуальными окружениями (`venv`, `virtualenv`)
* Управление версиями Python (`pyenv`)
* Запуск скриптов в изолированной среде (`pipx`)
* Работа с зависимостями проекта (`poetry`, `pdm`)

Основные преимущества UV:

* Скорость работы — в 15-20 раз быстрее стандартных инструментов Python[^16]
* Кросс-платформенность — одинаково хорошо работает на Linux, macOS и Windows
* Единый инструмент для всего жизненного цикла разработки
* Отличное управление зависимостями через lock-файлы


## Установка UV

### На Linux и macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Или через Homebrew:

```bash
brew install uv
```


### На Windows

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Альтернативно через Winget:

```
winget install --id=astral-sh.uv -e
```

Или Scoop:

```
scoop install main/uv
```


### Через pip или pipx

```bash
pip install uv
# или
pipx install uv
```


### Проверка установленной версии

```bash
uv --version
```


### Обновление UV

Если UV был установлен через автоматический установщик:

```bash
uv self update
```

Если через pip:

```bash
pip install --upgrade uv
```


## Управление версиями Python

UV обладает уникальной возможностью автоматически скачивать и использовать нужные версии Python, что делает его отличной заменой pyenv[^11][^4].

### Просмотр доступных версий

```bash
uv python list
```


### Установка определенной версии Python

```bash
uv python install 3.11
```


### Использование определенной версии Python в проекте

```bash
uv python use 3.11
```

Эта команда создаст файл `.python-version` в текущей директории, указывающий на нужную версию Python.

## Создание и управление проектами

### Инициализация нового проекта

```bash
mkdir my-project
cd my-project
uv init
```

UV создаст базовую структуру проекта с `pyproject.toml` и другими необходимыми файлами[^17].

### Создание виртуального окружения

```bash
uv venv
```

Или с указанием версии Python:

```bash
uv venv --python=3.11
```


### Активация виртуального окружения

На Linux/macOS:

```bash
source .venv/bin/activate
```

На Windows:

```bash
.venv\Scripts\activate
```


### Где хранится виртуальное окружение

По умолчанию UV создаёт виртуальное окружение в директории `.venv` вашего проекта[^18].

## Работа с пакетами

### Установка пакетов

```bash
uv pip install flask
```

Или установка из файла requirements.txt:

```bash
uv pip install -r requirements.txt
```


### Просмотр дерева зависимостей

```bash
uv pip list --tree
```

Эта команда покажет не только установленные пакеты, но и все их зависимости в древовидной структуре[^18].

### Фиксация зависимостей (lock-файл)

```bash
uv pip freeze > requirements.txt
```

Или использование встроенного lock-механизма:

```bash
uv lock
```


### Установка dev-зависимостей

Для разделения основных и разработческих зависимостей:

```bash
uv pip install --dev pytest
```


## Запуск Python-кода

### Запуск скрипта в проекте

```bash
uv run script.py
```

UV автоматически обнаружит виртуальное окружение и запустит скрипт с использованием правильной версии Python и установленных в проекте пакетов[^14].

### Запуск скрипта без проекта

```bash
uv run /path/to/script.py
```

UV создаст временное окружение для запуска скрипта.

### Запуск с аргументами

```bash
uv run script.py arg1 arg2
```


### Встраивание зависимостей в скрипт

Одна из самых мощных возможностей UV — запуск скрипта с указанием зависимостей в самом коде:

```python
#!/usr/bin/env python3
# uv-x: flask==2.0.1
# uv-x: requests>=2.26.0

import flask
import requests

# Ваш код...
```

Затем запустите:

```bash
uv run script.py
```

UV автоматически установит указанные зависимости во временное окружение и запустит скрипт[^18].

## Продвинутые возможности

### Использование инструментов форматирования и анализа кода

```bash
uv tool run ruff check .
uv tool run black .
```


### Установка глобальных инструментов

```bash
uv tool install ruff
```

Установленные инструменты доступны через команду `uvx`:

```bash
uvx ruff check .
```


### Настройка Pyright LSP для работы с UV

Для интеграции с языковыми серверами (например, для VS Code):

В `settings.json` VS Code:

```json
{
    "python.linting.enabled": true,
    "python.linting.pyrightEnabled": true,
    "python.analysis.extraPaths": [".venv/lib/python3.11/site-packages"]
}
```

Это позволит LSP находить пакеты, установленные через UV[^18].

### Использование в Docker

UV отлично работает в контейнерах, позволяя создавать более эффективные Docker образы:

```dockerfile
FROM python:3.11-slim

# Установка UV
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app
COPY requirements.txt .
COPY pyproject.toml .

# Установка зависимостей (быстрее, чем pip)
RUN uv pip install -r requirements.txt

COPY . .

CMD ["uv", "run", "app.py"]
```


## Сравнение с другими инструментами

| Особенность | UV | pip | Poetry | pipenv |
| :-- | :-- | :-- | :-- | :-- |
| Скорость | Очень высокая | Низкая | Средняя | Низкая |
| Управление виртуальными окружениями | ✅ | ❌ | ✅ | ✅ |
| Управление версиями Python | ✅ | ❌ | ❌ | ❌ |
| Lock-файлы | ✅ | ❌ | ✅ | ✅ |
| Разделение dev-зависимостей | ✅ | ❌ | ✅ | ✅ |
| Запуск скриптов | ✅ | ❌ | ✅ | ✅ |
| Встраивание зависимостей в скрипты | ✅ | ❌ | ❌ | ❌ |

## Заключение

UV представляет собой революционный инструмент для Python-разработчиков, объединяющий функциональность нескольких отдельных инструментов в единое, быстрое и удобное решение. Основные преимущества:

1. Значительно ускоряет работу с зависимостями и виртуальными окружениями
2. Упрощает управление проектами благодаря единому интерфейсу
3. Обеспечивает предсказуемость сборок через lock-файлы
4. Предлагает уникальные возможности, такие как встраивание зависимостей в скрипты
5. Поддерживает все основные платформы и сценарии использования

UV — это инструмент, который меняет представление о том, как должна выглядеть экосистема инструментов для Python-разработки. Его стоит взять на вооружение каждому Python-разработчику для упрощения и ускорения рабочего процесса[^1][^11][^16].

К просмотру обязательно!!! https://youtu.be/0Osso8mLL-A?si=T4pNll_e7vPFm23L
[^1]: https://www.youtube.com/watch?v=0Osso8mLL-A

[^2]: https://www.semanticscholar.org/paper/6715755c2b0792b74cd7ae03fa6b7bebccd5b1ec

[^3]: https://www.semanticscholar.org/paper/d84636ff0bba80ae27cd820aab34b1f3d88e8367

[^4]: https://www.semanticscholar.org/paper/376531a8bc33f029c04af55d410f0052dfa114c8

[^5]: https://arxiv.org/abs/2402.08137

[^6]: https://arxiv.org/abs/2402.17163

[^7]: https://www.semanticscholar.org/paper/f9248efad6e3847f0eba36c841cdf74cf9be98e6

[^8]: https://www.reddit.com/r/neovim/comments/1gjq952/best_way_to_execute_python_code/

[^9]: https://www.reddit.com/r/NixOS/comments/1h8y6vl/how_to_install_python_packages_globally_on_nixos/

[^10]: https://www.reddit.com/r/ProgrammerHumor/comments/1iefjqu/learnpythonitwillbefun/

[^11]: https://www.reddit.com/r/Python/comments/1ex6n9k/uv_unified_python_packaging/

[^12]: https://www.reddit.com/r/OpenWebUI/comments/1izq7l1/mac_1531_manual_install_using_uv_where_are_my/

[^13]: https://www.reddit.com/r/Python/comments/1gaz3tm/hatch_or_uv_for_a_new_project/

[^14]: https://habr.com/ru/articles/875840/

[^15]: https://devopsgu.ru/devops/languages-programming/python/uv/

[^16]: https://www.youtube.com/watch?v=l04of2hEb8c

[^17]: https://github.com/Hexlet/ru-instructions/blob/main/uv.md

[^18]: https://www.youtube.com/watch?v=0Osso8mLL-A

[^19]: https://ru.hexlet.io/courses/python-setup-environment/lessons/init-project/theory_unit

[^20]: https://www.semanticscholar.org/paper/d2558ad3b8a32b67bbf61cfeba94aaf3c9556814

[^21]: https://arxiv.org/abs/2305.03533

[^22]: https://arxiv.org/abs/2309.02167

[^23]: https://www.semanticscholar.org/paper/e44157d42d8f29eab3baba8d607d30089e45edff

[^24]: https://www.reddit.com/r/Python/comments/1ixryec/anyone_used_uv_package_manager_in_production/

[^25]: https://www.reddit.com/r/programming/comments/1dpr61b/never_thought_id_be_saying_this_but_switching/

[^26]: https://www.reddit.com/r/Python/comments/1ex6n9k/uv_unified_python_packaging/?tl=es-es

[^27]: https://www.reddit.com/r/Python/comments/1ex6n9k/uv_unified_python_packaging/?tl=pt-br

[^28]: https://habr.com/ru/articles/828016/

[^29]: https://docs.astral.sh/uv/guides/install-python/

[^30]: https://kryptonite.ru/articles/building-a-python-project-with-uv-and-docker/

[^31]: https://docs.astral.sh/uv/

