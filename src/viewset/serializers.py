from rest_framework import serializers


class FilterCommentListSerializer(serializers.ListSerializer):
    """Filter comments"""

    def to_representation(self, data):
        """
        Return a list of comments.

        :param data: List of comments
        :return: List of comments
        """
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveFilterCommentSerializer(serializers.Serializer):
    """Recursive filter comment serializer"""

    def to_representation(self, instance):
        serializers = self.parent.parent.__class__(instance, context=self.context)
        return serializers.data
    