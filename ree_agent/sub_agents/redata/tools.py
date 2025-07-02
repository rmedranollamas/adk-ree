import logging
import ssl
import urllib.request
from datetime import datetime

import certifi
from google.adk.tools import ToolContext

logger = logging.getLogger(__name__)


def fetch_api(url: str, tool_context: ToolContext) -> dict[str, str]:
    """Retrieve the content of 'url' and store it in the ToolContext."""
    context = ssl.create_default_context(cafile=certifi.where())
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "Mozilla/5.0")]
    urllib.request.install_opener(opener)
    logger.debug("Fetching page: %s", url)
    try:
        page = urllib.request.urlopen(url, context=context)
        page_text = page.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        errmsg = f"Failed to fetch page {url}: {err}"
        logger.error(errmsg)
        return {"status": "ERROR", "message": errmsg}
    tool_context.state.update({"page_contents": page_text})
    return {"status": "OK"}


def get_date() -> str:
    """Return the current date and time in ISO8601 format (YYYY-MM-DDTHH:MM)."""
    return datetime.now().strftime("%Y-%m-%dT%H:%M")
