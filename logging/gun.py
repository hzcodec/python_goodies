# Author      : Heinz Samuelsson
# Date        : Fri Mar 25 10:38:15 CET 2016
# File        : gun.py
# Reference   : -
# Description : Used together with space.py
#
# Python ver : 2.7.3

import logging

class Gun(object):
  def __init__(self, type):
    logging.debug('Type:%s', type)
    self.noOfRounds = 10
    self.type = type

  def Gun__fire(self):
    logging.debug('Type:%s', self.type)
    self.noOfRounds -= 1
    self.Gun__getNoOfRounds()

  def Gun__reload(self):
    logging.warning('No of rounds=%s for %s', self.noOfRounds, self.type)
    self.noOfRounds = 10

  def Gun__getNoOfRounds(self):
    logging.debug('Number of rounds:%s', self.noOfRounds)
    pass

  def getType(self):
    logging.info('Type:%s', self.type)
    pass


# ---------------------------------------------------------------------------------------------------
#
# ---------------------------------------------------------------------------------------------------
def main():
  gun = Gun('laser')
  gun.Gun__fire()
  gun.Gun__reload()


if __name__ == '__main__':
  main()
