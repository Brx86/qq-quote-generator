from contextlib import asynccontextmanager
from typing import AsyncIterator, Literal
from playwright.async_api import Browser, Playwright, Page, async_playwright

_playwright: Playwright | None = None
_browser: Browser | None = None


async def init() -> Browser:
    global _playwright
    global _browser
    _playwright = await async_playwright().start()
    _browser = await _playwright.firefox.launch(headless=False)
    return _browser


async def get_browser() -> Browser:
    return _browser if _browser and _browser.is_connected() else await init()


@asynccontextmanager
async def get_new_page() -> AsyncIterator[Page]:
    browser = await get_browser()
    page = await browser.new_page()
    try:
        yield page
    finally:
        await page.close()


async def screenshot(
    url: str = "",
    html: str = "",
    locate: str = "",
    type: Literal["jpeg", "png"] = "png",
) -> bytes:
    """网页截图

    Args:
        url (str): 网址
        type (Literal["jpeg", "png"], optional): 图片格式. 默认为 "png".

    Returns:
        bytes: 截图数据
    """
    async with get_new_page() as page:
        if url:
            await page.goto(url)
        if html:
            await page.set_content(html)
        if locate:
            return await page.locator(locate).screenshot(type=type)
        return await page.screenshot(full_page=True, type=type)


async def main(url):
    img = await screenshot(url)
    with open("file.png", "wb") as f:
        f.write(img)


if __name__ == "__main__":
    import asyncio
    import sys

    asyncio.run(main(sys.argv[1]))
