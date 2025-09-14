from typing import Any

class PreferenceHandler():

    def __init__(self, preferences: dict) -> None:
        self.user_preferences = preferences

    def get_preference(self, preference_key: str, default: Any = None) -> Any:
        return self.user_preferences.get(preference_key, default)