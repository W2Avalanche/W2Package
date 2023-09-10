from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum, IntEnum

class PickPhasesEnum(IntEnum):
    ban_blue_1 = 0
    ban_red_1 = 1
    ban_blue_2 = 2
    ban_red_2 = 3
    ban_blue_3 = 4
    ban_red_3 = 5
    pick_blue_1 = 6
    pick_red_1 = 7
    pick_red_2 = 8
    pick_blue_2 = 9
    pick_blue_3 = 10
    pick_red_3 = 11
    ban_red_4 = 12
    ban_blue_4 = 13
    ban_red_5 = 14
    ban_blue_5 = 15
    pick_red_4 = 16
    pick_blue_4 = 17
    pick_blue_5 = 18
    pick_red_5 = 19
    ended = 20

    def is_blue_turn(self):
        return self in {PickPhasesEnum.ban_blue_1, PickPhasesEnum.ban_blue_2, PickPhasesEnum.ban_blue_3, PickPhasesEnum.ban_blue_4, PickPhasesEnum.ban_blue_5, PickPhasesEnum.pick_blue_1, PickPhasesEnum.pick_blue_2, PickPhasesEnum.pick_blue_3, PickPhasesEnum.pick_blue_4, PickPhasesEnum.pick_blue_5}

    def is_red_turn(self):
        return self in {PickPhasesEnum.ban_red_1, PickPhasesEnum.ban_red_2, PickPhasesEnum.ban_red_3, PickPhasesEnum.ban_red_4, PickPhasesEnum.ban_red_5, PickPhasesEnum.pick_red_1, PickPhasesEnum.pick_red_2, PickPhasesEnum.pick_red_3, PickPhasesEnum.pick_red_4, PickPhasesEnum.pick_red_5}

class GameTeam(BaseModel):
    picks: list[str]
    bans: list[str]
    active: bool

class GameStatus(BaseModel):
    blue_team : GameTeam
    red_team : GameTeam
    phase: PickPhasesEnum

class GameConfig(BaseModel):
    blue_team_id: str
    blue_team_players_id: list[str]
    red_team_id: str
    red_team_players_id: list[str]
    tournament_id: str

class GameMessage:
    origin: str
    type: str
    status: Optional[GameStatus]
    config: Optional[GameConfig]