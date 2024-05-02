from ast import literal_eval


def valid_attributes(attributes: dict) -> dict:
    """Конвертує всі атрибути зі строкового типу в свій власний тип."""
    return {key: literal_eval(value) for key, value in attributes.items() if value}

def valid_attribute(attribute: str) -> any:
    """Конвертує атрибут зі строкового типу в свій власний тип."""
    return literal_eval(attribute)
