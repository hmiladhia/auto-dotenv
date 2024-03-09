import os

import dotenv


def autoload_dotenv():
    _current_env = os.environ.get("AUTO_DOTENV_ENV", None)
    _env_file = os.environ.get(
        "AUTO_DOTENV_PATH", f".env.{_current_env}" if _current_env else None
    )
    dotenv.load_dotenv(_env_file)
