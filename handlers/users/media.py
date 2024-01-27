from aiogram.types import ContentType, Message, InputFile, MediaGroup
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.chat.id

    photo_file_id = 'id_photo'
    photo_url = 'sf'
    photo_bites = InputFile(path_or_bytesio='media/photo2.jpg')

    await dp.bot.send_photo(chat_id=chat_id, photo=photo_file_id)


# @dp.message_handler(Command('album'))
# async def send_album(message: Message):
#     album = MediaGroup()
#     album.attach_photo(photo=) # для добовления фото
#     await message.answer_media_group(media=album)
