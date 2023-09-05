import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from db import catprefijos as catprefijoDBMODEL, session
class catprefijosSchema(SQLAlchemyObjectType):
    class Meta:
        model=catprefijoDBMODEL
        interfaces=(relay.Node,)
class Query(graphene.ObjectType):
    node=relay.Node.Field()
    all_prefijos=SQLAlchemyConnectionField(catprefijosSchema.connection)
schema=graphene.Schema(query=Query)