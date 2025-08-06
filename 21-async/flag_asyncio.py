import asyncio

from httpx import AsyncClient
from flags_single import BASE_URL, save_flag, main


async def get_flag(client: AsyncClient, cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1,
                            follow_redirects=True)
    resp.raise_for_status()
    return resp.read()


async def download_one(client: AsyncClient, cc: str):
    image = await get_flag(client, cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    return asyncio.run(supervisor(cc_list))


async def supervisor(cc_list: list[str]) -> int:
    async with AsyncClient() as client:
        to_do = [download_one(client, cc) for cc in cc_list]
        res = await asyncio.gather(*to_do)
        return len(res)


if __name__ == '__main__':
    main(download_many)
