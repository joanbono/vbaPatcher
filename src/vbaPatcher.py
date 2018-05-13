#!/usr/bin/python
# Author: Joan Bono <@joan_bono>

import r2pipe
import sys

r2 = r2pipe.open(sys.argv[1])

address = r2.cmd('/ DPB')
seek_addr = address.split(' ')[0]

r2.cmd('oo+')
write2addr = 'wx 445078 @ ' + seek_addr
r2.cmd(write2addr)
printaddr = 'px 50 @ ' + seek_addr
print r2.cmd(printaddr)
r2.quit()
