from django.core.management.base import BaseCommand

from src.profiles.models import UserSonet
from src.followers.models import Follower
from src.wall.models import Post


class Command(BaseCommand):
    """Test command for database"""


    def handle(self, *args, **options):
        self.create_user()
        self.create_follower()
        self.create_post()
        print('[INFO] Success!')


    def create_user(self):
        for i in range(10):
            user = UserSonet.objects.create(
                username=f"test_user_{i}",
                first_name=f"first_name_{i}",
                last_name=f"last_name_{i}",
                email=f"test{i}@gmail.com",
                biography=f"{i} Test Biography",
                github=f"github.com/{i}",
                linkedin=f"linked.com/{i}",
                is_active=True,
                work_place=f"work_place_{i}",
                work_position=f"work_position_{i}",
                phone=f"1234567890{i}"
            )
                
            user.set_password(f'test_password{i}')
            user.save()
            print(f'[INFO] user {i} was successfully created')


    def create_follower(self):
        user_list = UserSonet.objects.order_by()[1:]
        for user in user_list:
            Follower.objects.create(user=user, subscriber_id=1)
            print(f'[INFO] Follower {user} was successfully created')


    def create_post(self):
        user_list = UserSonet.objects.all()
        for user in user_list:
            print(f'[INFO] Test posts for {user}')
            for i in range(10):
                Post.objects.create(text=f"Test post{i}", user=user)
                print(f'[INFO] Post was successfully created')
