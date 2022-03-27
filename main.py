"""Main entrypoint"""
import fire
from loguru import logger

from dates.date_diff import date_diff

if __name__ == "__main__":
    try:
        fire.Fire(date_diff)
    except fire.core.FireExit as e:
        logger.error(e.trace)
