import asyncio
import sys
from core.utils.logger import logger
from prometheus_client import start_http_server

def check_tkinter_available():
    try:
        import customtkinter
        return True
    except ImportError:
        return False

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        logger.info("Starting console version...")
        from core.menu import ConsoleMenu
        menu = ConsoleMenu()
        start_http_server(8080)
        asyncio.run(menu.run())
            
    except KeyboardInterrupt:
        logger.info("Application terminated by user")
