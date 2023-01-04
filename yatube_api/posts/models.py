from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    """Stores a comments to a posts."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Stores a subscriptions of user."""
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )


class Group(models.Model):
    """Stores the unique groups."""
    description = models.TextField(
        verbose_name='Краткое описание группы'
    )
    slug = models.SlugField(
        verbose_name='Уникальное имя',
        unique=True
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    """Stores all information about posts."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Имя автора',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
    )
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Картинка',
        upload_to='posts/',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    text = models.TextField(
        verbose_name='Текст поста',
    )

    def __str__(self) -> str:
        return self.text[:15]
