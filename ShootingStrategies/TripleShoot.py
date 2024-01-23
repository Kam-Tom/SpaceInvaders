from ShootingStrategies.ShootStrategy import ShootStrategy
from Projectile import Projectile

class TripleShoot(ShootStrategy):
    def shoot(self,pool,pos):
      missile1 = pool.get_object(Projectile.__name__)
      missile2 = pool.get_object(Projectile.__name__)
      missile3 = pool.get_object(Projectile.__name__)
      missile1.set_type("missile",15)
      missile2.set_type("missile",15)
      missile3.set_type("missile",15)
      x1 = pos[0] - 5
      x2 = pos[0]
      x3 = pos[0] + 5
      y1 = pos[1] 
      y2 = pos[1] + 5
      y3 = pos[1]
      missile1.enable(x1,y1)
      missile2.enable(x2,y2)
      missile3.enable(x3,y3)
      return [missile1, missile2, missile3]
