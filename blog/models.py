from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_image_file_extension


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    parent = models.ForeignKey('self', verbose_name=_('Category'), on_delete=models.CASCADE, related_name='children',
                               blank=True, null=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.SET_NULL,
                                 blank=True, null=True)
    user = models.ForeignKey('account.User', verbose_name=_('User'), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='article_images/', verbose_name=_('Cover of the article'),
                              validators=[validate_image_file_extension])

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
