import asyncio
from collections import Counter
from http import HTTPStatus
from pathlib import Path

import httpx
import tqdm

from flags2_common import main, DownloadStatus, save_flag

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 50


async def get_flag(client: httpx.AsyncClient, base_url: str, cc: str) -> bytes:
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1,
                            follow_redirects=True)
    # print('req url', resp.request.url, Path(url).stem)
    resp.raise_for_status()
    return resp.content


async def download_one(client: httpx.AsyncClient,
                       cc: str,
                       base_url: str,
                       semaphore: asyncio.Semaphore,
                       verbose: bool) -> DownloadStatus:
    try:
        async with semaphore:
            image = await get_flag(client, base_url, cc)
            await asyncio.sleep(.5)
    except httpx.HTTPStatusError as exe:
        resp = exe.response
        if resp.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'not found: {resp.url}'
        else:
            raise
    else:
        await asyncio.to_thread(save_flag, image, f'{cc}.gif')
        status = DownloadStatus.OK
        msg = 'OK'
    if verbose and msg:
        print(cc, msg)
    return status


async def supervisor(cc_list: list[str],
                     base_url: str,
                     verbose: bool,
                     concur_req: int) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()
    semaphore = asyncio.Semaphore(concur_req)
    async with httpx.AsyncClient() as client:
        to_do = [download_one(client, cc, base_url, semaphore, verbose) for cc in cc_list]
        to_do_iter = asyncio.as_completed(to_do)
        if not verbose:
            to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))
        error: httpx.HTTPError | None = None
        to_do_map = {}
        for coro in to_do_iter:
            print(f'coro: {coro}')
            try:
                status = await coro
            except httpx.HTTPStatusError as exe:
                error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
                error_msg = error_msg.format(resp=exe.response)
                error = exe
            except httpx.RequestError as exe:
                error_msg = f'{exe} {type(exe)}'.strip()
                error = exe
            except KeyboardInterrupt:
                break
            else:
                error = None

            if error:
                status = DownloadStatus.ERROR
                if verbose:
                    url = str(error.request.url)
                    cc = Path(url).stem.upper()
                    print(f'{cc} error: {error_msg}')
            counter[status] += 1

    return counter


def download_many(cc_list: list[str],
                  base_url: str,
                  verbose: bool,
                  concur_req: int) -> Counter[DownloadStatus]:
    coro = supervisor(cc_list, base_url, verbose, concur_req)
    counts = asyncio.run(coro)  # <14>

    return counts


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
