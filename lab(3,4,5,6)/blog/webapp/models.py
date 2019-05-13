from django.db import models

class Post(models.Model):

	title = models.CharField("Заголовок статьи", max_length=150)
	text = models.TextField("Содержание", max_length=5000)
	create = models.DateTimeField("Время создания", auto_now_add=True)
	author = models.TextField("Автор статьи", max_length=100)

	def __str__(self):
		return self.title