from django.db import models
from utils.models import TimeStampAbstractModel
from slugify import slugify



class News(TimeStampAbstractModel):
    title = models.CharField('Название', max_length=55)
    image = models.ImageField('Изображение', upload_to='news/')
    content = models.TextField('Содержание')
    views = models.PositiveBigIntegerField('Просмотры', default=0, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def display_date(self):
        return self.created_at.strftime('%d.%m.%Y %H:%M')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super (News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class SocialNetwork(models.Model):

    NETWORKS = [
        ('instagram', 'Instagram'),
        ('telegram', 'Telegram'),
        ('threads', 'Threads'),
        ('facebook', 'Facebook'),
        ('whatsapp', 'WhatsApp'),
        ('youtube', 'YouTube')
    ]
    name = models.CharField(max_length=55)
    type = models.CharField(max_length=15, choices=NETWORKS)
    url = models.URLField()
    order = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return f'{self.name} - {self.type}'




class ContactInfo(models.Model):
    address = models.CharField('Адрес', max_length=255)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', max_length=255)
    map_embed = models.TextField('Карта (iframe)', blank=True)
    working_hours = models.CharField('Время работы', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'



class PodcastChannel(TimeStampAbstractModel):
    name = models.CharField('Название', max_length=55)
    image = models.ImageField('Изображение', upload_to='podcast/channel-images/')
    slug = models.SlugField(unique=True, blank=True)
    youtube_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Подкаст'
        verbose_name_plural = 'Подкасты'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super (PodcastChannel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    


class PodcastRelease(TimeStampAbstractModel):
    channel = models.ForeignKey(PodcastChannel, on_delete=models.PROTECT, related_name='releases')
    name = models.CharField('Название', max_length=55)
    image = models.ImageField('Изображение', upload_to='podcast/release-images/', default='defaults/podcast-release.jpg')
    youtube_id = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Выпуск подкаста'
        verbose_name_plural = 'Выпуски подкаста'

    def __str__(self):
        return f'{self.channel.name} - {self.name}'
    
    def display_date(self):
        return self.created_at.strftime('%d.%m.%Y %H:%M')
    
    @property
    def youtube_url(self):
        return f"https://www.youtube.com/embed/{self.youtube_id}"
    
    @property
    def name_display(self):
        ep_num = self.channel.releases.count()
        return f'Эпизод {ep_num}:{self.name}'


class MainSlider(models.Model):
    text = models.CharField(max_length=55)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='banner-photos/')
    btn_text = models.CharField(max_length=15)



