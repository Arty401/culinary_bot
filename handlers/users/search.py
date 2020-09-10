from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import cancel, menu
from loader import dp, db
from states import SearchByTitle, SearchByIngredients


@dp.message_handler(text='Все рецепты')
async def show_all_recipes(message: types.Message):
    query = [f"""\n<b>Название:</b>\n\n {item[1]}\n
<b>Рецепт</b>:\n
{item[2]}\n
{'-' * 30}""" for item in db.select_all_recipes()]

    if not query:
        await message.answer("На данный момент наша база данных пуста.\nИзвините за неудобства.\n"
                             "Вы можете обратиться к администратору @Arty401 за помощью")
        return

    await message.answer('\n'.join(query), parse_mode=types.ParseMode.HTML)


@dp.message_handler(text='Поиск по ингридиентам')
async def search_by_ingredients_start(message: types.Message):
    await message.answer('Введите ингридиеты вот так:\n--> картошка, капуста, лавровый лист', reply_markup=cancel)
    await SearchByIngredients.ingredients.set()


@dp.message_handler(state=SearchByIngredients.ingredients)
async def search_by_ingredients_end(message: types.Message, state: FSMContext):
    if message.text == "❌Отмена❌":
        await state.reset_state(with_data=True)
        await message.answer("Возвращаюсь...", reply_markup=menu)
        return

    ingredients = message.text

    await state.finish()
    query = db.select_recipes_by_ingredients(ingredients)

    if not query:
        await message.answer("Рецептов с такими ингредиентами не найдено :(", reply_markup=menu)
        return

    answer = '\n'.join(
        [f'<b>{title}</b>\n\n<b>Ингридиеты</b>:\n{ing}\n\n{recipe}' for title, recipe, ing in query])

    await message.answer(answer, parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Поиск по названию")
async def search_step1(message: types.Message):
    await message.answer("Введите название:", reply_markup=cancel)
    await SearchByTitle.Title.set()


@dp.message_handler(state=SearchByTitle.Title)
async def search_step2(message: types.Message, state: FSMContext):
    if message.text == "❌Отмена❌":
        await state.reset_state(with_data=True)
        await message.answer("Возвращаюсь...", reply_markup=menu)
        return

    answer = message.text

    async with state.proxy() as data:
        data["answer"] = answer
        query = db.select_recipe_by_title(data["answer"])

    await message.answer(f"Вы ввели: {answer}.\nВыполняю поиск...")

    await state.finish()

    if not query:
        await message.answer("Рецепта с таким названием в нашей базе нет :(", reply_markup=menu)
        return

    query_answer = [
        f"\n<b>Название:</b>\n\n{item[0]}\n\n" +
        f"<b>Ингридиенты</b>:\n\n{item[2]}\n\n" +
        f"<b>Рецепт</b>:\n\n{item[1]}\n\n{'-' * 30}"
        for item in db.select_recipe_by_title(answer)]
    await message.answer('\n'.join(query_answer), reply_markup=menu, parse_mode=types.ParseMode.HTML)
