import os
import shutil

def sort_files_by_type(source_dir):
    if not os.path.exists(source_dir):
        print(f"Ошибка: Исходная директория \'{source_dir}\' не существует.")
        return

    print(f"Начинаю сортировку файлов в директории: {source_dir}")

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            if not file_extension: # Для файлов без расширения
                destination_folder = os.path.join(source_dir, "Без_расширения")
            else:
                # Удаляем точку из расширения для имени папки
                folder_name = file_extension[1:]
                destination_folder = os.path.join(source_dir, folder_name)

            # Создаем папку, если ее нет
            os.makedirs(destination_folder, exist_ok=True)

            # Перемещаем файл
            try:
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Перемещен: {filename} -> {folder_name}/")
            except shutil.Error as e:
                print(f"Ошибка при перемещении {filename}: {e}")
            except Exception as e:
                print(f"Неизвестная ошибка при перемещении {filename}: {e}")

    print("Сортировка завершена.")

if __name__ == "__main__":
    
    directory_to_sort = input("Введите путь к директории для сортировки (например, . для текущей): ")
    sort_files_by_type(directory_to_sort)


