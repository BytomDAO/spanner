# UTXO combiner

Requirements: Python 3.x, with requests package

Dependencies:
   ```
    pip install requests
   ```

Usage:
   ```
    ./bytomd init --chain_id mainnet
   ```
   ```
    python utxo_combiner.py [options]
   ```
   If you don't know how to run bytomd please check this [wiki](https://github.com/Bytom/bytom/wiki/Build-and-Install)

Options:
   ```
  -h, --help      show this help message and exit
  -c connection   connection url
  -a account      account_alias
  -p password     account password
  -m max_amount   utxo less than max_amount to combine
  -s size		  combine utxo size every time
  ```

Example:
   ```shell
python utxo_combiner.py -c http://127.0.0.1:9888 -a sheng -p 123456 -m 41250000000 -s 20
   ```

   or

   ```shell
   python utxo_combiner.py --connection http://127.0.0.1:9888 --account sheng  --password 123456 --max_amount 41250000000 --size 20
   ```