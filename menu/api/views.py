from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PositionSerializer
from position.models import Position


class ApiPositionViewSet(CreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (IsAuthenticated,)
