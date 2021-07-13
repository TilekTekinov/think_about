from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    parent_id = models.ForeignKey('self', verbose_name=_('Category'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Article(models.Model):
    category_id = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.SET_NULL)
    user_id = models.ForeignKey('account.User', verbose_name=_('User'), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='article_images/', verbose_name=_('Cover of the article'))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title
