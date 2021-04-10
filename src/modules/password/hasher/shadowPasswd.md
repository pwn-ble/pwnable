## /etc/shadow entry: `pwnable:RgM0tQYiWpC2o:18720:0:99999:7:::`

## /etc/passwd entry: `pwnable:x:1000:1000::/home/pwnable:/bin/bash`

John the Ripper's `unshadow` command combines the 2 by replacing the `x` in `/etc/passwd` with the hash string from `/etc/shadow`