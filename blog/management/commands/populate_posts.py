from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="this command inserts post data"

    def handle(self, *args: Any, **options: Any) :

        titles=[
    "The Enchanted Forest: A Journey Beyond Reality",
"Tech Trends 2024: Innovations Shaping the Future",
"Healthy Eating: Delicious Recipes for a Balanced Diet",
"Mastering Mindfulness: Techniques for Stress-Free Living",
"Travel Destinations: Hidden Gems Around the World",
"Home Décor: Transform Your Space with These Ideas",
"Fitness Fundamentals: Effective Workouts for Beginners",
"Financial Freedom: Smart Strategies for Managing Money",
"Gardening Guide: Grow Your Own Organic Vegetables",
"Parenting Tips: Raising Happy and Confident Kids",

]

        contents=[
    "The Enchanted Forest: A Journey Beyond Reality",
"Tech Trends 2024: Innovations Shaping the Future",
"Healthy Eating: Delicious Recipes for a Balanced Diet",
"Mastering Mindfulness: Techniques for Stress-Free Living",
"Travel Destinations: Hidden Gems Around the World",
"Home Décor: Transform Your Space with These Ideas",
"Fitness Fundamentals: Effective Workouts for Beginners",
"Financial Freedom: Smart Strategies for Managing Money",
"Gardening Guide: Grow Your Own Organic Vegetables",
"Parenting Tips: Raising Happy and Confident Kids",

]

        img_urls =[
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",

]
        for title,content,img_url in zip(titles , contents,img_urls):
             Post.objects.create(title=title,content=content,img_url=img_url)

        self.stdout.write(self.style.SUCCESS("COMPLETED INSERTING DATA"))
            
