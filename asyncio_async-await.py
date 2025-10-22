# план 
# 1. asyncio фреймворк для создания событийных циклов
# 2. пример простой асинхронной программы времен python 3.4
# 3. синтаксис async/await на замену @asyncio.coroutine и yield from
# 4. пример асинхронного скачивания файлов

import asyncio

async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)

async def print_time():
    count = 0 
    while True:
        if count % 3 == 0:
            print(f"{count} seconds passed")
        count += 1
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    asyncio.run(main())