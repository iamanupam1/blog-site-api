from statistics import mode
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

STATUS = (
    (0,"Draft"),
    (1,"Published")
)

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    path_alias = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category_name
    
    def save(self):
        self.path_alias = "category/" + slugify(self.category_name)
        super(Category, self).save()

class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail_img = models.ImageField(upload_to='article-thumbnail/', blank=True)
    excerpt = models.CharField(max_length=120)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    writer = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('article-detail', args =[self.slug])

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, blank=False)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comment"

    def __str__(self):
        return self.email


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name

