from django.conf import settings
from django.db import models
from django.utils import timezone
from django.forms import forms
from django.core.files.images import get_image_dimensions

from PIL import Image
from tinymce import models as tinymce_models
# Create your models here.


# Checking whether the image sizes match
class LimitedImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        self.max_upload_size = kwargs.pop('max_upload_size', None)
        self.min_dim = kwargs.pop('min_dim', None)
        self.max_dim = kwargs.pop('max_dim', None)
        if not self.max_upload_size:
            self.max_upload_size = settings.FILE_UPLOAD_MAX_MEMORY_SIZE
        super(LimitedImageField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(LimitedImageField, self).clean(*args, **kwargs)
        try:
            img_file = data.file
            if img_file.size > self.max_upload_size:
                err_msg = 'Размер файла не должен превышать {}'.format(self.max_upload_size)
                raise forms.ValidationError(err_msg)

            w, h = get_image_dimensions(img_file)
            if self.min_dim:
                if (w < self.min_dim[0]) or (h < self.min_dim[1]):
                    err_msg = 'Разрешение изображения не должно быть меньше, чем {}x{}'.format(*self.min_dim)
                    raise forms.ValidationError(err_msg)
                if self.max_dim:
                    if (w > self.max_dim[0]) or (h > self.max_dim[1]):
                        err_msg = 'Разрешение изображения не должно превышать {}x{}'.format(*self.max_dim)
                        raise forms.ValidationError(err_msg)
        except AttributeError:
            pass
        return data


# resize image function
def resize_image(input_image_path, size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size)
    resized_image.save(input_image_path, quality=95)
    return resized_image


# Post model
class Post(models.Model):

    HEADER_IMAGE_RESOLUTION = (1000, 1000)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=35, help_text='Title must not exceed 35 characters.')
    description = models.CharField(max_length=160, default='Федеральная сеть центров образования цифрового,'
                                                           ' естественнонаучного, технического и гуманитарного '
                                                           'профилей, организованная в рамках проекта '
                                                           '"Современная школа".',
                                   help_text='Description must not exceed 160 characters.')
    text = tinymce_models.HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    header_image = LimitedImageField('Header Image', default="images/1000x1000.jpg",
                                     upload_to='images/',
                                     min_dim=HEADER_IMAGE_RESOLUTION,
                                     max_dim=HEADER_IMAGE_RESOLUTION,
                                     help_text='Header image should be {}x{} in size.'.format(*HEADER_IMAGE_RESOLUTION))
    published_date = models.DateTimeField(blank=True, null=True)
    image = LimitedImageField(blank=True)

    def publish(self, request, obj, form, change):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class PostAdditionalImages(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = LimitedImageField('Image', upload_to='images/', min_dim=(400, 300), max_dim=(3840, 2160), blank=True,
                              null=True)
    text = tinymce_models.HTMLField(blank=True, null=True)


# class PostAdditionalText(models.Model):
#     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
