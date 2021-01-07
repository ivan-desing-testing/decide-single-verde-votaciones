from django.urls import path
from .views import CurrentTallyView


urlpatterns = [
    path('<int:voting_id>/', CurrentTallyView.as_view()),
]
