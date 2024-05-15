from dotenv import load_dotenv
from .utils import update_ui_text
from .page_format import default_pages_config, format_an_upcoming_event_display

load_dotenv()
update_ui_text()  # Load UI text translations