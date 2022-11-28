from django.utils.text import slugify
from rest_framework import serializers

from baskin_robbins.branch.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"
        read_only_fields = ("slug", "created_at", "updated_at")

    def create(self, validated_data):
        return super().create(
            {**validated_data, "slug": slugify(validated_data.get("name"))}
        )

    def update(self, instance, validated_data):
        return super().update(
            instance, {**validated_data, "slug": slugify(validated_data.get("name"))}
        )
