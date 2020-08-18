import os
from time import sleep, time


def get_signal():
    with open("/proc/net/wireless", 'r') as f:
        auxstr = f.read().splitlines()[-1]
        aux = auxstr.split()
        signal = int(aux[3].replace('.', ''))

def get_total_bytes():
    """divide result by 10**20 to get it on MiB
    (10 ** 20? wtf quando escrevi isso?)
    """
    with open("/proc/net/dev", 'r') as f:
        auxstr = f.read().splitlines()[-1]
        aux = auxstr.split()
        bytes = int(aux[1])
    return bytes
def format_bytes(b: int) -> str:
    if b >= 10**12: #TB
        return str(b/10**12 
    if b >= 10**9: #GB
    if b >= 10**6: #MB
    if b >= 10**3: #KB
    

def get_speed(lookback=1):
    last_bytes = get_total_bytes()
    sleep(lookback)
    new_bytes = get_total_bytes()
    return (new_bytes-last_bytes)/lookback

def live_speed(lookback=3, refresh=0.05):
    t0 = time()
    last_bytes_list = []
    while 1:
        last_bytes_list.append(get_total_bytes())
        sleep(refresh)
        if time() - t0 > lookback:
            last_bytes_list.pop(0)
        print(f"{(last_bytes_list[-1] - last_bytes_list[0])/lookback:^20}", end='\r' )

