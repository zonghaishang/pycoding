import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues

from primes import is_prime, NUMBERS


class PrimerResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


JobQueue = queues.SimpleQueue[int]
ResultQueue = queues.SimpleQueue[PrimerResult]


def check(n: int) -> PrimerResult:
    t0 = perf_counter()
    prime = is_prime(n)
    return PrimerResult(n, prime, perf_counter() - t0)


def worker(jobs: JobQueue, result: ResultQueue) -> None:
    while n := jobs.get():
        result.put(check(n))
    result.put(PrimerResult(0, False, 0.0))


def start_jobs(procs: int, jobs: JobQueue, result: ResultQueue) -> None:
    for n in NUMBERS:
        jobs.put(n)

    for _ in range(procs):
        p = Process(target=worker, args=(jobs, result))
        p.start()
        jobs.put(0)


# tag::PRIMES_PROC_MAIN[]
def main() -> None:
    if len(sys.argv) < 2:  # <1>
        procs = cpu_count()
    else:
        procs = int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {procs} processes:')
    t0 = perf_counter()
    jobs: JobQueue = SimpleQueue()  # <2>
    results: ResultQueue = SimpleQueue()
    start_jobs(procs, jobs, results)  # <3>
    checked = report(procs, results)  # <4>
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')  # <5>


def report(procs: int, results: ResultQueue) -> int:  # <6>
    checked = 0
    procs_done = 0
    while procs_done < procs:  # <7>
        n, prime, elapsed = results.get()  # <8>
        if n == 0:  # <9>
            procs_done += 1
        else:
            checked += 1  # <10>
            label = 'P' if prime else ' '
            print(f'{n:16}  {label} {elapsed:9.6f}s')
    return checked


if __name__ == '__main__':
    main()
