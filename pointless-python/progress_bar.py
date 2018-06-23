#!/usr/bin/env python3

import time, random
from tqdm import tqdm

def main():
    for x in tqdm(range(10)):
        time.sleep(random.randint(1, 3))
    


main()