from ShootingStrategies.ShootStrategy import ShootStrategy
from Projectile import Projectile

class DoubleShoot(ShootStrategy):
    def shoot(self,pool,pos):
      missile1 = pool.get_object(Projectile.__name__)
      missile2 = pool.get_object(Projectile.__name__)
      missile1.size = (13,10)
      missile2.size = (13,10)
      missile1.set_type("missile",15)
      missile2.set_type("missile",15)
      x1 = pos[0] - 15
      x2 = pos[0] + 15
      y1 = pos[1] 
      y2 = pos[1]
      missile1.enable(x1,y1)
      missile2.enable(x2,y2)
      return [missile1,missile2]
