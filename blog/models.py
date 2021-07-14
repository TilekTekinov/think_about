from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    parent = models.ForeignKey('self', verbose_name=_('Category'), on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.SET_NULL,
                                 blank=True, null=True)
    user = models.ForeignKey('account.User', verbose_name=_('User'), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='article_images/', verbose_name=_('Cover of the article'))

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class FeedBack(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    email = models.CharField(max_length=100, verbose_name=_('Email'))
    phone = models.CharField(max_length=100, verbose_name=_('Phone Number'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        verbose_name = _("FeedBack")
        verbose_name_plural = _("FeedBacks")

    def __str__(self):
        return self.name
