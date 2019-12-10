from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):
    name = filters.CharFilter(label='書名', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('type', 'type'),
            ('name', 'name'),
            ('author', 'author'),
        ),
        field_labels={
            'type': 'ジャンル',
            'name': '書名',
            'author': '著者',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ('type', 'name', 'author', 'grade', )
