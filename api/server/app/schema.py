from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from app.models import Branch
import graphene

class BranchModel(DjangoObjectType):
    class Meta:
        model = Branch
        filter_fields = ['id','branch','bank_id', 'bank_name','district','state']
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    branchinfo= relay.Node.Field(BranchModel)
    all_branch_info= DjangoFilterConnectionField(BranchModel)

    def resolve_branchinfo(self,info):
        return Branch.objects.all()

schema = graphene.Schema(query=Query)