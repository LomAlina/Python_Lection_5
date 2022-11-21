# from isOdd import isOdd

# print(isOdd(0)) 
# print(isOdd(4))





# from progress.bar import Bar
# import time 

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()




# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))




# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use('_mpl-gallery')

# # make data
# np.random.seed(1)
# x = 4 + np.random.normal(0, 1.5, 200)

# # plot:
# fig, ax = plt.subplots()

# ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 56), yticks=np.linspace(0, 56, 9))

# plt.show()






# import matplotlib.pyplot as plt
# import numpy as np
# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()





# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from bot_commands import *


# def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     update.message.reply_text(f'Hi {update.effective_user.first_name}!')


# app = ApplicationBuilder().token('5563396070:AAG27HtXinDeQhM2jypfUOrWx92NuDNREHE').build()

# app.add_handler(CommandHandler("hi", hi_command))
# app.add_handler(CommandHandler("time", time_command))
# app.add_handler(CommandHandler("help", help_command))
# app.add_handler(CommandHandler("sum", sum_command))

# print('server start')

# app.run_polling()






from telegram import Update 
from telegram.ext import Updater, CommandHandler, CallbackContext 
from bot_commands import * 
updater = Updater('5563396070:AAG27HtXinDeQhM2jypfUOrWx92NuDNREHE') 
updater.dispatcher.add_handler(CommandHandler('hi', hi_command)) 
updater.dispatcher.add_handler(CommandHandler('time', time_command)) 
updater.dispatcher.add_handler(CommandHandler('help', help_command)) 
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
print('server start') 
updater.start_polling() 
updater.idle()