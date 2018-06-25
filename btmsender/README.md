# btm-sender

Usage:
   ```
    btmspanner.py btmsender [options]
   ```
Options:
   ```
  -h, --help      show this help message and exit
  -i input        transaction txt file
  -a account      wallet account id
  -p password     wallet account password
  -c count        transaction output count
  ```

Example:
   ```
    btmspanner.py btmsender -i btmsender/btm.txt -a 0F0BV1OLG0A04 -p 123456 -c 1000
   ```

Transaction txt file format:
   ```
    bm1qqn5mrdcaz00d0rvqd0zuuh6z4u4a860qfquwys,265024793
    bm1qufvnqamhyjwl2c58n0t4ej27kr0xzpm4r94578,296430573
    bm1qyenrv6thy5pl2jhz08xqj7ukg3kcyn2j3mfc7n,266596998
    bm1qkkwln4xwgxfl4j838ykudecqehxes6szxmy4fl,366249088
    bm1qhsk20pnxu2yudxrucmx5pccltgew3z0e3wfqv4,225333795
   ```
