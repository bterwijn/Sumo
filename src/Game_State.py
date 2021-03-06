
import pygame

import Player

class Game_State:

    def __init__(self,world_size):
        self.world_size=world_size
        self.players={}

    def update(self,elapsed_time,actions):
        for name,action_list in actions.get_actions().items():
            if name not in self.players:
                print("new player:",name)
                self.players[name]=Player.Player(self.world_size)
            self.players[name].update(action_list,self.world_size)

    def draw(self,screen):
        screen.fill((0,0,0))
        for name,player in self.players.items():
            player.draw(screen)
        pygame.display.flip()
