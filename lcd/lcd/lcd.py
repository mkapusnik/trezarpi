#!/usr/bin/env python
dev = easyi2c.IIC(0x3c, 1)

def text(title, message=''):
  try:
    dev.i2c([31, 1], 0)
    sleep(0.01)
    for t in title:
      dev.i2c([32, ord(t), 0],0)
    dev.i2c([31, 0xc0], 0)
    for m in message:
      dev.i2c([32, ord(m), 0],0)
  except Exception:
    print(traceback.format_exc())