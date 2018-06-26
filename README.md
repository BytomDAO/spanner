# btm-spanner
Python based Bytom wallet tools

Requirements: Python 3.x, with requests package

Dependencies:
   ```
    pip install requests
   ```
Prepare:
   ```
    bytomd init --chain_id mainnet
   ```
   If you don't know how to run bytomd please check this [wiki](https://github.com/Bytom/bytom/wiki/Build-and-Install)

## btm-sender

Bytom tool send BTM to large numbers of address

Usage:
   ```
    btmspanner.py btmsender [-h] -i I -a A -p P [-c C]
   ```
Options:
   ```
  -h, --help      show this help message and exit
  -i input        transaction txt file
  -a account      wallet account id
  -p password     wallet account password
  -c count        transaction output count
  ```
See more details in btm-sender [README.md](https://github.com/Bytom/btm-spanner/blob/master/btmsender/README.md) file.
## utxo-merger

Bytom tool merge some utxos to one for loops.

Usage:
  
  ```shell
  $ python btmspanner.py utxomerger -h
usage: btmspanner.py [-h] [-o URL] [-a ACCOUNT_ALIAS] [-p PASSWORD]
                     [-x MAX_AMOUNT] [-s MIN_AMOUNT] [-l] [-m MERGE_LIST]
                     [-f FOR_LOOP] [-y]

Bytom merge utxo tool

optional arguments:
  -h, --help            show this help message and exit
  -o URL, --url URL     API url to connect
  -a ACCOUNT_ALIAS, --account ACCOUNT_ALIAS
                        account alias
  -p PASSWORD, --pass PASSWORD
                        account password
  -x MAX_AMOUNT, --max MAX_AMOUNT
                        range lower than max_amount
  -s MIN_AMOUNT, --min MIN_AMOUNT
                        range higher than min_amount
  -l, --list            Show UTXO list without merge
  -m MERGE_LIST, --merge MERGE_LIST
                        UTXO to merge
  -f FOR_LOOP, --forloop FOR_LOOP
                        size for loop of UTXO to merge
  -y, --yes             confirm transfer
  
  ```

See more details in utxo-merger [README.md](https://github.com/Bytom/btm-spanner/blob/master/utxomerger/README.md) file.