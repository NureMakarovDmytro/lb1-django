import django
from django.conf import settings

settings.configure(
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    INSTALLED_APPS=["django.contrib.contenttypes", "django.contrib.auth"],
    DEFAULT_AUTO_FIELD="django.db.models.AutoField",
    USE_TZ=False,
)
django.setup()

from django.db import models, connection


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")
    author = models.CharField(max_length=100, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        app_label = "demo"
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
        ordering = ["-published_at"]


with connection.schema_editor() as se:
    se.create_model(Article)

Article.objects.create(title="Django для початківців", text="Основи роботи з Django: проект, додаток, моделі.", author="Іваненко І.І.")
Article.objects.create(title="ORM в Django: просунуті запити", text="Вивчення QuerySet API та складних фільтрів.", author="Іваненко І.І.")
Article.objects.create(title="Шаблони та статичні файли", text="Як організувати templates і підключити CSS.", author="Петренко П.П.")
Article.objects.create(title="REST API в Django", text="Django REST Framework: серіалізатори та ViewSet.", author="Сидоренко О.В.")

SEP = "=" * 62

print(SEP)
print("  ЗАВДАННЯ 1 (РІВЕНЬ 1) — усі статті (адмін-панель / ORM)")
print(SEP)
print(f"  {'Заголовок':<36} {'Автор':<18} Дата")
print("-" * 62)
for a in Article.objects.all():
    date = a.published_at.strftime("%d.%m.%Y")
    print(f"  {a.title:<36} {a.author:<18} {date}")
print(f"\n  Всього статей: {Article.objects.count()}")

print()
print(SEP)
print("  ЗАВДАННЯ 1 (РІВЕНЬ 2) — Django ORM: статті автора")
print(SEP)

author_name = "Іваненко І.І."
qs = Article.objects.filter(author=author_name).order_by("-published_at")

print(f"  Запит: Article.objects.filter(author='{author_name}')")
print(f"  SQL:   {qs.query}")
print()
print(f"  Знайдено {qs.count()} статей для автора «{author_name}»:")
print()
for a in qs:
    print(f"  Заголовок : {a.title}")
    print(f"  Текст     : {a.text}")
    print(f"  Дата      : {a.published_at.strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"  Автор     : {a.author}")
    print("-" * 62)
