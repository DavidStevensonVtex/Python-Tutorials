from typing import Optional

_cache: dict[str, str] = {"питон": "python"}


def fetch_translation(word: str, target_lang: str, default_lang: str) -> Optional[str]:
    return None


def translate(word: str) -> Optional[str]:
    from_cache: Optional[str] = _cache.get(word)
    if from_cache is not None:
        return from_cache
    fetched: Optional[str] = fetch_translation(word, "ru", "en")
    if fetched is None:
        return None
    _cache[word] = fetched
    return fetched


print(translate("питон"))
