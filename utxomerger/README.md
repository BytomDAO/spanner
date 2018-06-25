# UTXO merger

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
    cd utxomerger
    python merge_utxo.py [options]
   ```
   If you don't know how to run bytomd please check this [wiki](https://github.com/Bytom/bytom/wiki/Build-and-Install)

Options:
  ```shell
  usage: python btmspanner.py utxomerger [-h] [-o URL] [-a ACCOUNT_ALIAS] [-p PASSWORD]
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

Example:
   ```shell
python btmspanner.py utxomerger -o http://127.0.0.1:9888 -a sheng -p 123456 -x 41250000000 -s 0 -l   
   ```

   or

   ```shell
python btmspanner.py utxomerger -o http://127.0.0.1:9888 -a sheng -p 123456 -x 41250000000 -s 0 -m 10
   ```

Result:
```shell
python btmspanner.py utxomerger -o http://127.0.0.1:9888 -a sheng -p 123456 -x 41250000000 -s 0 -l   
   0.  412.50000000 BTM f9c0d3831061edcf045e13e1a6408cb1794817290fceed1ef41fcbd809ef24d4 (mature)
   1.  412.50000000 BTM f98e8faf54ee9731578e973ab44dbdd2001fd254d34f5e8982de1cee0fc95126 (mature)
   2.  325.00000000 BTM f9864118a26f852149ac84d7d5b5da2bb97fb390a929a98faf3f3187c6ac6c35 (mature)
   3.  412.50000000 BTM f860fb39404fac64806eeae5f5ce7cc221fc7ab49386f84d19010fc4b0fd60c4 (mature)
   4.  412.50000000 BTM f7d895890405f228e709160231d1db4bd08fe56b20b0be92f13cd778105ce8fd (mature)
   5.  412.50000000 BTM f7d5180377f0b87dcb12ce3804bb47abe034edf5bc9d82349a87ca5533781b38 (mature)
   6.  412.50000000 BTM f7cccc6ace814de907e4ee71d8d3a8741fb341bfea96e03abcf3dc88d0a6aaa7 (mature)
   7.  412.50000000 BTM f76003ff07c92f5ddd1806d51e94c847d60b35b26da1479976fcb1d85aac3358 (mature)
   8.  412.50000000 BTM f73565bdcc54eb749599ef1ed5118381f133b10bce6cb8fcd863a9a5b133689d (mature)
   9.  412.50000000 BTM f7220f8e8f6d80bf75a6bd5af3a7f24831ff806816928d82c1df498b2cc55136 (mature)
  10.  412.50000000 BTM f6a21da21b50bed465a12f0028e01870866e2a5ddea047588b8d7f60e97c7eca (mature)
  11.  412.50000000 BTM f6933473a9ee26cb48a5ff0c4fa2c3c3464290ee5294accef7efb315a8d7efa0 (mature)
  12.  412.50000000 BTM f4372863e40dcb0092e9d4c358b7875aae57c5b41a76b88cb8e5b0c4115a8edb (mature)
  13.  412.50000000 BTM f3f07faef598e6934e1bbd5b842dd4fa91961b8efc2f782331429a423d0c2fc8 (mature)
  14.  412.50000000 BTM f355cb331def6878b118d9c99c2d915005c399c6c7af2d430da7fc4d3d495f3d (mature)
  15.  412.50000000 BTM f26d274a4374b06a1fba02a33d282cea223435c215239236ad99065007697457 (mature)
  16.  412.50000000 BTM f0be46800428a4f3dec4c167f8593a9ca0e791b08bb07b142040b3c5ac8a33a5 (mature)
  17.  412.50000000 BTM ef95348ac7e42d47af6853666bcb356b3b1a13fa1af02cb9d156cbcd18d3a519 (mature)
  18.  412.50000000 BTM ef664a0594ad4009c067a9b2556f6297f0c2deaba0d1226f782864480d0bd43e (mature)
  19.  412.50000000 BTM ef0c18355207ee87645bf43ccceca5ce4060c677b88cf5cff9dd49dd684a9e15 (mature)
  20.  412.50000000 BTM ec27d6edef04156433d7e888e5c9afddfdb04f0f737044f8ede0202ff5e71368 (mature)
  21.  412.50000000 BTM ec1ef67d64d0d35d2937fd810acd23ca30f0a54a9aa85d46d207f07a117108a1 (mature)
total size of available utxos is 395
To merge 10 UTXOs with 4037.50000000 BTM
One last disclaimer: the code we are about to go over is in no way intended to be used as an example of a robust solution.
You will transfer BTM to an address, please check this python code and DO IT later.
Confirm [y/N] y
fba70efdbdfc4901adaea5ffb56c1c79b9d6bed3e38ac9946c7925d00bc4b7f3
```