from rest_framework.viewsets import ModelViewSet

from baskin_robbins.branch.api.serializers import BranchSerializer
from baskin_robbins.branch.models import Branch


class BranchViewSet(ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
