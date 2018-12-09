#!/bin/bash
import roomai

class RoleCardNames:
    sheriff        = "sheriff"
    deputy_sheriff = "deputy_sheriff"
    outlaw         = "outlaw"
    renegade       = "renegade"

class RoleCard(object):

    def __init__(self, role):
        logger = roomai.get_logger()
        if isinstance(role, str):
            logger.fatal("In the constructor RoleCard(rolecard), the rolecard must be a str.")
            raise TypeError("In the constructor RoleCard(rolecard), the rolecard must be a str.")
        if role not in [RoleCardNames.sheriff, RoleCardNames.deputy_sheriff, RoleCardNames.outlaw, RoleCardNames.renegade]:
            logger.fatal("In the constructor RoleCard(rolecard), the rolecard must be one of [%s,%s,%s,%s]"%(RoleCardNames.sheriff, RoleCardNames.deputy_sheriff, RoleCardNames.outlaw, RoleCardNames.renegade))
            raise TypeError("In the constructor RoleCard(rolecard), the rolecard must be one of [%s,%s,%s,%s]"%(RoleCardNames.sheriff, RoleCardNames.deputy_sheriff, RoleCardNames.outlaw, RoleCardNames.renegade))

        self.__role__ = role

    def __get_role__(self):
        return self.__role__
    role = property(__get_role__, doc="The rolecard")

    def __get_key__(self):  return self.__role__
    key = property(__get_key__, doc = "The key of rolecard normalcard is the rolecard")

    @classmethod
    def lookup(cls, key):
        logger = roomai.get_logger()
        if key not in RoleCardsDict:
            logger.fatal("%s is not valid rolecard key"%(key))
            raise TypeError("%s is not valid rolecard key"%(key))
        return RoleCardsDict[key]

    def __deepcopy__(self, memodict={}):
        return RoleCardsDict[self.key]

RoleCardsDict = dict()
RoleCardsDict[RoleCardNames.sheriff]        = RoleCard(RoleCardNames.sheriff)
RoleCardsDict[RoleCardNames.deputy_sheriff] = RoleCard(RoleCardNames.deputy_sheriff)
RoleCardsDict[RoleCardNames.outlaw]         = RoleCard(RoleCardNames.outlaw)
RoleCardsDict[RoleCardNames.renegade]       = RoleCard(RoleCardNames.renegade)