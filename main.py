import asyncio
from crawl4ai import *


async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
        )
        # print(result.markdown)
        with open("output/nbcnews_output.md", "w") as f:
            f.write(result.markdown)


if __name__ == "__main__":
    asyncio.run(main())
