import asyncio
from datetime import datetime
from loguru import logger
from telebot.async_telebot import AsyncTeleBot
import emoji
from config import BOT_TOKEN, RECIPIENT_CHAT_ID

# Инициализация бота
bot = AsyncTeleBot(BOT_TOKEN)

async def send_vacancy_notification(vacancy_data: dict):
    """Отправка уведомления о новой вакансии в личный чат с ботом"""
    try:
        # Форматируем дату
        date = datetime.strptime(vacancy_data['date'], '%Y-%m-%d %H:%M:%S')
        date_str = date.strftime('%d.%m.%Y %H:%M')
        
        # Форматируем текст вакансии (обрезаем если слишком длинный)
        vacancy_text = vacancy_data['text'][:1000]
        if len(vacancy_data['text']) > 1000:
            vacancy_text += "..."
        
        # Формируем текст сообщения в HTML
        message = (
            f'<b>🔍 Новая продуктовая вакансия!</b>\n\n'
            f'📌 <i>Pin: @vikapaleshko</i>\n\n'
            f'<b>📝 Описание:</b>\n'
            f'<pre>{vacancy_text}</pre>\n\n'
            f'<b>💼 Канал:</b> <code>{vacancy_data["channel_name"]}</code>\n'
            f'<b>📅 Дата публикации:</b> <code>{date_str}</code>\n'
        )
        
        # Добавляем контакты, если есть
        if vacancy_data.get('contacts'):
            message += f'<b>📞 Контакты:</b> <code>{vacancy_data["contacts"]}</code>\n'
            
        # Добавляем зарплату, если есть
        if vacancy_data.get('salary'):
            message += f'<b>💰 Зарплата:</b> <code>{vacancy_data["salary"]}</code>\n'
            
        # Добавляем статистику
        message += f'\n<b>📊 Статистика:</b>\n'
        message += f'👁 Просмотры: <code>{vacancy_data["views"]}</code>\n'
        message += f'🔄 Репосты: <code>{vacancy_data["forwards"]}</code>\n'
        
        # Добавляем разделитель
        message += '\n' + '─' * 30 + '\n'
        
        # Добавляем ссылку на оригинал
        message += f'🔗 <a href="{vacancy_data["message_link"]}">Ссылка на оригинал</a>'
        
        # Отправляем сообщение в личный чат
        await bot.send_message(
            RECIPIENT_CHAT_ID,
            message,
            parse_mode='HTML',
            disable_web_page_preview=True
        )

        logger.info("✅ Уведомление о вакансии отправлено в личный чат")
        
    except Exception as e:
        logger.error(f"❌ Ошибка при отправке уведомления: {e}")

async def test_notification():
    """Тестовая отправка уведомления"""
    test_data = {
        'text': 'Ищем Product Manager для мобильного продукта. 🚀\n\nТребования:\n- Опыт работы от 2 лет\n- Умение ставить и проверять гипотезы\n- Знание продуктовых метрик\n\nУсловия:\n- Удаленная работа\n- Гибкий график',
        'channel_name': '🔍 Product Вакансии',
        'date': '2025-02-07 21:55:00',
        'contacts': 'HR менеджер: @test_contact\nТелефон: +7 (999) 999-99-99',
        'salary': '200 000 - 250 000 ₽',
        'views': 1250,
        'forwards': 15,
        'message_link': 'https://t.me/test_channel/123'
    }
    try:
        await send_vacancy_notification(test_data)
    finally:
        # Закрываем сессию бота
        await bot.close_session()
        await asyncio.sleep(0.250)  # Даем время на закрытие соединений

if __name__ == '__main__':
    # Тестируем отправку уведомления
    asyncio.run(test_notification())
