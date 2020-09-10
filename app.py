from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    from utils.notify_admins import notify_admins_on_startup

    await notify_admins_on_startup(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
