import os
from datetime import datetime, timedelta


def make_commits(start_date: str, num_days: int):
    """Создаёт коммиты в Git за несколько дней с указанной даты."""
    start = datetime.strptime(start_date, "%d.%m.%Y")

    for day in range(num_days):
        current_date = start + timedelta(days=day)
        git_date = current_date.strftime("%Y-%m-%d")
        readable_date = current_date.strftime("%d.%m.%Y г.")

        with open("data.txt", "a", encoding="utf-8") as file:
            file.write(f"{readable_date} ← это коммит за день!\n")

        os.system("git add data.txt")
        os.system(
            f'git commit --date="{git_date}" '
            f'-m "Коммит за {readable_date}"'
        )

    os.system("git push -u origin main")


def main():
    """Запускает процесс создания коммитов."""
    make_commits("00.00.0000", 0)


if __name__ == "__main__":
    main()
