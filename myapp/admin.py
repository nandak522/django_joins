from django.contrib import admin
from myapp.models import Question, Answer, QuestionComment, AnswerComment 
from myapp.models import Reputation, Follower, Mention

class QuestionAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('title','raised_by')
    search_fields = ('title',)
    
class AnswerAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('description', 'given_by')
    search_fields = ('description',)
    
class QuestionCommentAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('description', 'author')
    search_fields = ('description',)
    
class AnswerCommentAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('description', 'author')
    search_fields = ('description',)
    
class ReputationAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('points', 'user')
    search_fields = ('points',)
    
class FollowerAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('user','following')
    search_fields = ('user',)
    
class MentionAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('user','count')
    search_fields = ('user',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuestionComment, QuestionCommentAdmin)
admin.site.register(AnswerComment, AnswerCommentAdmin)
admin.site.register(Reputation, ReputationAdmin)
admin.site.register(Follower, FollowerAdmin)
admin.site.register(Mention, MentionAdmin)