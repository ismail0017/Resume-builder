# API views - only if REST framework is available
try:
    from rest_framework import viewsets
    from rest_framework.permissions import IsAuthenticated
    from .models import Resume, WorkExperience, Education
    
    # Add your API viewsets here when needed
    class ResumeViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticated]
        
        def get_queryset(self):
            return Resume.objects.filter(user=self.request.user)
            
except ImportError:
    # REST framework not available
    pass
