"""
Стоп-слова для фильтрации вакансий продуктовых менеджеров.
"""

STOP_WORDS = {
    'агентство',
    'digital-агентство',
    'беттинг',
    'букмекер',
}

def contains_stop_words(text: str) -> bool:
    """
    Проверяет, содержит ли текст стоп-слова
    
    Args:
        text: Текст для проверки
        
    Returns:
        bool: True если найдены стоп-слова, False иначе
    """
    text = text.lower()
    return any(word in text for word in STOP_WORDS)
