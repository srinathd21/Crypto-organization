from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, permissions, status
from rest_framework.response import Response
from core.models import Organization
from core.serializers.organization_serializer import OrganizationSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['created_at']  
    search_fields = ['name']  
    ordering_fields = ['created_at']  

    def get_queryset(self):
        return Organization.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            return Response({"detail": "You do not have permission to edit this organization."}, status=status.HTTP_403_FORBIDDEN)

        name = request.data.get("name")
        if not name:
            return Response({"detail": "Name field is required."}, status=status.HTTP_400_BAD_REQUEST)

        instance.name = name
        instance.save()

        return Response({"message": "Organization name updated successfully!", "name": instance.name})
