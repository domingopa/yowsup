from yowsup.structs import ProtocolEntity, ProtocolTreeNode
from yowsup.layers.protocol_iq.protocolentities import IqProtocolEntity
class GroupsV2IqProtocolEntity(IqProtocolEntity):
    '''
    <iq type="{{get | set?}}" id="{{id}}" xmlns="w:g2", to="{{group_jid}}">
    </iq>
    '''
    def __init__(self, to = None, _from  = None, _id = None, _type = None):
        super(GroupsV2IqProtocolEntity, self).__init__("w:g2", _id, _type, to = to, _from = _from)
