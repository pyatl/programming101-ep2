# I want to have a program that will allow me to enter 
# information about my day and save them to file.
# This would be my digital diary.
# I dont need a fancy user interface. I will do it through the
# command line.

# - A way to feed python information or get input
# - A way to save the information into files
# - A way to save the information into separate files 
# - with clear names.

from datetime import datetime

def get_daily_diary_input():
    daily_diary = input('Write your daily diary:\n')
    return daily_diary


def write_daily_diary(diary):
    filename = f'{datetime.now().strftime("%c")}.diary'
    with open(filename, 'w') as f:
        f.write(diary)


def main():
    diary = get_daily_diary_input()
    write_daily_diary(diary)
    print('Diary saved!')


if __name__ == "__main__":
    main()






