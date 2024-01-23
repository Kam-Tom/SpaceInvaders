from ShootingStrategies.ShootStrategy import ShootStrategy
from Projectile import Projectile

class BigShoot(ShootStrategy):
    def shoot(self,pool,pos):
      missile = pool.get_object(Projectile.__name__)
      missile.size = (20,20)
      missile.set_type("missile",15)
      missile.enable(pos[0]-5,pos[1])
      return [missile]

