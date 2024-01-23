from ShootingStrategies.ShootStrategy import ShootStrategy
from Projectile import Projectile

class BigShoot(ShootStrategy):
    def shoot(self,pool,pos):
      missile = pool.get_object(Projectile.__name__)
      missile.set_type("missile",15)
      missile.enable(*pos)
      return [missile]

