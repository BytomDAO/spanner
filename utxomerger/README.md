# UTXO merger


> **One last disclaimer:**

**The code we are about to go over is in no way intended to be used as an example of a robust solution.**

**We wouldn't be responsible for the consequences of using this tool.**

**Please check this python code carefully and use it later.**


## Preparation

- Requirements: Python 3.x, with requests package

- Dependencies:
   ```
    pip install requests
   ```

## Usage:


   ```
    ./bytomd init --chain_id mainnet
   ```
   ```
    cd utxomerger
    python merge_utxo.py [options]
   ```
   If you don't know how to run bytomd please check this [wiki](https://github.com/Bytom/bytom/wiki/Build-and-Install)

- Options:


  ```
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

## Example

  
**eg.01:**

   ```
$ python btmspanner.py utxomerger -l
   ```
   this example can list all utxos at localhost.

**eg.02:**

   ```
$ python btmspanner.py utxomerger -o http://127.0.0.1:9888 -l
   ```
   this example can list all utxos at host http://127.0.0.1:9888.

**eg.03:**

   ```
$ python btmspanner.py utxomerger -o http://127.0.0.1:9888 -a your_account_alias -p your_password -x 41250000000 -s 0 -m 20 -f 3 -y
   ```

**Result:**

```
$ python btmspanner.py utxomerger -o http://52.83.158.112:9888 -a btmpool_test -p btmpool -x 41250000000 -s 0 -m 20 -f 3 -y
   0.  412.50000000 BTM fac1fa4776c43e2159683c6ce7ffdd64734be2bd982d997b59fa8198c6af4d1c (mature)
   1.  412.50000000 BTM f7065066c92ec44986b8f19e29dc7b7fcadecd54544fd97124640a9118e897ca (mature)
   2.  412.50000000 BTM e59676bb52ad8e1bb601603f4a34a1e43626fc69cdf65a73016cddfc4877e399 (mature)
   3.  412.50000000 BTM e582399482fdc941dacf02041d21e0d29cfe6c3fe8d2ad4092de5dc9f7e91fef (mature)
   4.  412.50000000 BTM e56e1fcc4415637c7d4ef7e4604047ebbe67c39a1642686382b6b233be93f10b (mature)
   5.  412.50000000 BTM e529442ad904e8a4f37b3cd8935376858bbcf37ecc81ee0b5b33deb8f2a8a818 (mature)
   6.  412.50000000 BTM e5267499cfb321829eda3c2fd85d535640202b43abf6cdc3c46c08f5074a81b2 (mature)
   7.  412.50000000 BTM e503b1e89a3bf9724db495b47704a45bb5b684def45db822ee3c9601b1b74254 (mature)
   8.  412.50000000 BTM e4c75c64e847b0d69c323561267cb7f6a1606e3c261da4e3996ed6d056c17b2a (mature)
   9.  412.50000000 BTM e4b0b52a016d1db20c21742bb99b800fa44dbb4b4d9741ef49140527a04b83d4 (mature)
  10.  412.50000000 BTM e492b09256943979f1c3e3992e186202038e891dc4f2a935a9c75cf3d0b522c2 (mature)
  11.  412.50000000 BTM e4917857edfd64c07c8b8be0dc699fff472fcd7f90223f5a305a702e058cfb1d (mature)
  12.  412.50000000 BTM e48d180aa1c6b4c20ea8919105558fea62d14a2b129760780e345ee7ceb5344c (mature)
  13.  412.50000000 BTM e48716fe2e3ddfebac926eb6ea7c7f514b3ba5106e919b0bfd05385d965d5c44 (mature)
  14.  412.50000000 BTM e484803600da4c55da6dbf75132b91b19e02b8bec1a5dfcee4dce4e05d8369cc (mature)
  15.  412.50000000 BTM e4752c66f529528e0dba113e52412dd89590110fbd48a1b3f2f1262a0a0017dd (mature)
  16.  412.50000000 BTM e4737d15af5b8c0fa8d35585cf8ea954bd8661d95c8815706aa2023456825929 (mature)
  17.  412.50000000 BTM e46a66bd8c4c4d9179b046769c772d885e190ed8c886cb3e7f067d50dad6d642 (mature)
  18.  412.50000000 BTM e45c99d0c10da07fa552397d7f47cfbe127e409aa84af013625136d1e4ac8f44 (mature)
  19.  412.50000000 BTM e43ec438d3e7c9adb9a824d00213e06653beaea7d14769f2d679a357789f7d43 (mature)
  20.  412.50000000 BTM e43d7822e311b218741cee47be8206f497d2bcf09289261767c506363bbc581c (mature)
  21.  412.50000000 BTM e41bd6d7ee12bc0a31f6e18eb55a21b67d33ef832ebd406df19c391b6db35671 (mature)
  22.  412.50000000 BTM e3dd87d9360f88deea845d2e1427cfcbdba07c89960e3ab28d400386e44a01b5 (mature)
  23.  412.50000000 BTM e38cfab43d7378c0b1daef623d1d6780fc1916835030b9d8a1d767fb907ece59 (mature)
  24.  412.50000000 BTM e3838051192d4c18c91f423a33cd3bf3d1c651f7fda82fd8bd1a9ca9a6b3c255 (mature)
  25.  412.50000000 BTM e36c1cacd5f8076ccfcdaba9cc4535424eead5bf1c3f0056fdb4f3299f4b7809 (mature)
  26.  412.50000000 BTM e36783989966e30addfae455b47c48fd28a12d6ffffc89174905747b4f922ebc (mature)
  27.  412.50000000 BTM e3635e2da1951a7d6978ba460de2d391dcb2ea43d47823a97e4a78b10750c25b (mature)
  28.  412.50000000 BTM e35800c843235cc5190dedffb9ec47fea6cc7de8be3095b56c0b6bf4854f2956 (mature)
  29.  412.50000000 BTM e33fd6a2e5b97d844b86d66119e5261de9a834de21d27b26492176b0df11f003 (mature)
  30.  412.50000000 BTM e335a1c989bb737fb803c7bda33abdcfdc6438e5c04706ca83faed26fb2aa80d (mature)
  31.  412.50000000 BTM e3184af7738ff5d963491f723450aeab82a6272f41d1c5525a9e715294209922 (mature)
  32.  412.50000000 BTM e30d84b5610f4d5d028a49fe37167859aea5e3a3f20040d19091cac1b97b2be2 (mature)
  33.  412.50000000 BTM e306c2614ec834c87329323c3582e90be1c8a3ca6f56ce3b0e3cc554016a2a4e (mature)
  34.  412.50000000 BTM e2fb226581e1abefa20e2ad31a27a0796f60ca478a53d54b0726d9e379cfb2ff (mature)
  35.  412.50000000 BTM e258bc0106102c1ac1d46c5ec950f56572ed4431a6b56d42da5e2a5028ab06a5 (mature)
  36.  412.50000000 BTM e253836d0db710a0a35b31e739b3adafbc8164bb5ccaeea10759d84199251ae9 (mature)
  37.  412.50000000 BTM e218a03a677379c5772be887176a0dd4cdcb614714039692159edaa14970e1fd (mature)
  38.  412.50000000 BTM e1d76391823d6882a4483daa62e03ca936f336c394d815584f34781f83395107 (mature)
  39.  412.50000000 BTM e17315ccb095f012ee2a70ce879606795263ae7b0a50445a423c0bafb8cd13e4 (mature)
  40.  412.50000000 BTM e16f2e0f8e386d2c1ca144a5a50ab0e79195b30de359481ea03bca73eb16b3b3 (mature)
  41.  412.50000000 BTM e16a9fb91d1e708716da6ed93b486fde9f29525d4dbdf7c6b4e1b45ffca8111f (mature)
  42.  412.50000000 BTM e15000bd16de54e640b986549582515cbed7c45557d9aff9ab7578c44aa5d981 (mature)
  43.  412.50000000 BTM e149fda118008540986e31939f4f4903eda0fbe8a27c21d336384102e4a1b199 (mature)
  44.  412.50000000 BTM e1252730013f786f711d0e246ed7ae5671216092f73c71e98b6788e1ca271116 (mature)
  45.  412.50000000 BTM e0ba3a38ca04aaa7b5993fb8d818ad414bfd4186132b8a0d85b9aa1178415aab (mature)
  46.  412.50000000 BTM e0b20909de104f4101686fc94a6ae7e8a4b1f2e588b09b6241b213dd797a58c6 (mature)
  47.  412.50000000 BTM e0a6f9ed53edec3ca2c9bb383167c13d75539ccd111bfaaee5e5d18f036077f0 (mature)
  48.  412.50000000 BTM e09be71db521bfaaedeef2d51b1cd87c0324b06d03ae2ecb5ac98d335b5bcb0e (mature)
  49.  412.50000000 BTM e097c5c4e6e0dde8044dd6989da1e6924dcc06090d88129ff19c02a740235159 (mature)
  50.  412.50000000 BTM e034fe335ba7d6b40b288f9d6680e34f72e5d0cef67704a7b2fe09977703a86a (mature)
  51.  412.50000000 BTM e0223b5eb6d578fa99b48b82d7e06f2c91d3388653297bd39383d2c71a5ac0c3 (mature)
  52.  412.50000000 BTM e019f8ff7f1e0decc6cd7f60d1d3849d97a99d858754dcc6128f36a19fd01f0f (mature)
  53.  412.50000000 BTM dfdab7ea3b95377639e57ce51d9b846d54c082babb4b9422dc7efadd569c5ab9 (mature)
  54.  412.50000000 BTM dfce7685cd0a39afacbbc410a48acbb08eb133c8b8842eeac4b05607c665a354 (mature)
  55.  412.50000000 BTM dfb270c4771bf65972810b666271933f35479128f4bf9082083a569801306ac1 (mature)
  56.  412.50000000 BTM df3404da190a3670731d8a785a61d687860a4c2c0e21c53cb9e3bde034f460f4 (mature)
  57.  412.50000000 BTM df28d92522fe8cb4ab119b5e2c7afd351930cf50face5a0fd2490309010f1011 (mature)
  58.  412.50000000 BTM df2547dcf8d8fd44c7e58c3562044bf9851d503b0822d31379600a5a88ab095c (mature)
  59.  412.50000000 BTM dea768baf3f3566620cdee42125060a242542562994e7fde461d178db68a388a (mature)
  60.  412.50000000 BTM de5edab407e5a90c90122a170bdf3695cf1fb6fea8828bd4d0c170a3a35294eb (mature)
total size of available utxos is 2057
To merge 60 UTXOs with 24750.00000000 BTM totally.

One last disclaimer: the code we are about to go over is in no way intended to be used as an example of a robust solution.
You will transfer BTM to an address, please check this python code and DO IT later.

this is the 1 times to merge utxos. -----begin
   0.  412.50000000 BTM fac1fa4776c43e2159683c6ce7ffdd64734be2bd982d997b59fa8198c6af4d1c (mature)
   1.  412.50000000 BTM f7065066c92ec44986b8f19e29dc7b7fcadecd54544fd97124640a9118e897ca (mature)
   2.  412.50000000 BTM e59676bb52ad8e1bb601603f4a34a1e43626fc69cdf65a73016cddfc4877e399 (mature)
   3.  412.50000000 BTM e582399482fdc941dacf02041d21e0d29cfe6c3fe8d2ad4092de5dc9f7e91fef (mature)
   4.  412.50000000 BTM e56e1fcc4415637c7d4ef7e4604047ebbe67c39a1642686382b6b233be93f10b (mature)
   5.  412.50000000 BTM e529442ad904e8a4f37b3cd8935376858bbcf37ecc81ee0b5b33deb8f2a8a818 (mature)
   6.  412.50000000 BTM e5267499cfb321829eda3c2fd85d535640202b43abf6cdc3c46c08f5074a81b2 (mature)
   7.  412.50000000 BTM e503b1e89a3bf9724db495b47704a45bb5b684def45db822ee3c9601b1b74254 (mature)
   8.  412.50000000 BTM e4c75c64e847b0d69c323561267cb7f6a1606e3c261da4e3996ed6d056c17b2a (mature)
   9.  412.50000000 BTM e4b0b52a016d1db20c21742bb99b800fa44dbb4b4d9741ef49140527a04b83d4 (mature)
  10.  412.50000000 BTM e492b09256943979f1c3e3992e186202038e891dc4f2a935a9c75cf3d0b522c2 (mature)
  11.  412.50000000 BTM e4917857edfd64c07c8b8be0dc699fff472fcd7f90223f5a305a702e058cfb1d (mature)
  12.  412.50000000 BTM e48d180aa1c6b4c20ea8919105558fea62d14a2b129760780e345ee7ceb5344c (mature)
  13.  412.50000000 BTM e48716fe2e3ddfebac926eb6ea7c7f514b3ba5106e919b0bfd05385d965d5c44 (mature)
  14.  412.50000000 BTM e484803600da4c55da6dbf75132b91b19e02b8bec1a5dfcee4dce4e05d8369cc (mature)
  15.  412.50000000 BTM e4752c66f529528e0dba113e52412dd89590110fbd48a1b3f2f1262a0a0017dd (mature)
  16.  412.50000000 BTM e4737d15af5b8c0fa8d35585cf8ea954bd8661d95c8815706aa2023456825929 (mature)
  17.  412.50000000 BTM e46a66bd8c4c4d9179b046769c772d885e190ed8c886cb3e7f067d50dad6d642 (mature)
  18.  412.50000000 BTM e45c99d0c10da07fa552397d7f47cfbe127e409aa84af013625136d1e4ac8f44 (mature)
  19.  412.50000000 BTM e43ec438d3e7c9adb9a824d00213e06653beaea7d14769f2d679a357789f7d43 (mature)
total size of available utxos is 20
To merge 20 UTXOs with 8250.00000000 BTM
tx_id: 52b272e63d285c8011ef93eea399724dbe34145f81a1a0a6d6eed14ee9fb33ce
this is the 1 times to merge utxos. -----end

this is the 2 times to merge utxos. -----begin
  20.  412.50000000 BTM e43d7822e311b218741cee47be8206f497d2bcf09289261767c506363bbc581c (mature)
  21.  412.50000000 BTM e41bd6d7ee12bc0a31f6e18eb55a21b67d33ef832ebd406df19c391b6db35671 (mature)
  22.  412.50000000 BTM e3dd87d9360f88deea845d2e1427cfcbdba07c89960e3ab28d400386e44a01b5 (mature)
  23.  412.50000000 BTM e38cfab43d7378c0b1daef623d1d6780fc1916835030b9d8a1d767fb907ece59 (mature)
  24.  412.50000000 BTM e3838051192d4c18c91f423a33cd3bf3d1c651f7fda82fd8bd1a9ca9a6b3c255 (mature)
  25.  412.50000000 BTM e36c1cacd5f8076ccfcdaba9cc4535424eead5bf1c3f0056fdb4f3299f4b7809 (mature)
  26.  412.50000000 BTM e36783989966e30addfae455b47c48fd28a12d6ffffc89174905747b4f922ebc (mature)
  27.  412.50000000 BTM e3635e2da1951a7d6978ba460de2d391dcb2ea43d47823a97e4a78b10750c25b (mature)
  28.  412.50000000 BTM e35800c843235cc5190dedffb9ec47fea6cc7de8be3095b56c0b6bf4854f2956 (mature)
  29.  412.50000000 BTM e33fd6a2e5b97d844b86d66119e5261de9a834de21d27b26492176b0df11f003 (mature)
  30.  412.50000000 BTM e335a1c989bb737fb803c7bda33abdcfdc6438e5c04706ca83faed26fb2aa80d (mature)
  31.  412.50000000 BTM e3184af7738ff5d963491f723450aeab82a6272f41d1c5525a9e715294209922 (mature)
  32.  412.50000000 BTM e30d84b5610f4d5d028a49fe37167859aea5e3a3f20040d19091cac1b97b2be2 (mature)
  33.  412.50000000 BTM e306c2614ec834c87329323c3582e90be1c8a3ca6f56ce3b0e3cc554016a2a4e (mature)
  34.  412.50000000 BTM e2fb226581e1abefa20e2ad31a27a0796f60ca478a53d54b0726d9e379cfb2ff (mature)
  35.  412.50000000 BTM e258bc0106102c1ac1d46c5ec950f56572ed4431a6b56d42da5e2a5028ab06a5 (mature)
  36.  412.50000000 BTM e253836d0db710a0a35b31e739b3adafbc8164bb5ccaeea10759d84199251ae9 (mature)
  37.  412.50000000 BTM e218a03a677379c5772be887176a0dd4cdcb614714039692159edaa14970e1fd (mature)
  38.  412.50000000 BTM e1d76391823d6882a4483daa62e03ca936f336c394d815584f34781f83395107 (mature)
  39.  412.50000000 BTM e17315ccb095f012ee2a70ce879606795263ae7b0a50445a423c0bafb8cd13e4 (mature)
total size of available utxos is 20
To merge 20 UTXOs with 8250.00000000 BTM
tx_id: 584a4087a67ef4a1dc09f7ef30c6c20415d5cb107c9c9af4d1be66b6aa0eb46c
this is the 2 times to merge utxos. -----end

this is the 3 times to merge utxos. -----begin
  40.  412.50000000 BTM e16f2e0f8e386d2c1ca144a5a50ab0e79195b30de359481ea03bca73eb16b3b3 (mature)
  41.  412.50000000 BTM e16a9fb91d1e708716da6ed93b486fde9f29525d4dbdf7c6b4e1b45ffca8111f (mature)
  42.  412.50000000 BTM e15000bd16de54e640b986549582515cbed7c45557d9aff9ab7578c44aa5d981 (mature)
  43.  412.50000000 BTM e149fda118008540986e31939f4f4903eda0fbe8a27c21d336384102e4a1b199 (mature)
  44.  412.50000000 BTM e1252730013f786f711d0e246ed7ae5671216092f73c71e98b6788e1ca271116 (mature)
  45.  412.50000000 BTM e0ba3a38ca04aaa7b5993fb8d818ad414bfd4186132b8a0d85b9aa1178415aab (mature)
  46.  412.50000000 BTM e0b20909de104f4101686fc94a6ae7e8a4b1f2e588b09b6241b213dd797a58c6 (mature)
  47.  412.50000000 BTM e0a6f9ed53edec3ca2c9bb383167c13d75539ccd111bfaaee5e5d18f036077f0 (mature)
  48.  412.50000000 BTM e09be71db521bfaaedeef2d51b1cd87c0324b06d03ae2ecb5ac98d335b5bcb0e (mature)
  49.  412.50000000 BTM e097c5c4e6e0dde8044dd6989da1e6924dcc06090d88129ff19c02a740235159 (mature)
  50.  412.50000000 BTM e034fe335ba7d6b40b288f9d6680e34f72e5d0cef67704a7b2fe09977703a86a (mature)
  51.  412.50000000 BTM e0223b5eb6d578fa99b48b82d7e06f2c91d3388653297bd39383d2c71a5ac0c3 (mature)
  52.  412.50000000 BTM e019f8ff7f1e0decc6cd7f60d1d3849d97a99d858754dcc6128f36a19fd01f0f (mature)
  53.  412.50000000 BTM dfdab7ea3b95377639e57ce51d9b846d54c082babb4b9422dc7efadd569c5ab9 (mature)
  54.  412.50000000 BTM dfce7685cd0a39afacbbc410a48acbb08eb133c8b8842eeac4b05607c665a354 (mature)
  55.  412.50000000 BTM dfb270c4771bf65972810b666271933f35479128f4bf9082083a569801306ac1 (mature)
  56.  412.50000000 BTM df3404da190a3670731d8a785a61d687860a4c2c0e21c53cb9e3bde034f460f4 (mature)
  57.  412.50000000 BTM df28d92522fe8cb4ab119b5e2c7afd351930cf50face5a0fd2490309010f1011 (mature)
  58.  412.50000000 BTM df2547dcf8d8fd44c7e58c3562044bf9851d503b0822d31379600a5a88ab095c (mature)
  59.  412.50000000 BTM dea768baf3f3566620cdee42125060a242542562994e7fde461d178db68a388a (mature)
total size of available utxos is 20
To merge 20 UTXOs with 8250.00000000 BTM
tx_id: 04ff642f23f71710cf239a2533b5f4a9af57835d49068f5ae97054d1887b4343
this is the 3 times to merge utxos. -----end
```