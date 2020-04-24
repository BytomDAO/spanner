# spanner
Python based bytom and vapor wallet tools

Requirements: Python 3.x, with requests package

Dependencies:
   ```
    pip install requests
   ```
Prepare:
   ```
    bytomd init --chain_id mainnet
   ```
   OR  
   ```
    vapord init --chain_id mainnet
   ```
   If you don't know how to run bytomd or vapord please check [bytom wiki](https://github.com/Bytom/bytom/wiki/Build-and-Install) or [vapor wiki](https://github.com/Bytom/vapor/wiki/Build-and-Install)

## btm-sender

Tool send BTM to large numbers of address

Usage:
   ```
    spanner.py btmsender [-h] -n N -i I -a A [-s S] [-c C] [-u] [-t T]
   ```
Options:
   ```
  -h, --help      show this help message and exit
  -n node         bytomd or vapord node address
  -i input        transaction txt file
  -a account      wallet account id
  -s asset_id     transaction asset id
  -c count        transaction output count
  -u              use unconfirmed UTXO build transaction
  -t time_range   the transaction will not be submitted into block after this height
  ```
See more details in btm-sender [README.md](https://github.com/Bytom/spanner/blob/master/btmsender/README.md) file.
## utxo-merger

Tool merge some utxos to one for loops.

Usage:
```
spanner.py utxomerger [-h] [-o URL] [-a ACCOUNT_ALIAS] [-p PASSWORD]
                     [-x MAX_AMOUNT] [-s MIN_AMOUNT] [-l] [-m MERGE_LIST]
                     [-f FOR_LOOP] [-y]
```
Options:
```
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

See more details in utxo-merger [README.md](https://github.com/Bytom/spanner/blob/master/utxomerger/README.md) file.

