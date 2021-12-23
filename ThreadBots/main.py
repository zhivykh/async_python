import sys
from cutlery import kitchen
from bot import ThreadBot, BotTasks


bots = [ThreadBot() for i in range(10)]

for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put(BotTasks.PREPARE)
        bot.tasks.put(BotTasks.CLEAR)
    bot.tasks.put(BotTasks.SHUTDOWN)

print("Kitchen inventory before service:", kitchen)
for bot in bots:
    bot.start()

for bot in bots:
    bot.join()

print("Kitchen inventory after service:", kitchen)