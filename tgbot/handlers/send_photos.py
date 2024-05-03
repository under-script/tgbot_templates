from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

media_router = Router()


@media_router.message(F.PHOTO)
async def get_file_id_p(message: Message):
    await message.reply(message.photo[-1].file_id)


@media_router.message(F.VIDEO)
async def get_file_id_v(message: Message):
    await message.reply(message.video.file_id)


@media_router.message(Command("kitob"))
async def send_book(message: Message):
    photo_url = "https://telegra.ph/file/fd053ddb8d0fbee95e85e.png"
    photo_file = FSInputFile(path="./media/images/kitob.jpg")
    await message.reply_photo(
        photo=photo_url,
        caption="Dasturlash asoslari kitobi. \nNarxi: 50000 so'm",
    )
    await message.reply_photo(
        photo_file, caption="Dasturlash asoslari kitobi. \nNarxi: 50000 so'm"
    )


@media_router.message(Command("kurslar"))
async def send_courses(message: Message):
    media_group = MediaGroupBuilder(caption="Bizning online kurslarimiz")

    photo1 = "https://res.cloudinary.com/daily-now/image/upload/f_auto,q_auto/v1/posts/a1a18f6a8827a1657f8f65b368352a9d?_a=AQAEuiZ"
    photo2 = FSInputFile("./media/images/algoritm.png")

    # Dynamically add photo with known type without using separate method
    media_group.add(type="photo", media=photo1)
    media_group.add(type="photo", media=photo2)
    await message.reply_media_group(media=media_group.build())
