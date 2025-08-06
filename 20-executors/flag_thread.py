from concurrent import futures

from flags_single import save_flag, get_flag, main


def download_one(cc: str):
    image = get_flag(cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    with futures.ThreadPoolExecutor() as exe:
        res = exe.map(download_one, sorted(cc_list))
    return len(list(res))


if __name__ == '__main__':
    main(download_many)
