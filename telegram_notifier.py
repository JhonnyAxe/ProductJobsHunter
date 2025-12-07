import asyncio
import html
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

        # Экранируем пользовательские значения для безопасного HTML
        escaped_vacancy_text = html.escape(vacancy_text)
        channel_name = html.escape(vacancy_data.get('channel_name', 'Неизвестно'))
        contacts = html.escape(vacancy_data.get('contacts') or 'не указаны')
        salary = html.escape(vacancy_data.get('salary') or 'не указана')
        views = html.escape(str(vacancy_data.get('views', 0)))
        forwards = html.escape(str(vacancy_data.get('forwards', 0)))
        message_link = html.escape(vacancy_data.get('message_link', '#'))

        # Формируем текст сообщения в HTML согласно шаблону
        message = (
            f'<b>🔍 Новая продуктовая вакансия!</b>\n\n'
            f'💼 Канал: {channel_name}\n'
            f'📅 Дата публикации: {date_str}\n'
            f'📞 Контакты: {contacts}\n'
            f'💰 Зарплата: {salary}\n\n'
            f'📊 Статистика:\n'
            f'👁 Просмотры: {views}\n'
            f'🔄 Репосты: {forwards}\n\n'
            f'🔗 <a href="{message_link}">Ссылка на оригинал</a>\n\n'
            f'📝 Описание:\n\n'
            f'{escaped_vacancy_text}'
        )
        
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
