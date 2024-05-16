from dotenv import load_dotenv
from .utils import update_ui_text
from .services import Pipeline
from .page_format import default_pages_config, format_an_upcoming_event_display, format_user_image_display, \
    sample_image_display

load_dotenv()
update_ui_text()  # Load UI text translations
