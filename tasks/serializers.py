from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):

    created_at_formatted = serializers.SerializerMethodField()

    priority_display = serializers.CharField(source='get_priority_display', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'is_complete',
            'priority_display',
            'created_at',
            'created_at_formatted',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_created_at_formatted(self, obj):
        return obj.created_at.strftime("%d/%m/%Y à %Hh%M")

    def get_priority_display(self, obj):
        return obj.priority

    def validate_title(self, value):

        if len(value) < 3:
            raise serializers.ValidationError("Task title must be at least 3 characters")

        return value.strip()

class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']

    def validate_title(self, value):

        if len(value) < 3:
            raise serializers.ValidationError("Task title must be at least 3 characters")

        return value.strip()

