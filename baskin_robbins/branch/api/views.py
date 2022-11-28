from rest_framework.viewsets import ModelViewSet
from baskin_robbins.branch.models import Branch
from baskin_robbins.branch.api.serializers import BranchSerializer


class BranchViewSet(ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
