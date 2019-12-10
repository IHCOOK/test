from django.db import models
from django.core import validators


class Item(models.Model):
    EVA = (
        (1, 'very good'),
        (2, 'good'),
        (3, 'bad'),
        (4, 'very bad'),
    )

    GENRU = (
        (1, "漫画"),
        (2, "小説"),
    )

    type = models.IntegerField(
        verbose_name='ジャンル',
        choices=GENRU,
        default=1
    )
    name = models.CharField(
        verbose_name='書名',
        max_length=200,
    )
    author = models.CharField(
        verbose_name='著者',
        max_length=200,
    )
    grade = models.IntegerField(
        verbose_name='評価',
        choices=EVA,
        default=1
    )
    memo = models.TextField(
        verbose_name='感想',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'
