from django.urls import reverse
class Post(models.Model):
# ...
def get_absolute_url(self):
return reverse('blog:post_detail',
args=[self.publish.year,
self.publish.month,
self.publish.day,
self.slug])