# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "typing",
#   "tqdm"
# ]
# ///

import re
import sys
import logging
from pathlib import Path
from typing import List, Dict, Union
from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

MAX_HEADER_LEVEL = 3
SUPPORTED_ENCODINGS = ['utf-8', 'windows-1251']

class MarkdownMerger:
    def __init__(self):
        self.headers: List[Dict[str, Union[int, str]]] = []
        self.full_content: List[str] = []

    def process_files(self, folder_path: str) -> None:
        """Обработка всех файлов в указанной папке"""
        folder = Path(folder_path)
        if not folder.is_dir():
            raise ValueError(f"Указанный путь {folder_path} не является директорией")

        try:
            md_files = sorted(folder.glob('*.md'))
            if not md_files:
                logger.error(f"Ошибка: В папке {folder_path} нет .md файлов!")
                sys.exit(1)

            logger.info(f"Найдено файлов: {len(md_files)}")
            
            for md_file in tqdm(md_files, desc="Обработка файлов"):
                logger.info(f"Обработка файла: {md_file.name}")
                
                # Добавляем название файла как заголовок 1-го уровня
                file_title = self._format_filename(md_file.stem)
                self._add_header(file_title, 1)
                self.full_content.append(f"# {file_title}\n\n")
                
                # Обрабатываем содержимое файла
                self._process_file_content(md_file)

        except Exception as e:
            logger.error(f"Ошибка при обработке файлов: {str(e)}")
            sys.exit(1)

    def _format_filename(self, filename: str) -> str:
        """Форматирование имени файла для заголовка"""
        return filename.replace('_', ' ').title()

    def _add_header(self, title: str, level: int) -> None:
        """Добавление заголовка в структуру"""
        anchor = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
        self.headers.append({
            'level': level,
            'title': title,
            'anchor': anchor
        })

    def _process_file_content(self, file_path: Path) -> None:
        """Обработка содержимого файла с изменением уровней заголовков"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('#'):
                        match = re.match(r'^(#+)\s+(.+)$', line)
                        if match:
                            original_level = len(match.group(1))
                            new_level = min(original_level + 1, MAX_HEADER_LEVEL)
                            title = match.group(2).strip()
                            self._add_header(title, new_level)
                            line = f"{'#' * new_level} {title}\n"
                    self.full_content.append(line)
            self.full_content.append("\n")
        except UnicodeDecodeError:
            logger.warning(f"Проблема с кодировкой UTF-8 в файле {file_path.name}, пробуем windows-1251")
            try:
                with open(file_path, 'r', encoding='windows-1251') as f:
                    content = f.read()
                self.full_content.append(content + "\n\n")
            except UnicodeDecodeError:
                logger.error(f"Не удалось прочитать файл {file_path.name} с поддерживаемыми кодировками")

    def generate_toc(self) -> str:
        """Генерация многоуровневого оглавления"""
        if not self.headers:
            return "# Оглавление\n\nНет заголовков"
            
        toc = ["# Оглавление\n"]
        for header in self.headers:
            indent = '  ' * (header['level'] - 1)
            toc.append(f"{indent}- [{header['title']}](#{header['anchor']})")
        return '\n'.join(toc)

    def save_combined(self, output_file: str) -> None:
        """Сохранение объединенного файла"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(self.generate_toc())
                f.write('\n\n---\n\n')
                f.write(''.join(self.full_content))
            logger.info(f"Файл успешно сохранен: {output_file}")
        except Exception as e:
            logger.error(f"Ошибка при сохранении файла: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    merger = MarkdownMerger()
    
    input_folder = input("Введите путь к папке с .md файлами: ")
    
    # Проверка существования папки
    if not Path(input_folder).exists():
        logger.error(f"Ошибка: Папка {input_folder} не существует!")
        sys.exit(1)
    
    output_file = "combined_document.md"
    
    merger.process_files(input_folder)
    merger.save_combined(output_file)