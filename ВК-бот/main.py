from bot import bot
from handlers import main
import datetime

if __name__ == "__main__":
    main()
    print(f'start at {datetime.datetime.now()}')
    bot.run_forever()
