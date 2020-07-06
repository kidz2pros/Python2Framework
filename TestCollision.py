from Actor import Actor
from TestActor import TestActor


class TestCollision(Actor):

    def __init__(self):
        super(TestCollision, self).__init__()

    def act(self):
        self.collide()

    def collide(self):
        intersector = self.get_one_intersector(TestActor)
        if intersector is not None:
            self.world.remove_actor(intersector)
