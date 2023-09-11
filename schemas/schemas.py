import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from db.db import catprefijos as catprefijoDBMODEL, session
class catprefijosSchema(SQLAlchemyObjectType):
    class Meta:
        model=catprefijoDBMODEL
        interfaces=(relay.Node,)
class Query(graphene.ObjectType):
    node=relay.Node.Field()
    all_prefijos=SQLAlchemyConnectionField(catprefijosSchema.connection)

class prefijoMutation(graphene.Mutation):

    class Arguments:
        keyx = graphene.Int(required=True)
        fechaalta = graphene.Date(required=True)
        prefijo=graphene.String(required=True)

    prefijo = graphene.Field(lambda: catprefijosSchema)

    def mutate(self, info, keyx, fechaalta,prefijo):
        new_prefijo = catprefijoDBMODEL(
            keyx=keyx,
            fechaalta=fechaalta,
            prefijo=prefijo
        )

        session.add(new_prefijo)
        session.commit()

        return prefijoMutation(prefijo=new_prefijo)
class Mutation(graphene.ObjectType):
    mutate_prefijo=prefijoMutation.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)