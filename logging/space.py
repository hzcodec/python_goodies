# Auther      : Heinz Samuelsson
# Date        : fre 25 mar 2016 10:25:51 CET
# File        : space.py
# Reference   : -
# Description : Test of logging function. Used toghether with gun.py
#
# Python ver : 2.7.3 (gcc 4.6.3)

from gun import Gun
import logging

NO_OF_DELIMETER = 120
HELP_STRING     = 'Levels: CRITICAL (4), ERROR (3), WARNING (2), DEBUG (1), INFO (0)'


class SpaceShip(object):
  def __init__(self, name):
    logging.debug('name=%s', name)
    self.spaceShipName = name
    self.laserGun  = Gun('Laser')
    self.plasmaGun = Gun('Plasma')

  def SpaceShip__fireGun(self, gun):
    logging.info('Gun is fired!')
    logging.debug('gun=%s, self.spaceShipName=%s', gun, self.spaceShipName)
    if gun == 'Laser':
      self.laserGun.Gun__fire()
      logging.info('Laser gun selected for spaceship %s', self.spaceShipName)
    elif gun == 'Plasma':
      self.plasmaGun.Gun__fire()
      logging.info('Plasma gun selected for spaceship %s', self.spaceShipName)
    else:
      logging.error('gun=%s, type does not exists', gun)
      print 'No gun selected'

  def SpaceShip__updateShip(self):
    logging.warning('Ship %s updated', self.spaceShipName)
    self.laserGun.Gun__reload()
    self.plasmaGun.Gun__reload()


# ----------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------
def main():

  print NO_OF_DELIMETER*'.'
  spaceShip_Enterprize = SpaceShip('Enterprize')
  spaceShip_Explorer   = SpaceShip('Explorer')
  print NO_OF_DELIMETER*'.'

  spaceShip_Explorer.SpaceShip__fireGun('Laser')
  spaceShip_Explorer.SpaceShip__fireGun('Plasma')
  print NO_OF_DELIMETER*'-'

  spaceShip_Enterprize.SpaceShip__fireGun('Plasma')
  spaceShip_Enterprize.SpaceShip__fireGun('Blob')

  spaceShip_Enterprize.SpaceShip__updateShip()


if __name__ == '__main__':

  from optparse import OptionParser

  parser = OptionParser('Test logging')
  parser.add_option('-d', '--debug', type='string', help=HELP_STRING, default='CRITICAL')
  options, args = parser.parse_args()

  try:
    loglevel = getattr(logging, options.debug)

  except AttributeError:
    loglevel = {4:logging.CRITICAL,
                3:logging.ERROR,
                2:logging.WARNING,
                1:logging.DEBUG,
                0:logging.INFO,
                }[int(options.debug)]

  logging.basicConfig(filename='log.txt', level=loglevel, datefmt='%Y-%m-%d %H:%M:%S', format='[%(asctime)s] %(filename)s:%(lineno)s - [%(levelname)s]- %(funcName)s() - %(message)s')

  main()

