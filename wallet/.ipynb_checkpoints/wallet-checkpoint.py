from constants import *
import subprocess
import json
import os

def derive_wallets(coin):

    mnemonic = os.getenv('MNEMONIC', 'define sample clip alarm lazy bone doll vendor tell garage jealous dolphin')
    
    command = f'./derive -g --mnemonic={mnemonic} --coin={coin} --cols=path,address,privkey,pubkey --numderive=3 --format=json'
    
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    
    return keys
