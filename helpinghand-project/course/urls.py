from django.urls import path

from .views import * 

app_name = 'course'
urlpatterns = [
        path('', course, name='course'),
        path('quiz/', QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', QuestionDeleteView.as_view(), name='question_delete'),
    
]