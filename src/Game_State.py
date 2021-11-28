
import pygame

import Player

class Game_State:

    def __init__(self,world_size):
        self.world_size=world_size
        self.players={}
        self.deadpeople=set()

    def update(self,elapsed_time,actions):
        for name,action_list in actions.get_actions().items():
            if name in self.deadpeople: # ignore dead players
                break 
            if name not in self.players:
                print("new player:",name)
                self.players[name]=Player.Player(self.world_size)
            if name in self.players:
                self.players[name].update(action_list,self.world_size)
            self.bounce_players()
            self.kill_players()
            
    def bounce_players(self):
        list_players=list(self.players.values())
        for index1,player1 in enumerate(list_players):
            for index2 in range(index1+1, len(list_players)):
                    player1.bounce(list_players[index2])
                    
    def kill_players(self):
        list_name_players=list(self.players.items())
        for name,player in list_name_players:
            if player.radius < 10:
                print(f"Player {name} is dead" )
                self.deadpeople.add(name)
                del self.players[name]
                        
    def draw(self,screen):
        screen.fill((0,0,0))
        for name,player in self.players.items():
            player.draw(screen)
        pygame.display.flip()
