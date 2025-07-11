from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

class Command(BaseCommand):
    help = 'Promote a user by email to staff or superuser, or grant specific permissions'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        email = input("Enter the user's email: ").strip()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("User not found."))
            return

        print("\nWhat do you want to do?")
        print("1. Make user staff")
        print("2. Make user superuser")
        print("3. Grant specific permission")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"{user.email} is now a staff member."))

        elif choice == '2':
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"{user.email} is now a superuser."))

        elif choice == '3':
            codename = input("Enter permission codename (e.g., change_event): ").strip()
            try:
                permission = Permission.objects.get(codename=codename)
                user.user_permissions.add(permission)
                self.stdout.write(self.style.SUCCESS(f"Permission '{codename}' added to {user.email}."))
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR("Permission codename not found."))
        else:
            self.stdout.write(self.style.ERROR("Invalid choice."))
