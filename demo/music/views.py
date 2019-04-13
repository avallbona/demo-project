from rest_framework.generics import ListAPIView

from .serializers import PortfolioSerializer
from .models import Portfolio


class PortfolioListView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
