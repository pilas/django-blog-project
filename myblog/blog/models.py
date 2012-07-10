from django.db import models
from django.contrib import admin
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __unicode__(self):
	return self.title

    
    class admin:
	pass
		

class Comment(models.Model):
    body = models.TextField()
    author =  models.CharField(max_length=60)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    post = models.ForeignKey(Post)

    

    def __unicode__(self):
	return self.author

    def body_first(self):
	return self.body[:60]

    
    class admin:
	pass


class CommentInline(admin.TabularInline):
        model=Comment

class PostAdmin(admin.ModelAdmin):
	
	list_display = ('title','created','updated')
	list_filter = ('created',)
	search_fields = ['title','body']
	inlines = [CommentInline,]	

class CommentAdmin(admin.ModelAdmin):
	list_display = ('author','post','body_first','created','updated')
	list_filter = ('created','author')
	

		



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
#admin.site.register(CommentInline)
