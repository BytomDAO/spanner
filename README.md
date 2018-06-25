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

## [btm-sender](https://github.com/Bytom/btm-spanner/blob/master/btmsender/README.md)

## btm-merger

This is a bytom tool that can merge some utxos to one.

> btm-merger Usage:
  
  ```shell
python btmspanner.py utxomerger [-h] [-o URL] [-a ACCOUNT_ALIAS] [-p PASSWORD]
                     [-x MAX_AMOUNT] [-s MIN_AMOUNT] [-l] [-m MERGE_LIST] [-y]

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
  -y, --yes             confirm transfer
  ```

> see more details in [btm-merger README.md](https://github.com/Bytom/btm-spanner/blob/master/btmsender/README.md) file.