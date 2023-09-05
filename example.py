from graphene import ObjectType, Schema,String

class Query(ObjectType):
    hello=String(name=String(default_value="Stranger"))
    goodbye=String()
    def resolve_hello(root,info,name):
        return f"Hello {name}"
    def resolve_goodbye(root,info,name):
        return f"Good Bye"

schema= Schema(query=Query)
"""
type Query {
    hello(name:String="Betto")
    goodbye:String
}
"""
query_str="{hello}"
resultado=schema.execute(query_str)
print(resultado)
query_with_args='{hello(name:"Alberto")}'
resultado2=schema.execute(query_with_args)
print(resultado2)