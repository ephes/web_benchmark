import time
import httpx
import uvloop
import asyncio


def get_api_urls(num=10):
    # base_url = "http://staging.wersdoerfer.de:8000/api/"
    base_url = "https://staging.wersdoerfer.de/api/"
    return [f"{base_url}?task_id={task_id}" for task_id in range(num)]


async def fetch(client, urls):
    responses = await asyncio.gather(*[client.get(url) for url in urls])
    return [r.json() for r in responses]


async def main():
    responses = []
    urls = get_api_urls(num=2000)
    limits = httpx.Limits(max_keepalive_connections=20, max_connections=80)  # 104
    # limits = httpx.Limits(max_keepalive_connections=10, max_connections=20)  # 104
    # limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)  # 102
    s = time.perf_counter()
    async with httpx.AsyncClient(limits=limits, timeout=20.0) as client:
        responses = await fetch(client, urls)
    elapsed = time.perf_counter() - s
    print(f"elapsed time: {elapsed}")
    requests_per_second = len(urls) / elapsed
    print(f"requests/s: {requests_per_second}")


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
asyncio.run(main())
